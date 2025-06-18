-- sql/phase1/06_items_by_dataset.sql (FIXED)
-- Which items appear in which datasets
WITH dataset_items AS (
    SELECT 
        source_dataset,
        item_code,
        item
    FROM item_codes
    GROUP BY source_dataset, item_code, item
)
SELECT 
    source_dataset,
    COUNT(DISTINCT item_code) as unique_items,
    COUNT(*) as total_rows,
    (SELECT STRING_AGG(DISTINCT item, ', ' ORDER BY item) 
     FROM (SELECT DISTINCT item FROM dataset_items di2 
           WHERE di2.source_dataset = di.source_dataset 
           ORDER BY item LIMIT 10) t) as sample_items
FROM dataset_items di
GROUP BY source_dataset
ORDER BY unique_items DESC;