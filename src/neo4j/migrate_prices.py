from typing import Dict, Sequence
from sqlalchemy.engine import Row

from src.core import db_connections

from .migrate_base import BaseMigrator


class PricesMigrator(BaseMigrator):
    """Migrate prices to Neo4j USES_NUTRIENT relationships."""

    def __init__(self):
        super().__init__("prices")

    @classmethod
    def get_description(cls) -> str:
        return "Migrate prices data to Neo4j"

    def get_migration_query(self) -> str:
        return """
            SELECT 
                p.area_code_id,
                p.item_code_id,
                p.element_code_id,
                p.flag_id,
                p.year,
                p.year_code,
                p.year,
                p.months_code,
                p.months,
                p.value,
                p.unit
            FROM prices p
            JOIN area_codes ac ON ac.id = p.area_code_id
            JOIN item_codes ic ON ic.id = p.item_code_id
            JOIN elements e ON e.id = p.element_code_id
            WHERE p.value > 0
            ORDER BY p.year, p.months, p.area_code_id, p.item_code_id, p.element_code_id, p.id
            LIMIT :limit OFFSET :offset
        """
