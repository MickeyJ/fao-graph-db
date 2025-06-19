from typing import Dict, List, Any
from sqlalchemy import text

from src.core import db_connections
from utils import logger


class ReferenceDataMigrator:
    """Migrate reference tables to Neo4j nodes using SQL IDs."""

    def __init__(self):
        self.batch_size = 5000
        self.nodes_created = {}

    def migrate_countries(self) -> None:
        """Migrate area_codes to Country nodes."""
        logger.info("Migrating countries...")

        query = text(
            """
            SELECT 
                id as sql_id,
                area_code,
                area,
                area_code_m49,
                source_dataset
            FROM area_codes
            WHERE area_code NOT LIKE 'aquastat-%'  -- Skip aquastat duplicates
            ORDER BY id
        """
        )

        with db_connections.pg_session() as pg_session:
            result = pg_session.execute(query)
            countries = result.fetchall()

        logger.info(f"Found {len(countries)} country records to migrate")

        with db_connections.neo4j_session() as neo4j_session:
            for i in range(0, len(countries), self.batch_size):
                batch = countries[i : i + self.batch_size]

                neo4j_session.run(
                    """
                    UNWIND $batch as country
                    CREATE (c:Country {id: country.sql_id})
                    SET c.area_code = country.area_code,
                        c.name = country.area,
                        c.m49_code = country.area_code_m49,
                        c.source_dataset = country.source_dataset
                """,
                    batch=[dict(c._mapping) for c in batch],
                )

                logger.info(f"Created {min(i + self.batch_size, len(countries))}/{len(countries)} countries")

        self.nodes_created["countries"] = len(countries)

    def migrate_items(self) -> None:
        """Migrate item_codes to Item nodes."""
        logger.info("Migrating items...")

        query = text(
            """
            SELECT 
                id as sql_id,
                item_code,
                item,
                item_code_cpc,
                item_code_fbs,
                item_code_sdg,
                source_dataset
            FROM item_codes
            ORDER BY id
        """
        )

        with db_connections.pg_session() as pg_session:
            result = pg_session.execute(query)
            items = result.fetchall()

        logger.info(f"Found {len(items)} item records to migrate")

        with db_connections.neo4j_session() as neo4j_session:
            for i in range(0, len(items), self.batch_size):
                batch = items[i : i + self.batch_size]

                neo4j_session.run(
                    """
                    UNWIND $batch as item
                    CREATE (i:Item {id: item.sql_id})
                    SET i.item_code = item.item_code,
                        i.name = item.item,
                        i.cpc_code = item.item_code_cpc,
                        i.fbs_code = item.item_code_fbs,
                        i.sdg_code = item.item_code_sdg,
                        i.source_dataset = item.source_dataset
                """,
                    batch=[dict(i._mapping) for i in batch],
                )

                logger.info(f"Created {min(i + self.batch_size, len(items))}/{len(items)} items")

        self.nodes_created["items"] = len(items)

    def migrate_elements(self) -> None:
        """Migrate elements to Element nodes."""
        logger.info("Migrating elements...")

        query = text(
            """
            SELECT 
                id as sql_id,
                element_code,
                element,
                source_dataset
            FROM elements
            ORDER BY id
        """
        )

        with db_connections.pg_session() as pg_session:
            result = pg_session.execute(query)
            elements = result.fetchall()

        logger.info(f"Found {len(elements)} element records to migrate")

        with db_connections.neo4j_session() as neo4j_session:
            neo4j_session.run(
                """
                UNWIND $elements as element
                CREATE (e:Element {id: element.sql_id})
                SET e.element_code = element.element_code,
                    e.name = element.element,
                    e.source_dataset = element.source_dataset
            """,
                elements=[dict(e._mapping) for e in elements],
            )

        self.nodes_created["elements"] = len(elements)

    def migrate_flags(self) -> None:
        """Migrate flags to Flag nodes."""
        logger.info("Migrating flags...")

        query = text(
            """
            SELECT 
                id as sql_id,
                flag,
                description,
                source_dataset
            FROM flags
            ORDER BY id
        """
        )

        with db_connections.pg_session() as pg_session:
            result = pg_session.execute(query)
            flags = result.fetchall()

        logger.info(f"Found {len(flags)} flag records to migrate")

        with db_connections.neo4j_session() as neo4j_session:
            neo4j_session.run(
                """
                UNWIND $flags as flag
                CREATE (f:Flag {id: flag.sql_id})
                SET f.flag = flag.flag,
                    f.description = flag.description,
                    f.source_dataset = flag.source_dataset
            """,
                flags=[dict(f._mapping) for f in flags],
            )

        self.nodes_created["flags"] = len(flags)

    def create_year_nodes(self) -> None:
        """Create Year nodes for temporal queries."""
        logger.info("Creating year nodes...")

        query = text(
            """
            SELECT MIN(year) as min_year, MAX(year) as max_year
            FROM production_crops_livestock
            WHERE year IS NOT NULL AND year > 1900 AND year < 2100
        """
        )

        with db_connections.pg_session() as pg_session:
            result = pg_session.execute(query).fetchone()

            if not result or result.min_year is None or result.max_year is None:
                logger.warning("No valid year range found in production data")
                return

            min_year, max_year = result.min_year, result.max_year

        logger.info(f"Creating year nodes from {min_year} to {max_year}")

        years = []
        for year in range(min_year, max_year + 1):
            years.append({"year": year, "decade": (year // 10) * 10, "century": (year // 100) * 100})

        with db_connections.neo4j_session() as neo4j_session:
            neo4j_session.run(
                """
                UNWIND $years as year
                CREATE (y:Year {year: year.year})
                SET y.decade = year.decade,
                    y.century = year.century
            """,
                years=years,
            )

        self.nodes_created["years"] = len(years)

    def create_reference_links(self) -> None:
        """Create links between reference nodes with same codes."""
        logger.info("Creating reference links...")

        with db_connections.neo4j_session() as neo4j_session:
            # Link countries with same area_code
            neo4j_session.run(
                """
                MATCH (c1:Country), (c2:Country)
                WHERE c1.area_code = c2.area_code 
                  AND c1.id < c2.id
                CREATE (c1)-[:SAME_AREA_CODE]->(c2)
            """
            )

            # Link items with same item_code
            neo4j_session.run(
                """
                MATCH (i1:Item), (i2:Item)
                WHERE i1.item_code = i2.item_code 
                  AND i1.id < i2.id
                CREATE (i1)-[:SAME_ITEM_CODE]->(i2)
            """
            )

            # Link elements with same element_code
            neo4j_session.run(
                """
                MATCH (e1:Element), (e2:Element)
                WHERE e1.element_code = e2.element_code 
                  AND e1.id < e2.id
                CREATE (e1)-[:SAME_ELEMENT_CODE]->(e2)
            """
            )

            logger.info("Reference links created")

    def migrate_all(self) -> None:
        """Run all reference data migrations."""
        try:
            self.migrate_countries()
            self.migrate_items()
            self.migrate_elements()
            self.migrate_flags()
            self.create_year_nodes()
            self.create_reference_links()

            logger.info(f"Reference data migration complete! Created: {self.nodes_created}")

        except Exception as e:
            logger.error(f"Migration failed: {e}")
            raise


if __name__ == "__main__":
    migrator = ReferenceDataMigrator()
    migrator.migrate_all()
