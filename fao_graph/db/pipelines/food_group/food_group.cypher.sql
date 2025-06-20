-- Create FoodGroup nodes from food_groups
SELECT * FROM cypher('fao_graph', $
    CREATE (n:FoodGroup {
        id: row.id,
        food_group_code: row.food_group_code,
        food_group: row.food_group,
        source_dataset: row.source_dataset,
    })   
$) AS (result agtype)
FROM food_groups row;