# fao_neo4j/connections.py
from contextlib import contextmanager
from typing import Generator, Any, Optional

from neo4j import GraphDatabase, Driver
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

from utils import logger
from src.core import settings


class DatabaseConnections:
    """Manage both PostgreSQL and Neo4j connections."""

    def __init__(self) -> None:
        self._pg_engine: Optional[Engine] = None
        self._neo4j_driver: Optional[Driver] = None
        self._pg_session_factory: Optional[sessionmaker] = None

    @property
    def pg_engine(self) -> Engine:
        """Lazy-load PostgreSQL engine."""
        if self._pg_engine is None:
            # Build PostgreSQL URL from settings
            pg_url = f"postgresql://{settings.db_user}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}"

            self._pg_engine = create_engine(pg_url, pool_pre_ping=True, pool_size=10)
            self._pg_session_factory = sessionmaker(bind=self._pg_engine)
            logger.info("PostgreSQL engine created")
        return self._pg_engine

    @property
    def neo4j_driver(self) -> Driver:
        """Lazy-load Neo4j driver."""
        if self._neo4j_driver is None:
            self._neo4j_driver = GraphDatabase.driver(
                settings.neo4j_uri, auth=(settings.neo4j_user, settings.neo4j_password)
            )
            logger.info("Neo4j driver created")
        return self._neo4j_driver

    @contextmanager
    def pg_session(self) -> Generator[Session, None, None]:
        """Context manager for PostgreSQL sessions."""
        # Ensure engine and factory are initialized
        _ = self.pg_engine  # This creates the factory as a side effect

        if self._pg_session_factory is None:
            raise RuntimeError("PostgreSQL session factory not initialized")

        session = self._pg_session_factory()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    @contextmanager
    def neo4j_session(self) -> Generator[Any, None, None]:
        """Context manager for Neo4j sessions."""
        session = self.neo4j_driver.session()
        try:
            yield session
        finally:
            session.close()

    def close(self) -> None:
        """Clean up connections."""
        if self._pg_engine:
            self._pg_engine.dispose()
        if self._neo4j_driver:
            self._neo4j_driver.close()


# Global connection manager
db_connections = DatabaseConnections()
