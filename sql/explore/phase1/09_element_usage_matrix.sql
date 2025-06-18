-- Which elements are used in which datasets
WITH element_usage AS (
    SELECT 
        e.element,
        e.source_dataset,
        1 as used
    FROM elements e
)
SELECT 
    element,
    COUNT(DISTINCT source_dataset) as used_in_n_datasets,
    SUM(CASE WHEN source_dataset LIKE '%production%' THEN 1 ELSE 0 END) > 0 as in_production,
    SUM(CASE WHEN source_dataset LIKE '%trade%' THEN 1 ELSE 0 END) > 0 as in_trade,
    SUM(CASE WHEN source_dataset LIKE '%balance%' THEN 1 ELSE 0 END) > 0 as in_food_balance,
    SUM(CASE WHEN source_dataset LIKE '%emission%' THEN 1 ELSE 0 END) > 0 as in_emissions,
    SUM(CASE WHEN source_dataset LIKE '%price%' THEN 1 ELSE 0 END) > 0 as in_prices
FROM element_usage
GROUP BY element
HAVING COUNT(DISTINCT source_dataset) >= 3
ORDER BY used_in_n_datasets DESC, element;