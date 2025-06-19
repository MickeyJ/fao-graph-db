# src/neo4j/schema.py
from typing import List, Dict, Any
from utils import logger
from src.core import db_connections


class Neo4jSchema:
    """Manage Neo4j schema creation."""

    def __init__(self):
        self.constraints_created = []
        self.indexes_created = []

    def create_constraint(self, name: str, cypher: str) -> None:
        """Create a single constraint."""
        with db_connections.neo4j_session() as session:
            try:
                session.run(cypher)
                self.constraints_created.append(name)
                logger.info(f"Created constraint: {name}")
            except Exception as e:
                logger.warning(f"Constraint {name} may already exist: {e}")

    def create_index(self, name: str, cypher: str) -> None:
        """Create a single index."""
        with db_connections.neo4j_session() as session:
            try:
                session.run(cypher)
                self.indexes_created.append(name)
                logger.info(f"Created index: {name}")
            except Exception as e:
                logger.warning(f"Index {name} may already exist: {e}")

    def setup_reference_node_constraints(self) -> None:
        """Create constraints for reference table nodes."""

        # Countries
        self.create_constraint(
            "country_id_unique",
            "CREATE CONSTRAINT country_id_unique IF NOT EXISTS FOR (c:Country) REQUIRE c.id IS UNIQUE",
        )

        # Items
        self.create_constraint(
            "item_id_unique", "CREATE CONSTRAINT item_id_unique IF NOT EXISTS FOR (i:Item) REQUIRE i.id IS UNIQUE"
        )

        # Elements
        self.create_constraint(
            "element_id_unique",
            "CREATE CONSTRAINT element_id_unique IF NOT EXISTS FOR (e:Element) REQUIRE e.id IS UNIQUE",
        )

        # Flags
        self.create_constraint(
            "flag_id_unique", "CREATE CONSTRAINT flag_id_unique IF NOT EXISTS FOR (f:Flag) REQUIRE f.id IS UNIQUE"
        )

        # Year
        self.create_constraint(
            "year_unique", "CREATE CONSTRAINT year_unique IF NOT EXISTS FOR (y:Year) REQUIRE y.year IS UNIQUE"
        )

    def setup_indexes(self) -> None:
        """Create indexes for common queries."""

        # Core node lookups
        self.create_index("country_name", "CREATE INDEX country_name IF NOT EXISTS FOR (c:Country) ON (c.name)")
        self.create_index(
            "country_area_code", "CREATE INDEX country_area_code IF NOT EXISTS FOR (c:Country) ON (c.area_code)"
        )
        self.create_index(
            "country_source_dataset",
            "CREATE INDEX country_source_dataset IF NOT EXISTS FOR (c:Country) ON (c.source_dataset)",
        )
        self.create_index(
            "country_area_source",
            "CREATE INDEX country_area_source IF NOT EXISTS FOR (c:Country) ON (c.area_code, c.source_dataset)",
        )

        self.create_index("item_name", "CREATE INDEX item_name IF NOT EXISTS FOR (i:Item) ON (i.name)")
        self.create_index("item_item_code", "CREATE INDEX item_item_code IF NOT EXISTS FOR (i:Item) ON (i.item_code)")
        self.create_index(
            "item_source_dataset", "CREATE INDEX item_source_dataset IF NOT EXISTS FOR (i:Item) ON (i.source_dataset)"
        )
        self.create_index(
            "item_code_source",
            "CREATE INDEX item_code_source IF NOT EXISTS FOR (i:Item) ON (i.item_code, i.source_dataset)",
        )

        self.create_index("element_name", "CREATE INDEX element_name IF NOT EXISTS FOR (e:Element) ON (e.name)")
        self.create_index(
            "element_element_code",
            "CREATE INDEX element_element_code IF NOT EXISTS FOR (e:Element) ON (e.element_code)",
        )
        self.create_index(
            "element_source_dataset",
            "CREATE INDEX element_source_dataset IF NOT EXISTS FOR (e:Element) ON (e.source_dataset)",
        )

    def setup_all(self) -> None:
        """Run complete schema setup."""
        logger.info("Starting Neo4j schema setup...")

        # Constraints first (they create indexes automatically)
        self.setup_reference_node_constraints()

        # Then additional indexes
        self.setup_indexes()

        logger.info(
            f"Schema setup complete! Created {len(self.constraints_created)} constraints, {len(self.indexes_created)} indexes"
        )

        # Show what was created
        with db_connections.neo4j_session() as session:
            result = session.run("SHOW CONSTRAINTS")
            print("\nConstraints:")
            for record in result:
                print(f"  - {record['name']}")

            result = session.run("SHOW INDEXES")
            print("\nIndexes:")
            for record in result:
                print(f"  - {record['name']}")

    def reset_database(self) -> None:
        """Complete reset - drop all data and constraints."""
        logger.warning("Resetting Neo4j database - this will delete ALL data!")

        with db_connections.neo4j_session() as session:
            # Drop all constraints first
            logger.info("Dropping all constraints...")
            result = session.run("SHOW CONSTRAINTS")
            constraints = [record["name"] for record in result]

            for constraint in constraints:
                session.run(f"DROP CONSTRAINT {constraint}")
                logger.info(f"Dropped constraint: {constraint}")

            # Drop all indexes
            logger.info("Dropping all indexes...")
            result = session.run("SHOW INDEXES")
            indexes = [record["name"] for record in result if record["type"] != "LOOKUP"]

            for index in indexes:
                session.run(f"DROP INDEX {index}")
                logger.info(f"Dropped index: {index}")

            # Delete all nodes and relationships
            logger.info("Deleting all nodes and relationships...")
            session.run("MATCH (n) DETACH DELETE n")

            # Verify
            result = session.run("MATCH (n) RETURN count(n) as count")
            count = result.single()["count"]
            logger.info(f"Database reset complete. Node count: {count}")


# For easy CLI usage
if __name__ == "__main__":
    schema = Neo4jSchema()
    schema.setup_all()
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "reset":
        schema.reset_database()
        schema.setup_all()
    else:
        schema.setup_all()
