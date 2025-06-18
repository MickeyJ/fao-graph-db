-- sql/phase1/07_most_common_items.sql (FIXED)
-- Items that appear in the most datasets (likely core commodities)
WITH item_dataset_count AS (
    SELECT 
        item_code,
        MIN(item) as item, -- Since item_code should map to same item name
        COUNT(DISTINCT source_dataset) as dataset_count,
        STRING_AGG(DISTINCT source_dataset, ', ' ORDER BY source_dataset) as datasets
    FROM item_codes
    GROUP BY item_code
)
SELECT 
    item_code,
    item,
    dataset_count,
    CASE 
        WHEN LENGTH(datasets) > 100 THEN SUBSTRING(datasets, 1, 100) || '...'
        ELSE datasets
    END as appears_in_datasets
FROM item_dataset_count
WHERE dataset_count >= 5
ORDER BY dataset_count DESC, item;