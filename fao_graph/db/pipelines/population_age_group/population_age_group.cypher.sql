-- Create PopulationAgeGroup nodes from population_age_groups
SELECT * FROM cypher('fao_graph', $
    CREATE (n:PopulationAgeGroup {
        id: row.id,
        population_age_group_code: row.population_age_group_code,
        population_age_group: row.population_age_group,
        source_dataset: row.source_dataset,
    })   
$) AS (result agtype)
FROM population_age_groups row;