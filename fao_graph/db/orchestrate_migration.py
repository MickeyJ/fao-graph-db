"""
Orchestrate all graph migrations
Generated from YAML configuration
"""
from pathlib import Path
from sqlalchemy import text
from fao_graph.utils import load_sql
from fao_graph.logger import logger
from fao_graph.db.db_connections import db_connections  # Updated import
from fao_graph.core.exceptions import MigrationError

# Import all node migrators
from fao_graph.db.pipelines.area_code.area_code import AreaCodeMigrator
from fao_graph.db.pipelines.reporter_country_code.reporter_country_code import ReporterCountryCodeMigrator
from fao_graph.db.pipelines.partner_country_code.partner_country_code import PartnerCountryCodeMigrator
from fao_graph.db.pipelines.item_code.item_code import ItemCodeMigrator

# Import all relationship migrators  
from fao_graph.db.pipelines.trade_detailed_trade_matrix__trades.trade_detailed_trade_matrix__trades import TradeDetailedTradeMatrixTradesMigrator
from fao_graph.db.pipelines.food_balance_sheets__produces.food_balance_sheets__produces import FoodBalanceSheetsProducesMigrator
from fao_graph.db.pipelines.food_balance_sheets__trades.food_balance_sheets__trades import FoodBalanceSheetsTradesMigrator
from fao_graph.db.pipelines.food_balance_sheets__consumes.food_balance_sheets__consumes import FoodBalanceSheetsConsumesMigrator
from fao_graph.db.pipelines.food_security_data__experiences.food_security_data__experiences import FoodSecurityDataExperiencesMigrator
from fao_graph.db.pipelines.food_security_data__measures.food_security_data__measures import FoodSecurityDataMeasuresMigrator
from fao_graph.db.pipelines.prices__has_price.prices__has_price import PricesHasPriceMigrator


def ensure_age_extension():
    """Ensure AGE extension is created in the graph database"""
    with db_connections.graph_session() as session:
        # Check if AGE extension exists
        result = session.execute(text("""
            SELECT 1 FROM pg_extension WHERE extname = 'age'
        """))
        
        if not result.first():
            logger.info("Creating AGE extension...")
            session.execute(text("CREATE EXTENSION age"))
            session.commit()
        else:
            logger.info("AGE extension already exists")


def create_graph():
    """Create the graph if it doesn't exist"""
    with db_connections.graph_session() as session:
        # Check if graph exists
        result = session.execute(text("""
            SELECT * FROM ag_catalog.ag_graph 
            WHERE name = 'fao_graph'
        """))
        
        if not result.first():
            logger.info("Creating graph fao_graph...")
            session.execute(text("SELECT create_graph('fao_graph')"))
            session.commit()
        else:
            logger.info("Graph fao_graph already exists")


def migrate_nodes():
    """Migrate all nodes"""
    logger.info("=" * 50)
    logger.info("          Starting node migrations...")
    logger.info("=" * 50)
    
    node_migrators = [
        ("AreaCode", AreaCodeMigrator()),
        ("ReporterCountryCode", ReporterCountryCodeMigrator()),
        ("PartnerCountryCode", PartnerCountryCodeMigrator()),
        ("ItemCode", ItemCodeMigrator()),
    ]
    
    for label, migrator in node_migrators:
        logger.info(f"\nMigrating {label} nodes...")
        try:
            migrator.migrate()
        except Exception as e:
            logger.error(f"Failed to migrate {label}: {e}")
            raise


def migrate_relationships():
    """Migrate all relationships"""
    logger.info("\n" + "=" * 50)
    logger.info("          Starting relationship migrations...")
    logger.info("=" * 50)
    
    relationship_migrators = [
        ("TRADES from trade_detailed_trade_matrix", TradeDetailedTradeMatrixTradesMigrator()),
        ("PRODUCES from food_balance_sheets", FoodBalanceSheetsProducesMigrator()),
        ("TRADES from food_balance_sheets", FoodBalanceSheetsTradesMigrator()),
        ("CONSUMES from food_balance_sheets", FoodBalanceSheetsConsumesMigrator()),
        ("EXPERIENCES from food_security_data", FoodSecurityDataExperiencesMigrator()),
        ("MEASURES from food_security_data", FoodSecurityDataMeasuresMigrator()),
        ("HAS_PRICE from prices", PricesHasPriceMigrator()),
    ]
    
    for description, migrator in relationship_migrators:
        logger.info(f"\nMigrating {description}...")
        try:
            migrator.migrate()
        except Exception as e:
            logger.error(f"Failed to migrate {description}: {e}")
            raise


def create_global_indexes():
    """Create global indexes for the graph"""
    logger.info("\n" + "=" * 50)
    logger.info("          Creating global indexes...")
    logger.info("=" * 50)
    
    try:
        with db_connections.graph_session() as session:
            # Load and execute the global indexes SQL
            index_queries = load_sql("create_global_indexes.sql", Path(__file__).parent)
            
            # Execute the index creation
            session.execute(text(index_queries))
            session.commit()
            
        logger.success("Global indexes created successfully")
    except Exception as e:
        logger.error(f"Failed to create global indexes: {e}")
        raise


def create_reference_links() -> None:
    """Create links between reference nodes with same codes."""
    logger.info("Creating reference links...")

    try:
        with db_connections.graph_session() as session:
            # Link areas
            link_areas = """
                SELECT count(*) as count FROM cypher('fao_graph', $$
                    MATCH (a1:AreaCode), (a2:AreaCode)
                    WHERE a1.area_code = a2.area_code 
                    AND a1.id < a2.id
                    CREATE (a1)-[rel:SAME_AREA_CODE]->(a2)
                $$) AS (result agtype);
            """
            
            result = session.execute(text(link_areas))
            area_count = result.scalar()
            logger.info(f"Created {area_count} SAME_AREA_CODE relationships")

            # Link items
            link_items = """
                SELECT count(*) as count FROM cypher('fao_graph', $$
                    MATCH (i1:ItemCode), (i2:ItemCode)
                    WHERE i1.item_code = i2.item_code 
                    AND i1.id < i2.id
                    CREATE (i1)-[rel:SAME_ITEM_CODE]->(i2)
                $$) AS (result agtype);
            """
            
            result = session.execute(text(link_items))
            item_count = result.scalar()
            logger.info(f"Created {item_count} SAME_ITEM_CODE relationships")
            
            session.commit()
            
        logger.success("Linked references successfully")
    except Exception as e:
        logger.error(f"Failed to link references: {e}")
        raise MigrationError(f"Failed to link reference nodes: {e}")


def main():
    """Run all migrations in order"""
    logger.info("Starting FAO Graph Database Migration")

    # Ensure AGE extension is created
    ensure_age_extension()

    # Ensure progress table exists
    db_connections.ensure_progress_table()
    
    # Create graph
    create_graph()
    
    # Migrate nodes first
    migrate_nodes()
    
    # Then migrate relationships
    migrate_relationships()
    
    # Create global indexes
    create_global_indexes()

    # Link duplicate reference nodes
    create_reference_links()
    
    logger.success("\n✅ Graph migration complete!")
    
    # Clean up connections
    db_connections.close()


if __name__ == "__main__":
    main()