-- Create FoodValue nodes from food_values
SELECT * FROM cypher('fao_graph', $
    CREATE (n:FoodValue {
        id: row.id,
        food_value_code: row.food_value_code,
        food_value: row.food_value,
        source_dataset: row.source_dataset,
    })   
$) AS (result agtype)
FROM food_values row;