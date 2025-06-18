from sqlalchemy import text
from src.core import db_connections

# Test PostgreSQL
with db_connections.pg_session() as session:
    result = session.execute(text("SELECT COUNT(*) FROM area_codes"))
    print(f"PostgreSQL connected! Area codes: {result.scalar()}")

# Test Neo4j
with db_connections.neo4j_session() as session:
    result = session.run("RETURN 'Connected!' as message")
    print(f"Neo4j: {result.single()['message']}")

# Cleanup
db_connections.close()
