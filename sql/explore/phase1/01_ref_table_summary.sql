-- Overview of all reference tables: unique values and dataset usage
WITH reference_summary AS (
    SELECT 'area_codes' as table_name,
           COUNT(DISTINCT area_code) as unique_codes,
           COUNT(DISTINCT area) as unique_names,
           COUNT(*) as total_rows,
           COUNT(DISTINCT source_dataset) as datasets_using
    FROM area_codes
    
    UNION ALL
    
    SELECT 'item_codes',
           COUNT(DISTINCT item_code),
           COUNT(DISTINCT item),
           COUNT(*),
           COUNT(DISTINCT source_dataset)
    FROM item_codes
    
    UNION ALL
    
    SELECT 'elements',
           COUNT(DISTINCT element_code),
           COUNT(DISTINCT element),
           COUNT(*),
           COUNT(DISTINCT source_dataset)
    FROM elements
    
    UNION ALL
    
    SELECT 'flags',
           COUNT(DISTINCT flag),
           COUNT(DISTINCT description),
           COUNT(*),
           COUNT(DISTINCT source_dataset)
    FROM flags
    
    UNION ALL
    
    SELECT 'indicators',
           COUNT(DISTINCT indicator_code),
           COUNT(DISTINCT indicator),
           COUNT(*),
           COUNT(DISTINCT source_dataset)
    FROM indicators
)
SELECT 
    table_name,
    unique_codes,
    unique_names,
    total_rows,
    datasets_using,
    ROUND(total_rows::numeric / unique_codes, 1) as avg_rows_per_code
FROM reference_summary
ORDER BY total_rows DESC;