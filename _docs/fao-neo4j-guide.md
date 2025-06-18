# FAO to Neo4j Knowledge Graph Transformation Guide

## Executive Summary

The FAO database structure naturally maps to a graph model where:
- **Reference tables** (area_codes, item_codes, elements) become **NODES**
- **Dataset tables** (production, trade, emissions) become **RELATIONSHIPS**
- **Time and quality** become connected dimensions rather than just properties

This transformation unlocks powerful graph analytics, pattern discovery, and intuitive querying of the complex relationships within global food and agriculture data.

## Table of Contents

1. [Conceptual Mapping](#conceptual-mapping)
2. [Graph Model Design](#graph-model-design)
3. [Implementation Strategy](#implementation-strategy)
4. [Migration Architecture](#migration-architecture)
5. [Code Examples](#code-examples)
6. [Query Patterns](#query-patterns)
7. [Advanced Analytics](#advanced-analytics)
8. [Performance Optimization](#performance-optimization)
9. [Best Practices](#best-practices)

---

## Conceptual Mapping

### The Insight: Reference Tables = Nodes, Dataset Tables = Relationships

```
Traditional Relational View:
┌─────────────────┐     ┌───────────────────────────┐     ┌─────────────────┐
│  area_codes     │────→│ production_crops_livestock │←────│  item_codes     │
│ (lookup table)  │     │     (fact table)          │     │ (lookup table)  │
└─────────────────┘     └───────────────────────────┘     └─────────────────┘

Graph View:
    (:Country)──────[:PRODUCED {value, year}]──────→(:Item)
```

### Mapping Rules

1. **Entity Tables → Node Labels**
   - area_codes → :Country nodes
   - item_codes → :Item nodes  
   - elements → :MeasurementType nodes
   - donors → :Donor nodes
   - currencies → :Currency nodes

2. **Fact Tables → Relationships**
   - production_crops_livestock → PRODUCED
   - trade_detailed_trade_matrix → EXPORTED_TO / IMPORTED_FROM
   - prices → HAS_PRICE
   - emissions_* → EMITTED

3. **Temporal Data → Connected Time Nodes**
   - Year columns → :Year nodes
   - Enables time-series traversals

4. **Data Quality → Relationship Properties or Nodes**
   - Flag → property or :DataQuality node
   - Enables filtering by reliability

---

## Graph Model Design

### Core Node Types

```cypher
// Geographic Entities
(:Country {
  area_code: String,      // Primary key from SQL
  name: String,
  m49_code: String,
  type: String,           // 'Country' or 'Aggregate'
  region: String,
  subregion: String
})

// Commodity Entities  
(:Item {
  item_code: String,      // Primary key from SQL
  name: String,
  cpc_code: String,
  category: String,
  is_aggregate: Boolean
})

// Measurement Types
(:Element {
  element_code: String,
  name: String,
  unit: String
})

// Temporal Nodes
(:Year {
  year: Integer,
  decade: Integer,
  period: String          // 'pre-2000', '2000s', '2010s', '2020s'
})

// Data Quality
(:Flag {
  code: String,
  description: String,
  reliability_score: Float
})
```

### Relationship Types

```cypher
// Production Relationships
(:Country)-[:PRODUCES {
  value: Float,
  unit: String,
  year: Integer,
  flag: String,
  element: String         // 'Production', 'Yield', 'Area Harvested'
}]->(:Item)

// Trade Relationships
(:Country)-[:TRADES_WITH {
  item_code: String,
  value: Float,
  unit: String,
  year: Integer,
  direction: String       // 'export' or 'import'
}]->(:Country)

// Price Relationships
(:Country)-[:PRICES {
  value: Float,
  currency: String,
  year: Integer,
  month: String
}]->(:Item)

// Emission Relationships
(:Country)-[:EMITS {
  gas_type: String,       // 'CO2', 'CH4', 'N2O'
  source: String,
  value: Float,
  unit: String,
  year: Integer
}]->(:EmissionSource)

// Temporal Connections
(:Production)-[:IN_YEAR]->(:Year)
(:Trade)-[:IN_YEAR]->(:Year)
```

---

## Implementation Strategy

### Phase 1: Hybrid SQL → Neo4j Migration

```python
class FAOGraphMigrator:
    """Orchestrates the migration from PostgreSQL to Neo4j"""
    
    def __init__(self, sql_engine, neo4j_driver):
        self.sql = sql_engine
        self.neo4j = neo4j_driver
        self.batch_size = 10000
        
    def migrate(self):
        """Full migration pipeline"""
        # 1. Create constraints and indexes
        self.create_graph_schema()
        
        # 2. Load reference data as nodes
        self.load_reference_nodes()
        
        # 3. Create temporal framework
        self.create_temporal_nodes()
        
        # 4. Load relationships from fact tables
        self.load_fact_relationships()
        
        # 5. Create derived relationships
        self.create_derived_insights()
        
        # 6. Validate migration
        self.validate_migration()
```

### Phase 2: Schema Creation

```cypher
// Constraints ensure data integrity
CREATE CONSTRAINT country_unique IF NOT EXISTS
FOR (c:Country) REQUIRE c.area_code IS UNIQUE;

CREATE CONSTRAINT item_unique IF NOT EXISTS
FOR (i:Item) REQUIRE i.item_code IS UNIQUE;

CREATE CONSTRAINT year_unique IF NOT EXISTS
FOR (y:Year) REQUIRE y.year IS UNIQUE;

// Indexes for performance
CREATE INDEX country_name IF NOT EXISTS FOR (c:Country) ON (c.name);
CREATE INDEX item_name IF NOT EXISTS FOR (i:Item) ON (i.name);
CREATE INDEX country_type IF NOT EXISTS FOR (c:Country) ON (c.type);

// Composite indexes for relationships
CREATE INDEX rel_produces_year IF NOT EXISTS FOR ()-[r:PRODUCES]-() ON (r.year);
CREATE INDEX rel_trades_year_item IF NOT EXISTS FOR ()-[r:TRADES_WITH]-() ON (r.year, r.item_code);
```

---

## Migration Architecture

### 1. Reference Data → Nodes

```python
def load_country_nodes(self):
    """Load countries with enriched metadata"""
    
    query = """
    SELECT 
        ac.area_code,
        ac.area as name,
        ac.area_code_m49,
        -- Derive type from code pattern
        CASE 
            WHEN ac.area_code ~ '^5[0-9]{3}' THEN 'Aggregate'
            WHEN ac.area_code ~ '^[0-9]{1,3}$' THEN 'Country'
            ELSE 'Special'
        END as node_type,
        -- Get data availability metrics
        COUNT(DISTINCT pcl.item_code_id) as items_produced,
        COUNT(DISTINCT pcl.year) as years_of_data,
        MIN(pcl.year) as earliest_data,
        MAX(pcl.year) as latest_data,
        -- Get trade relationships count
        COUNT(DISTINCT dtm.partner_country_code) as trade_partners
    FROM area_codes ac
    LEFT JOIN production_crops_livestock pcl ON pcl.area_code_id = ac.id
    LEFT JOIN trade_detailed_trade_matrix dtm ON dtm.reporter_country_code = ac.area_code
    GROUP BY ac.area_code, ac.area, ac.area_code_m49
    """
    
    with self.neo4j.session() as session:
        session.execute_write(self._create_country_nodes_tx, query)
        
def _create_country_nodes_tx(self, tx, sql_query):
    """Transaction function to create country nodes"""
    
    # Fetch from SQL
    sql_data = self.fetch_sql_data(sql_query)
    
    # Create in Neo4j
    cypher = """
    UNWIND $countries as country
    MERGE (c:Country {area_code: country.area_code})
    SET c.name = country.name,
        c.m49_code = country.area_code_m49,
        c.type = country.node_type,
        c.items_produced_count = country.items_produced,
        c.data_years_available = country.years_of_data,
        c.earliest_data_year = country.earliest_data,
        c.latest_data_year = country.latest_data,
        c.trade_partner_count = country.trade_partners
    """
    
    tx.run(cypher, countries=sql_data)
```

### 2. Production Data → Relationships

```python
def load_production_relationships(self):
    """Create PRODUCES relationships with temporal connections"""
    
    # SQL: Aggregate by country-item-year for cleaner graph
    query = """
    WITH production_clean AS (
        SELECT 
            ac.area_code,
            ic.item_code,
            pcl.year,
            e.element,
            SUM(pcl.value) as total_value,
            STRING_AGG(DISTINCT pcl.unit, ', ') as units,
            STRING_AGG(DISTINCT f.flag, '') as flags,
            COUNT(*) as data_points,
            AVG(pcl.value) as avg_value
        FROM production_crops_livestock pcl
        JOIN area_codes ac ON ac.id = pcl.area_code_id
        JOIN item_codes ic ON ic.id = pcl.item_code_id
        JOIN elements e ON e.id = pcl.element_code_id
        JOIN flags f ON f.id = pcl.flag_id
        WHERE pcl.value > 0 
          AND pcl.value != 'NaN'::float
          AND f.flag IN ('A', 'X', 'E')  -- Quality filter
        GROUP BY ac.area_code, ic.item_code, pcl.year, e.element
    )
    SELECT * FROM production_clean
    ORDER BY year, area_code  -- For efficient batching
    """
    
    # Stream data in batches
    self._stream_relationships(query, self._create_production_relationships_tx)
    
def _create_production_relationships_tx(self, tx, batch):
    """Create production relationships with proper connections"""
    
    cypher = """
    UNWIND $productions as prod
    MATCH (c:Country {area_code: prod.area_code})
    MATCH (i:Item {item_code: prod.item_code})
    MATCH (y:Year {year: prod.year})
    
    // Create production node (allows multiple elements per country-item-year)
    CREATE (p:Production {
        element: prod.element,
        value: prod.total_value,
        unit: prod.units,
        flags: prod.flags,
        data_points: prod.data_points
    })
    
    // Connect all relationships
    CREATE (c)-[:PRODUCED]->(p)
    CREATE (p)-[:OF_ITEM]->(i)
    CREATE (p)-[:IN_YEAR]->(y)
    
    // Also create direct relationship for simple queries
    MERGE (c)-[r:PRODUCES {year: prod.year, element: prod.element}]->(i)
    SET r.value = prod.total_value,
        r.unit = prod.units,
        r.flags = prod.flags
    """
    
    tx.run(cypher, productions=batch)
```

### 3. Trade Matrix → Complex Relationships

```python
def load_trade_relationships(self):
    """Create trade flow network"""
    
    query = """
    SELECT 
        dtm.reporter_country_code,
        dtm.partner_country_code,
        ic.item_code,
        ic.item as item_name,
        e.element,  -- 'Export Quantity' or 'Import Quantity'
        dtm.year,
        SUM(dtm.value) as total_value,
        STRING_AGG(DISTINCT dtm.unit, ', ') as units
    FROM trade_detailed_trade_matrix dtm
    JOIN item_codes ic ON ic.id = dtm.item_code_id
    JOIN elements e ON e.id = dtm.element_code_id
    WHERE dtm.value > 0
      AND dtm.year >= 2010  -- Recent data for performance
    GROUP BY dtm.reporter_country_code, dtm.partner_country_code, 
             ic.item_code, ic.item, e.element, dtm.year
    """
    
    cypher = """
    UNWIND $trades as trade
    MATCH (reporter:Country {area_code: trade.reporter_country_code})
    MATCH (partner:Country {area_code: trade.partner_country_code})
    MATCH (item:Item {item_code: trade.item_code})
    MATCH (year:Year {year: trade.year})
    
    // Create trade relationship with all context
    CREATE (reporter)-[t:TRADES_WITH {
        item_code: trade.item_code,
        item_name: trade.item_name,
        year: trade.year,
        value: trade.total_value,
        unit: trade.units,
        direction: CASE 
            WHEN trade.element CONTAINS 'Export' THEN 'export'
            ELSE 'import'
        END
    }]->(partner)
    """
```

---

## Code Examples

### Complete Migration Script

```python
# migrate_fao_to_neo4j.py
import asyncio
from neo4j import AsyncGraphDatabase
from sqlalchemy import create_engine
import logging

class FAOToNeo4j:
    def __init__(self, sql_url, neo4j_url, neo4j_auth):
        self.sql_engine = create_engine(sql_url)
        self.neo4j_driver = AsyncGraphDatabase.driver(neo4j_url, auth=neo4j_auth)
        self.logger = logging.getLogger(__name__)
        
    async def migrate(self):
        """Full migration pipeline"""
        try:
            # 1. Setup
            await self.create_constraints_and_indexes()
            
            # 2. Load reference data
            await self.load_countries()
            await self.load_items()
            await self.load_temporal_framework()
            
            # 3. Load relationships
            tasks = [
                self.load_production_data(),
                self.load_trade_data(),
                self.load_price_data(),
                self.load_emissions_data()
            ]
            await asyncio.gather(*tasks)
            
            # 4. Create derived insights
            await self.create_supply_chains()
            await self.create_market_clusters()
            
            # 5. Validate
            await self.validate_migration()
            
        finally:
            await self.neo4j_driver.close()
    
    async def create_constraints_and_indexes(self):
        """Set up graph schema"""
        constraints = [
            "CREATE CONSTRAINT country_unique IF NOT EXISTS FOR (c:Country) REQUIRE c.area_code IS UNIQUE",
            "CREATE CONSTRAINT item_unique IF NOT EXISTS FOR (i:Item) REQUIRE i.item_code IS UNIQUE",
            "CREATE CONSTRAINT year_unique IF NOT EXISTS FOR (y:Year) REQUIRE y.year IS UNIQUE"
        ]
        
        indexes = [
            "CREATE INDEX country_name IF NOT EXISTS FOR (c:Country) ON (c.name)",
            "CREATE INDEX item_category IF NOT EXISTS FOR (i:Item) ON (i.category)",
            "CREATE INDEX rel_produces_year IF NOT EXISTS FOR ()-[r:PRODUCES]-() ON (r.year)"
        ]
        
        async with self.neo4j_driver.session() as session:
            for constraint in constraints:
                await session.run(constraint)
            for index in indexes:
                await session.run(index)
```

### Smart Relationship Discovery

```python
def discover_correlations(self):
    """Find hidden relationships using SQL analysis"""
    
    # Find items that are frequently produced together
    co_production_query = """
    WITH country_items AS (
        SELECT 
            pcl1.area_code_id,
            pcl1.item_code_id as item1_id,
            pcl2.item_code_id as item2_id,
            COUNT(DISTINCT pcl1.year) as years_together,
            CORR(pcl1.value, pcl2.value) as correlation
        FROM production_crops_livestock pcl1
        JOIN production_crops_livestock pcl2 
            ON pcl1.area_code_id = pcl2.area_code_id 
            AND pcl1.year = pcl2.year
            AND pcl1.element_code_id = pcl2.element_code_id
            AND pcl1.item_code_id < pcl2.item_code_id  -- Avoid duplicates
        WHERE pcl1.value > 0 AND pcl2.value > 0
        GROUP BY pcl1.area_code_id, pcl1.item_code_id, pcl2.item_code_id
        HAVING COUNT(DISTINCT pcl1.year) >= 10  -- At least 10 years of data
            AND ABS(CORR(pcl1.value, pcl2.value)) > 0.7  -- Strong correlation
    )
    SELECT 
        ac.area_code,
        ic1.item_code as item1_code,
        ic1.item as item1_name,
        ic2.item_code as item2_code,
        ic2.item as item2_name,
        ci.years_together,
        ci.correlation
    FROM country_items ci
    JOIN area_codes ac ON ac.id = ci.area_code_id
    JOIN item_codes ic1 ON ic1.id = ci.item1_id
    JOIN item_codes ic2 ON ic2.id = ci.item2_id
    ORDER BY ci.correlation DESC
    """
    
    # Create CO_PRODUCED relationships
    cypher = """
    UNWIND $correlations as corr
    MATCH (c:Country {area_code: corr.area_code})
    MATCH (i1:Item {item_code: corr.item1_code})
    MATCH (i2:Item {item_code: corr.item2_code})
    
    MERGE (i1)-[r:CO_PRODUCED {country: c.area_code}]->(i2)
    SET r.correlation = corr.correlation,
        r.years_observed = corr.years_together,
        r.country_name = c.name
    """
```

---

## Query Patterns

### Basic Traversals

```cypher
// What does the USA produce?
MATCH (c:Country {name: "United States"})-[:PRODUCES]->(i:Item)
RETURN i.name, SUM(r.value) as total_production
ORDER BY total_production DESC

// Who trades wheat with whom?
MATCH (c1:Country)-[t:TRADES_WITH {item_name: "Wheat"}]->(c2:Country)
WHERE t.year = 2023
RETURN c1.name as exporter, c2.name as importer, t.value
ORDER BY t.value DESC
LIMIT 20
```

### Temporal Analysis

```cypher
// Production trends over time
MATCH (c:Country {name: "India"})-[p:PRODUCES]->(i:Item {name: "Rice"})
WITH p.year as year, p.value as production
ORDER BY year
WITH collect({year: year, value: production}) as timeseries
RETURN timeseries

// Year-over-year growth
MATCH (c:Country)-[p1:PRODUCES {year: 2022}]->(i:Item)
MATCH (c)-[p2:PRODUCES {year: 2023}]->(i)
WITH c, i, (p2.value - p1.value) / p1.value * 100 as growth_rate
WHERE abs(growth_rate) > 10
RETURN c.name, i.name, growth_rate
ORDER BY growth_rate DESC
```

### Network Analysis

```cypher
// Find supply chain dependencies
MATCH path = (c1:Country)-[:TRADES_WITH*1..3]->(c2:Country)
WHERE c1.name = "China" 
  AND ALL(r IN relationships(path) WHERE r.year = 2023)
RETURN path

// Market communities (requires GDS)
CALL gds.louvain.stream('trade-network-2023')
YIELD nodeId, communityId
MATCH (c:Country) WHERE id(c) = nodeId
RETURN communityId, collect(c.name) as countries
ORDER BY size(countries) DESC
```

### Complex Analytics

```cypher
// Food security risk assessment
MATCH (c:Country)
// Get production diversity
OPTIONAL MATCH (c)-[:PRODUCES {year: 2023}]->(item:Item)
WITH c, COUNT(DISTINCT item) as production_diversity
// Get import dependency
OPTIONAL MATCH (c)-[imports:TRADES_WITH {direction: 'import', year: 2023}]-()
WITH c, production_diversity, SUM(imports.value) as total_imports
// Get climate impact
OPTIONAL MATCH (c)-[e:EMITS {year: 2023}]-()
WITH c, production_diversity, total_imports, SUM(e.value) as emissions
// Calculate risk score
RETURN c.name,
       production_diversity,
       total_imports,
       emissions,
       CASE 
         WHEN production_diversity < 10 THEN 'HIGH'
         WHEN production_diversity < 20 THEN 'MEDIUM'
         ELSE 'LOW'
       END as diversity_risk
ORDER BY production_diversity ASC
```

---

## Advanced Analytics

### Graph Data Science Integration

```cypher
// Create supply chain graph projection
CALL gds.graph.project(
  'supply-chain-2023',
  {
    Country: {
      properties: ['items_produced_count', 'trade_partner_count']
    }
  },
  {
    TRADES_WITH: {
      properties: ['value'],
      orientation: 'UNDIRECTED'
    }
  }
)

// Find most critical countries in supply chain
CALL gds.betweenness.stream('supply-chain-2023')
YIELD nodeId, score
MATCH (c:Country) WHERE id(c) = nodeId
RETURN c.name, score as criticality
ORDER BY criticality DESC
LIMIT 10

// Predict future trade relationships
CALL gds.beta.linkPrediction.predict.stream(
  'supply-chain-2023',
  {
    modelName: 'trade-prediction-model',
    threshold: 0.7
  }
)
YIELD node1, node2, probability
MATCH (c1:Country), (c2:Country)
WHERE id(c1) = node1 AND id(c2) = node2
RETURN c1.name, c2.name, probability
ORDER BY probability DESC
```

### Custom Algorithms

```python
# Python driver for complex calculations
def calculate_food_system_resilience(driver, country_code):
    """Calculate multi-factor resilience score"""
    
    with driver.session() as session:
        result = session.run("""
        MATCH (c:Country {area_code: $country_code})
        
        // Factor 1: Production diversity
        OPTIONAL MATCH (c)-[:PRODUCES {year: 2023}]->(item:Item)
        WITH c, COUNT(DISTINCT item) as prod_diversity, COLLECT(DISTINCT item.category) as categories
        
        // Factor 2: Trade balance
        OPTIONAL MATCH (c)-[exp:TRADES_WITH {direction: 'export', year: 2023}]-()
        WITH c, prod_diversity, categories, SUM(exp.value) as exports
        OPTIONAL MATCH (c)-[imp:TRADES_WITH {direction: 'import', year: 2023}]-()
        WITH c, prod_diversity, categories, exports, SUM(imp.value) as imports
        
        // Factor 3: Supply chain connectivity
        OPTIONAL MATCH (c)-[:TRADES_WITH {year: 2023}]-(partner:Country)
        WITH c, prod_diversity, categories, exports, imports, COUNT(DISTINCT partner) as partners
        
        // Factor 4: Climate vulnerability
        OPTIONAL MATCH (c)-[em:EMITS {year: 2023}]-()
        
        RETURN c.name as country,
               prod_diversity,
               size(categories) as category_diversity,
               exports,
               imports,
               partners,
               SUM(em.value) as emissions,
               // Composite score
               (prod_diversity * 0.3 + 
                partners * 0.2 + 
                CASE WHEN imports > 0 THEN exports/imports ELSE 1 END * 0.3 +
                (1.0 / (1.0 + COALESCE(SUM(em.value), 0)/1000000)) * 0.2
               ) as resilience_score
        """, country_code=country_code)
        
        return result.single()
```

---

## Performance Optimization

### 1. Indexing Strategy

```cypher
// Frequently queried relationship properties
CREATE INDEX prod_year_value IF NOT EXISTS 
FOR ()-[r:PRODUCES]-() ON (r.year, r.value);

CREATE INDEX trade_year_item_value IF NOT EXISTS
FOR ()-[r:TRADES_WITH]-() ON (r.year, r.item_code, r.value);

// Full-text search on names
CREATE FULLTEXT INDEX country_names IF NOT EXISTS
FOR (c:Country) ON EACH [c.name];

CREATE FULLTEXT INDEX item_names IF NOT EXISTS  
FOR (i:Item) ON EACH [i.name];
```

### 2. Query Optimization

```cypher
// Bad: Cartesian product
MATCH (c:Country), (i:Item)
WHERE c.name = 'Brazil' AND i.name = 'Coffee'

// Good: Direct traversal
MATCH (c:Country {name: 'Brazil'})-[:PRODUCES]->(i:Item {name: 'Coffee'})

// Bad: Late filtering
MATCH (c:Country)-[r:PRODUCES]->(i:Item)
WHERE c.name = 'India' AND r.year = 2023

// Good: Index usage
MATCH (c:Country {name: 'India'})-[r:PRODUCES {year: 2023}]->(i:Item)
```

### 3. Batching Strategies

```python
def batch_create_relationships(self, data, batch_size=10000):
    """Efficiently create relationships in batches"""
    
    async with self.neo4j_driver.session() as session:
        for i in range(0, len(data), batch_size):
            batch = data[i:i + batch_size]
            
            await session.execute_write(
                lambda tx: tx.run(
                    """
                    UNWIND $batch as row
                    MATCH (c:Country {area_code: row.area_code})
                    MATCH (i:Item {item_code: row.item_code})
                    MERGE (c)-[r:PRODUCES {year: row.year}]->(i)
                    SET r.value = row.value,
                        r.unit = row.unit
                    """,
                    batch=batch
                )
            )
            
            if i % 100000 == 0:
                self.logger.info(f"Processed {i:,} relationships")
```

---

## Best Practices

### 1. Data Modeling
- **Use specific relationship types** rather than generic ones with properties
- **Create Year nodes** for efficient temporal queries
- **Denormalize for performance** where it makes sense
- **Use node labels** to enable index usage

### 2. Migration Process
- **Validate data quality** in SQL before migration
- **Create constraints first** to ensure data integrity
- **Batch operations** to manage memory usage
- **Run in parallel** where relationships are independent
- **Validate continuously** during migration

### 3. Query Patterns
- **Start specific** with node property matches
- **Use parameters** in queries to enable plan caching
- **Profile queries** to understand execution
- **Avoid unbounded traversals** without limits

### 4. Maintenance
- **Regular statistics updates**: `CALL db.stats.refresh()`
- **Monitor query logs** for slow queries
- **Periodic relationship aggregation** for performance
- **Archive old data** to separate graphs if needed

### 5. Development Workflow
```bash
# 1. Test with small dataset first
cypher-shell "MATCH (n) RETURN count(n) LIMIT 10"

# 2. Profile before optimization  
PROFILE MATCH (c:Country)-[:PRODUCES*1..3]-(connected)
RETURN count(connected)

# 3. Use EXPLAIN to verify index usage
EXPLAIN MATCH (c:Country {area_code: '840'})-[:PRODUCES {year: 2023}]->(i)
RETURN c, i

# 4. Monitor during bulk operations
CALL dbms.listQueries() YIELD query, elapsedTimeMillis
WHERE elapsedTimeMillis > 1000
RETURN query, elapsedTimeMillis
```

---

## Next Steps

1. **Set up Neo4j environment**
   - Neo4j Enterprise (or Community for testing)
   - Install APOC and GDS plugins
   - Configure memory settings for your data size

2. **Run proof of concept**
   - Start with one dataset (e.g., production_crops_livestock)
   - Validate the model works for your queries
   - Measure performance improvements

3. **Implement migration pipeline**
   - Use the code templates provided
   - Start with reference data
   - Add fact tables incrementally

4. **Explore and iterate**
   - Use Neo4j Browser/Bloom for visualization
   - Discover unexpected patterns
   - Refine the model based on findings

5. **Build applications**
   - Create APIs using Neo4j drivers
   - Build dashboards with graph visualizations
   - Implement real-time analytics

The FAO data's inherent graph structure makes this transformation natural and powerful. The combination of structured migration from SQL with Neo4j's flexibility gives you the best of both worlds: data quality and exploratory power.
