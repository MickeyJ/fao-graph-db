# src/exploration/base.py
from abc import ABC, abstractmethod
from typing import Any, Dict, List
from sqlalchemy import text
from tabulate import tabulate
from utils.logger import logger
from db.database import run_with_session


class DatasetExplorer(ABC):
    """Base class defining required exploration queries for each table"""

    base_query_names = [
        "coverage",
        "quality",
        "patterns",
        "elements",
    ]

    @property
    @abstractmethod
    def coverage(self) -> dict[str, str]:
        """What's in this table? Basic statistics and coverage"""
        pass

    @property
    @abstractmethod
    def quality(self) -> dict[str, str]:
        """Data quality assessment - flags, completeness, etc."""
        pass

    @property
    @abstractmethod
    def patterns(self) -> dict[str, str]:
        """Key patterns or insights specific to this table"""
        pass

    @property
    @abstractmethod
    def dimensions(self) -> dict[str, str]:
        """Shows the key dimensions that break down the data"""
        pass

    def _print_results_header(self, query_name: str, description: str) -> None:
        """Prints a formatted header for query results"""
        header_text = f"{self.__class__.__name__}.{query_name}"
        print(header_text)
        total_width = len(description) * 2
        padding = (total_width - len(description)) // 2

        print(f"{'='*total_width}")
        print(f"{' '*padding}{description}")
        print(f"{'='*total_width}")

    def _print_results(self, query_name: str, description: str, results: List[Any], max_col_width: int = 30) -> None:
        """Format query results with truncation"""

        self._print_results_header(query_name, description)

        if not results:
            print("No results")
            return

        def truncate(text: str, max_width: int) -> str:
            """Truncate text with ellipsis if too long"""
            text = str(text)
            if len(text) <= max_width:
                return text
            return text[: max_width - 4] + " ..."

        # If it's Row objects, convert to dicts
        if hasattr(results[0], "_fields"):
            columns = results[0]._fields
            data = []
            for row in results:
                # Truncate values as we convert
                truncated_row = {col: truncate(val, max_col_width) for col, val in zip(columns, row)}
                data.append(truncated_row)

            print(tabulate(data, headers="keys", tablefmt="fancy_grid"))
        else:
            # Already dicts - truncate values
            data = []
            for row in results:
                truncated_row = {k: truncate(v, max_col_width) for k, v in row.items()}
                data.append(truncated_row)

            print(tabulate(data, headers="keys", tablefmt="fancy_grid"))

    def execute(self, query_name: str | None = None) -> List[Any] | Dict[str, List[Any]]:
        """Run a query against the database"""
        if query_name:
            # Get the query property
            query = getattr(self, query_name, None)
            if not query:
                raise ValueError(f"Query '{query_name}' not defined in {self.__class__.__name__}")

            query_text = query.get("query")
            query_description = query.get("description")
            try:
                logger.info(f"Running query: {self.__class__.__name__}.{query_name}")
                result = run_with_session(lambda db: db.execute(text(query_text)).fetchall())
                logger.info(f"Query returned {len(result) if result else 0} rows")
                self._print_results(query_name, query_description, result)
                return result if result else []
            except Exception as e:
                logger.error(f"Error running query {self.__class__.__name__}.{query_name}: {e}")
                raise
        else:
            # Run all standard queries
            logger.info(f"Running all {self.__class__.__name__} queries")
            results: Dict[str, List[Any]] = {}

            for name in self.base_query_names:
                query = getattr(self, name, None)
                if not query:
                    raise ValueError(f"Query '{query_name}' not defined in {self.__class__.__name__}")

                query_text = query.get("query")
                query_description = query.get("description")
                try:
                    logger.info(f"Running query: {self.__class__.__name__}.{name}")
                    result = run_with_session(lambda db: db.execute(text(query_text)).fetchall())  # type: ignore
                    logger.info(f"Query {name} returned {len(result) if result else 0} rows")
                    results[name] = result if result else []
                    self._print_results(name, query_description, result)
                except Exception as e:
                    logger.error(f"Error running query {self.__class__.__name__}.{name}: {e}")
                    raise

            return results
