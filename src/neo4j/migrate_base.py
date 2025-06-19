from abc import ABC, abstractmethod
import argparse
from typing import Dict, List, Sequence, Any, Optional, Type, TypeVar
from sqlalchemy import text
from sqlalchemy.engine import Row

from src.core import db_connections
from utils import logger

T = TypeVar("T", bound="BaseMigrator")


class MigrationError(Exception):
    """Base exception for migration errors."""

    pass


class BaseMigrator(ABC):
    """Abstract base class for migrating PostgreSQL data to Neo4j relationships."""

    def __init__(self, source_dataset: str):
        self.source_dataset = source_dataset
        self.batch_size = 5000
        self.relationships_created = 0
        self.relationships_updated = 0

    def get_count_query(self) -> str:
        """Return SQL query to count total records to migrate.
        Default implementation - override if needed."""
        return f"""
            SELECT COUNT(*) as total
            FROM {self.source_dataset} sds
            WHERE sds.value > 0
        """

    @abstractmethod
    def get_migration_query(self) -> str:
        """Return SQL query to fetch records for migration with LIMIT/OFFSET."""
        pass

    @abstractmethod
    def create_relationships(self, records: Sequence[Row]) -> None:
        """Create Neo4j relationships from PostgreSQL records."""
        pass

    @abstractmethod
    def get_verification_queries(self) -> Dict[str, str]:
        """Return Neo4j queries for verification. Should include 'total_count' key."""
        pass

    def update_relationships(self, records: Sequence[Row]) -> None:
        """Update existing Neo4j relationships. Override in subclasses."""
        raise NotImplementedError("Subclasses must implement update_relationships if using update mode")

    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Main migration entry point with resume capability.

        Args:
            start_offset: Offset to start from
            mode: 'create' for new relationships, 'update' for updating existing
        """
        logger.info(f"Starting {self.source_dataset} migration in {mode} mode from offset {start_offset:,}...")
        logger.info(f"Using batch size: {self.batch_size}")

        try:
            # Count total records
            count_query = text(self.get_count_query())

            with db_connections.pg_session() as session:
                total_records = session.execute(count_query).scalar() or 0
                logger.info(f"Total records to process: {total_records:,}")

                if start_offset > 0:
                    logger.info(
                        f"Resuming from offset {start_offset:,} ({start_offset/total_records*100:.1f}% already done)"
                    )
        except Exception as e:
            raise MigrationError(f"Failed to count total records: {e}") from e

        # Get migration query
        query = text(self.get_migration_query())
        offset = start_offset

        try:
            while offset < total_records:
                with db_connections.pg_session() as pg_session:
                    # Fetch batch
                    result = pg_session.execute(query, {"limit": self.batch_size, "offset": offset})
                    records = result.fetchall()

                    if not records:
                        break

                    # Process batch based on mode
                    try:
                        if mode == "create":
                            self.create_relationships(records)
                        elif mode == "update":
                            self.update_relationships(records)
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

        except KeyboardInterrupt:
            logger.warning(f"\nMigration interrupted at offset {offset}")
            logger.info(f"Resume with: --offset {offset}")
            raise
        except MigrationError:
            # Already logged, just re-raise
            raise
        except Exception as e:
            logger.error(f"Unexpected error at offset {offset}: {e}")
            logger.info(f"Resume with: --offset {offset}")
            raise MigrationError(f"Migration failed at offset {offset}") from e

    def log_progress(self, offset: int, total_records: int, pct_complete: float) -> None:
        """Log migration progress. Override for custom logging."""
        if self.relationships_updated > 0:
            logger.info(
                f"Progress: {offset:,}/{total_records:,} records ({pct_complete:.1f}%) | "
                f"Created: {self.relationships_created:,} | Updated: {self.relationships_updated:,}"
            )
        else:
            logger.info(
                f"Progress: {offset:,}/{total_records:,} records ({pct_complete:.1f}%) | "
                f"Created: {self.relationships_created:,}"
            )

    def verify_migration(self) -> None:
        """Verify the migration completed successfully."""
        queries = self.get_verification_queries()

        try:
            with db_connections.neo4j_session() as session:
                # Run total count query
                if "total_count" in queries:
                    result = session.run(queries["total_count"])
                    record = result.single()  # Store the result
                    if record:
                        # Get the first value from the record
                        total = record[list(record.keys())[0]]
                        logger.info(f"Verification complete: {total:,} relationships exist")
                    else:
                        logger.warning("No results from total count query")

                # Run any additional verification queries
                for name, query in queries.items():
                    if name != "total_count":
                        try:
                            self.run_verification_query(session, name, query)
                        except Exception as e:
                            logger.error(f"Verification query '{name}' failed: {e}")
                            # Continue with other verifications instead of failing

        except Exception as e:
            logger.error(f"Verification failed: {e}")
            raise MigrationError("Migration verification failed") from e

    def run_verification_query(self, session, name: str, query: str) -> None:
        """Run a single verification query. Override for custom handling."""
        logger.info(f"Running verification: {name}")
        result = session.run(query, source_dataset=self.source_dataset)
        for record in result:
            logger.info(f"  {dict(record)}")

    def transform_records_for_neo4j(
        self, records: Sequence[Row], field_mapping: Dict[str, str]
    ) -> List[Dict[str, Any]]:
        """Helper to transform PostgreSQL records to Neo4j format."""
        relationships = []
        for record in records:
            rel_data = {}
            for pg_field, neo_field in field_mapping.items():
                value = getattr(record, pg_field)
                if pg_field == "value" and value is not None:
                    value = float(value)
                rel_data[neo_field] = value
            relationships.append(rel_data)
        return relationships

    @classmethod
    def get_description(cls) -> str:
        """Return description for argparse. Override for custom description."""
        return f"Migrate {cls.__name__.replace('Migrator', '').lower()} data to Neo4j"

    @classmethod
    def add_custom_arguments(cls, parser: argparse.ArgumentParser) -> None:
        """Override to add custom command-line arguments."""
        pass

    @classmethod
    def handle_custom_arguments(cls, migrator: "BaseMigrator", args: argparse.Namespace) -> bool:
        """Override to handle custom arguments. Return True to skip normal migration."""
        return False

    @classmethod
    def main(cls: Type[T]) -> None:
        """Run the migration with command-line options."""
        parser = argparse.ArgumentParser(description=cls.get_description())
        parser.add_argument("--offset", type=int, default=0, help="Starting offset for resuming migration")
        parser.add_argument("--batch-size", type=int, default=5000, help="Batch size for processing")
        parser.add_argument(
            "--mode",
            choices=["create", "update"],
            default="create",
            help="Mode: create new relationships or update existing",
        )

        # Allow subclasses to add custom arguments
        cls.add_custom_arguments(parser)

        args = parser.parse_args()

        # This assumes subclasses override __init__ to not require parameters
        migrator = cls()  # type: ignore[call-arg]
        migrator.batch_size = args.batch_size

        try:
            # Handle custom arguments - if returns True, skip migration
            if cls.handle_custom_arguments(migrator, args):
                return

            migrator.migrate(start_offset=args.offset, mode=args.mode)
            migrator.verify_migration()

            if args.mode == "create":
                logger.info(f"Migration complete! Created {migrator.relationships_created:,} relationships")
            else:
                logger.info(f"Update complete! Updated {migrator.relationships_updated:,} relationships")

        except KeyboardInterrupt:
            logger.info("\nMigration cancelled by user")
            return
        except MigrationError as e:
            logger.error(f"Migration failed: {e}")
            return
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise
