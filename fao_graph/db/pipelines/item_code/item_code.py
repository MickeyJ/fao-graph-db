# yaml_migrator.py.jinja2
# Generated migrator for node item_code
from pathlib import Path
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class ItemCodeMigrator(GraphMigrationBase):
    """Migrator for ItemCode nodes from item_codes"""
    
    def __init__(self):
        super().__init__("item_codes", "node")
        self.node_label = "ItemCode"
    
    def get_migration_query(self) -> str:
        return load_sql("item_code.cypher.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("item_code_verify.cypher.sql", Path(__file__).parent)

    def get_index_queries(self) -> str:
        return load_sql("item_code_indexes.sql", Path(__file__).parent)
