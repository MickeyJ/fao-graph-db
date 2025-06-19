# FAO Neo4j Database Query Guide

## Understanding the Data Model

### Key Concepts
1. **Multiple Node Instances**: Each FAO dataset creates separate nodes. For example:
   - USA from `production_crops_livestock` dataset
   - USA from `inputs_fertilizers_nutrient` dataset
   - These are DIFFERENT nodes with the same `area_code`

2. **Area Code Patterns**:
   - Individual countries: 1-3 digit codes (e.g., "231" = USA)
   - Regional aggregates: Start with "5" (e.g., "5000" = World)
   - Filter individuals: `WHERE NOT c.area_code STARTS WITH '5'`

3. **Element References**: Never use IDs directly
   - ❌ `WHERE p.element_code_id = 2032483233`
   - ✅ `MATCH (e:Element {id: p.element_code_id}) WHERE e.name = "Production"`

## Basic Query Patterns

### Finding What's Available
```cypher
// What crops does a country produce?
MATCH (c:Country {name: "India"})-[p:PRODUCES]->(i:Item)
WHERE p.year = 2020
RETURN DISTINCT i.name
ORDER BY i.name
LIMIT 20;

// What years have data?
MATCH ()-[p:PRODUCES]->()
RETURN DISTINCT p.year
ORDER BY p.year DESC
LIMIT 10;

// What elements are tracked?
MATCH (e:Element)
RETURN DISTINCT e.name, e.element_code
ORDER BY e.name;
```

### Simple Production Queries
```cypher
// Top wheat producers in 2020
MATCH (c:Country)-[p:PRODUCES]->(i:Item {name: "Wheat"})
WHERE p.year = 2020 
  AND NOT c.area_code STARTS WITH '5'
MATCH (e:Element {id: p.element_code_id})
WHERE e.name = "Production"
RETURN c.name, p.value as tonnes, p.unit
ORDER BY p.value DESC
LIMIT 10;

// Country production diversity
MATCH (c:Country {name: "Brazil"})-[p:PRODUCES]->(i:Item)
WHERE p.year = 2020
MATCH (e:Element {id: p.element_code_id})
WHERE e.name = "Production"
  AND p.value > 1000  // Significant production only
RETURN i.name, p.value, p.unit
ORDER BY p.value DESC;
```

## Cross-Dataset Queries

### Joining Production and Fertilizer Data
```cypher
// Fertilizer use by major producers
MATCH (c1:Country)-[u:USES_NUTRIENT]->(n:Item)
WHERE u.year = 2020 
  AND NOT c1.area_code STARTS WITH '5'
MATCH (e1:Element {id: u.element_code_id})
WHERE e1.name = "Agricultural Use"
WITH c1.area_code as area_code, 
     c1.name as country_name, 
     SUM(u.value) as total_fertilizer
// Join to production data using area_code
MATCH (c2:Country {area_code: area_code})-[p:PRODUCES]->(:Item)
WHERE p.year = 2020
  AND c2.source_dataset = "production_crops_livestock"
MATCH (e2:Element {id: p.element_code_id})
WHERE e2.name = "Production"
WITH country_name, 
     total_fertilizer, 
     SUM(p.value) as total_production
RETURN country_name,
       ROUND(total_fertilizer) as fertilizer_tonnes,
       ROUND(total_production) as crop_tonnes,
       ROUND(total_production / total_fertilizer) as efficiency_ratio
ORDER BY total_production DESC
LIMIT 20;
```

## Time Series Analysis
```cypher
// Production trends over time
MATCH (c:Country {name: "China"})-[p:PRODUCES]->(i:Item {name: "Rice"})
WHERE p.year >= 2010
MATCH (e:Element {id: p.element_code_id})
WHERE e.name = "Production"
RETURN p.year as year, p.value as production
ORDER BY year;

// Yield improvements
WITH ["India", "China", "United States of America"] as countries
MATCH (c:Country)-[p:PRODUCES]->(i:Item {name: "Wheat"})
WHERE c.name IN countries
  AND p.year IN [2000, 2020]
MATCH (e:Element {id: p.element_code_id})
WHERE e.name = "Yield"
RETURN c.name, p.year, ROUND(p.value) as yield_kg_ha
ORDER BY c.name, p.year;
```

## Aggregation Patterns
```cypher
// Regional vs country production
MATCH (c:Country)-[p:PRODUCES]->(i:Item)
WHERE p.year = 2020
  AND i.name = "Maize (corn)"
MATCH (e:Element {id: p.element_code_id})
WHERE e.name = "Production"
WITH c.area_code STARTS WITH '5' as is_aggregate,
     CASE 
       WHEN c.area_code STARTS WITH '5' THEN 'Regional Aggregate'
       ELSE 'Individual Country'
     END as entity_type,
     c.name as name,
     p.value as production
RETURN entity_type, name, ROUND(production) as tonnes
ORDER BY is_aggregate DESC, production DESC
LIMIT 20;
```

## Performance Tips

1. **Use indexes**: Area codes and years are indexed
2. **Filter early**: Apply WHERE clauses as soon as possible
3. **Limit results**: Always use LIMIT during exploration
4. **Know your IDs**: Element IDs are reused across relationships
   - Production: Often element_code "5510"
   - Yield: Often element_code "5412"
   - Area harvested: Often element_code "5312"

## Common Gotchas

1. **Source dataset mismatch**: Always check `source_dataset` when joining
2. **Missing years**: Not all countries have data for all years
3. **Zero values**: Some entries have value = 0, filter if needed
4. **Units vary**: Always check the unit field
5. **Duplicate elements**: Same element name may have multiple IDs

## Useful Starter Queries

```cypher
// What fertilizer elements exist?
MATCH ()-[u:USES_NUTRIENT]->()
WITH DISTINCT u.element_code_id as elem_id
MATCH (e:Element {id: elem_id})
RETURN e.name, e.element_code, e.id
ORDER BY e.name;

// Countries with most complete data
MATCH (c:Country)-[p:PRODUCES]->()
WHERE p.year = 2020
  AND NOT c.area_code STARTS WITH '5'
RETURN c.name, COUNT(DISTINCT p) as data_points
ORDER BY data_points DESC
LIMIT 20;

// Find related nodes
MATCH (c:Country {area_code: "231"})
RETURN c.name, c.source_dataset
ORDER BY c.source_dataset;
```