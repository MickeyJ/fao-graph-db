# yaml_migrator.py.jinja2
# Generated migrator for node partner_country_code
from pathlib import Path
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class PartnerCountryCodeMigrator(GraphMigrationBase):
    """Migrator for PartnerCountryCode nodes from partner_country_codes"""
    
    def __init__(self):
        super().__init__("partner_country_codes", "node")
        self.node_label = "PartnerCountryCode"
    
    def get_migration_query(self) -> str:
        return load_sql("partner_country_code.cypher.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("partner_country_code_verify.cypher.sql", Path(__file__).parent)

    def get_index_queries(self) -> str:
        return load_sql("partner_country_code_indexes.sql", Path(__file__).parent)
