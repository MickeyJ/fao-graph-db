# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for emissions_livestock EMITS relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class EmissionsLivestockEmitsMigrator(GraphMigrationBase):
    """Migrator for emissions_livestock EMITS relationships"""
    
    def __init__(self):
        super().__init__("emissions_livestock", "relationship")
        self.relationship_type = "EMITS"
        self.element_codes = ['5111', '72254', '72256', '72300', '72301', '72306', '72340', '72341', '72346', '72360', '723601', '723602', '72361', '723611', '723612', '72366', '72380', '723801', '723802', '72381', '723811', '723812', '72386', '72431', '72441']
        self.elements = ['Stocks', 'Enteric fermentation (Emissions CH4)', 'Manure management (Emissions CH4)', 'Manure left on pasture (Emissions N2O)', 'Emissions (N2O) (Manure applied)', 'Manure management (Emissions N2O)', 'Manure left on pasture (Direct emissions N2O)', 'Manure applied to soils (Direct emissions N2O)', 'Manure management (Direct emissions N2O)', 'Manure left on pasture (Indirect emissions N2O)', 'Indirect emissions (N2O that volatilises) (Manure on pasture)', 'Indirect emissions (N2O that leaches) (Manure on pasture)', 'Manure applied to soils (Indirect emissions N2O)', 'Indirect emissions (N2O that volatilises) (Manure applied)', 'Indirect emissions (N2O that leaches) (Manure applied)', 'Manure management (Indirect emissions N2O)', 'Manure left on pasture (N content)', 'Manure left on pasture that volatilises (N content)', 'Manure left on pasture that leaches (N content)', 'Manure applied to soils (N content)', 'Manure applied to soils that volatilises (N content)', 'Manure applied to soils that leaches (N content)', 'Manure management (manure treated, N content)', 'Livestock total (Emissions N2O)', 'Livestock total (Emissions CH4)']
        self.relationship_properties = {"category": "total", "element": "Livestock total (Emissions CH4)", "element_code": "72441", "gas_type": "CH4", "source": "livestock"}
    
    def get_migration_query(self) -> str:
        return load_sql("emissions_livestock_emits.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("emissions_livestock_emits_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("emissions_livestock_emits_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for emissions_livestock EMITS relationships"""
        logger.info(f"Starting emissions_livestock EMITS relationship migration...")
        logger.info(f"  Elements: Stocks, Enteric fermentation (Emissions CH4), Manure management (Emissions CH4), Manure left on pasture (Emissions N2O), Emissions (N2O) (Manure applied), Manure management (Emissions N2O), Manure left on pasture (Direct emissions N2O), Manure applied to soils (Direct emissions N2O), Manure management (Direct emissions N2O), Manure left on pasture (Indirect emissions N2O), Indirect emissions (N2O that volatilises) (Manure on pasture), Indirect emissions (N2O that leaches) (Manure on pasture), Manure applied to soils (Indirect emissions N2O), Indirect emissions (N2O that volatilises) (Manure applied), Indirect emissions (N2O that leaches) (Manure applied), Manure management (Indirect emissions N2O), Manure left on pasture (N content), Manure left on pasture that volatilises (N content), Manure left on pasture that leaches (N content), Manure applied to soils (N content), Manure applied to soils that volatilises (N content), Manure applied to soils that leaches (N content), Manure management (manure treated, N content), Livestock total (Emissions N2O), Livestock total (Emissions CH4)")
        logger.info(f"  Properties: {'source': 'livestock', 'gas_type': 'CH4', 'category': 'total', 'element_code': '72441', 'element': 'Livestock total (Emissions CH4)'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} EMITS relationships from emissions_livestock")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nemissions_livestock relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate emissions_livestock relationships: {e}")
            raise MigrationError(f"emissions_livestock relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass