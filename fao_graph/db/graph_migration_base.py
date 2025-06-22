import json
from abc import ABC, abstractmethod
from time import time
from typing import Dict, List, Sequence, Any, Optional, Type, TypeVar
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.engine import Row
from fao_graph.core.exceptions import MigrationError
from fao_graph.db.database import get_session, get_db
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class GraphMigrationBase(ABC):
    """Base class for all graph migrations"""

    def __init__(self, table_name: str, migration_type: str, project_name: str, node_label: str):
        self.project_name = project_name
        self.table_name = table_name
        self.migration_type = migration_type
        self.node_label = node_label
        self.batch_size = 5000
        self.created = 0
        self.updated = 0

    def get_count_query(self) -> str:
        """Return SQL query to count total records to migrate.
        Default implementation - override if needed."""
        return f"""
            SELECT COUNT(*) as total
            FROM {self.table_name}
            WHERE value > 0
        """

    @abstractmethod
    def get_migration_query(self) -> str:
        """Return SQL query to fetch records for migration with LIMIT/OFFSET."""
        pass

    @abstractmethod
    def get_verification_query(self) -> str:
        """Return AGE queries for verification. Should include 'total_count' key."""
        pass

    def get_index_queries(self) -> str:
        """Return SQL query to create indexes."""
        return ""

    def create(self, records: Sequence[Row], session: Session) -> None:
        """Create nodes or relationships"""
        pass

    def update(self, records: Sequence[Row], session: Session) -> None:
        """Update nodes or relationships"""
        pass

    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Main migration entry point with resume capability.

        Can be overridden for simpler migrations that don't need batch processing.
        """

        try:

            if self.migration_type == "node":
                with get_session() as session:
                    records = session.execute(text(f"SELECT * FROM {self.table_name}")).fetchall()

                    self.create(records, session)
                    self.run_verification_query(session, self.table_name)
                    # session.commit()

            else:
                logger.info(
                    f"Starting {self.table_name} relationship migration in {mode} mode from offset {start_offset:,}..."
                )
                logger.info(f"Using batch size: {self.batch_size}")
                # Count total records
                count_query = text(self.get_count_query())

                logger.warning(f"count_query: {count_query}")

                with get_session() as session:
                    logger.info("Starting count query...")
                    start_time = time()
                    total_records = session.execute(count_query).scalar() or 0

                    elapsed = time() - start_time
                    logger.info(f"Count query took {elapsed:.2f} seconds")
                    logger.info(f"Total records to process: {total_records:,}")

                    if start_offset > 0:
                        logger.info(
                            f"Resuming from offset {start_offset:,} ({start_offset/total_records*100:.1f}% already done)"
                        )

                # Get migration query
                query = text(self.get_migration_query())
                offset = start_offset

                while offset < total_records:
                    with get_session() as session:
                        # Fetch batch
                        result = session.execute(query, {"limit": self.batch_size, "offset": offset})
                        records = result.fetchall()

                        if not records:
                            break

                        # Process batch based on mode
                        try:
                            if mode == "create":
                                self.create(records, session)
                            elif mode == "update":
                                self.update(records, session)
                            else:
                                raise ValueError(f"Unknown mode: {mode}")
                        except Exception as e:
                            logger.error(f"Failed to process batch at offset {offset}: {e}")
                            logger.info(f"Resume with: --offset {offset}")
                            raise MigrationError(f"Batch processing failed at offset {offset}") from e

                        offset += len(records)

                        # Progress logging
                        pct_complete = offset / total_records * 100
                        self.log_progress(offset, total_records, pct_complete)

                self.run_verification_query(session, self.table_name)

        except KeyboardInterrupt:
            logger.error(f"\nMigration interrupted")
            raise
        except MigrationError as e:
            # Already logged, just re-raise
            raise MigrationError(f"Migration failed {e}")
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise MigrationError(f"Migration failed {e}")

    def create_indexes(self):
        """Create indexes"""
        with get_session() as session:
            index_queries = self.get_index_queries()
            session.execute(text(index_queries))
            logger.success(f"Created {self.table_name} indexes")

    def log_progress(self, offset: int, total_records: int, pct_complete: float) -> None:
        """Log migration progress. Override for custom logging."""
        if self.updated > 0:
            logger.info(
                f"Progress: {offset:,}/{total_records:,} records ({pct_complete:.1f}%) | "
                f"Created: {self.created:,} | Updated: {self.updated:,}"
            )
        else:
            logger.info(
                f"Progress: {offset:,}/{total_records:,} records ({pct_complete:.1f}%) | " f"Created: {self.created:,}"
            )

    def verify(self) -> None:
        """Verify the migration completed successfully."""

        # Verification complete: [('1759119356', '"Agriculture research spending"'), ('1364990269', '"Agricultural researchers (FTE)"'), ('111920601', '"Farm gate"'), ('943360549', '"Land
        # Use change"'), ('264809525', '"Pre- and Post- Production"'), ('1698056634', '"Agrifood systems"'), ('1169893819', '"Emissions on agricultural land"'), ('1879356118', '"Emissions
        # from crops"'), ('1250127877', '"Emissions from livestock"'), ('784534853', '"AFOLU"')]

        try:
            with get_session() as session:
                result = session.execute(text(self.get_verification_query())).mappings().all()
                logger.info(f"Verification complete: {result}")
                # logger.info(f"Verification complete: {json.dumps(result, indent=2)}")

        except Exception as e:
            logger.error(f"Verification Failed: {e}")
            raise MigrationError("Migration Verification Failed") from e

    def run_verification_query(self, session, name) -> None:
        """Run a single verification query. Override for custom handling."""
        logger.info(f"Running verification: {name}")
        result = session.execute(text(self.get_verification_query())).mappings().all()
        for record in result:
            logger.info(f"  {record}")
