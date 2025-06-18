
-- High-level database summary
WITH db_stats AS (
    SELECT 
        (SELECT COUNT(DISTINCT area_code) FROM area_codes) as total_areas,
        (SELECT COUNT(DISTINCT area_code) FROM area_codes 
         WHERE area NOT LIKE '%World%' AND area NOT LIKE '%Africa%' 
         AND area NOT LIKE '%Asia%' AND area NOT LIKE '%Europe%' 
         AND area NOT LIKE '%America%') as total_countries,
        (SELECT COUNT(DISTINCT item_code) FROM item_codes) as total_items,
        (SELECT COUNT(DISTINCT element_code) FROM elements) as total_elements,
        (SELECT COUNT(DISTINCT source_dataset) FROM area_codes) as total_datasets,
        (SELECT MIN(year) FROM production_crops_livestock) as earliest_year,
        (SELECT MAX(year) FROM production_crops_livestock) as latest_year,
        (SELECT COUNT(*) FROM production_crops_livestock) as production_records,
        (SELECT COUNT(*) FROM trade_crops_livestock) as trade_records,
        (SELECT COUNT(*) FROM food_balance_sheets) as food_balance_records
)
SELECT 
    'Total Geographic Areas' as metric,
    total_areas::text as value
FROM db_stats
UNION ALL
SELECT 'Total Countries (excl. aggregates)', total_countries::text FROM db_stats
UNION ALL
SELECT 'Total Items/Commodities', total_items::text FROM db_stats
UNION ALL
SELECT 'Total Measurement Types', total_elements::text FROM db_stats
UNION ALL
SELECT 'Total Source Datasets', total_datasets::text FROM db_stats
UNION ALL
SELECT 'Earliest Year', earliest_year::text FROM db_stats
UNION ALL
SELECT 'Latest Year', latest_year::text FROM db_stats
UNION ALL
SELECT 'Production Records', TO_CHAR(production_records, 'FM999,999,999') FROM db_stats
UNION ALL
SELECT 'Trade Records', TO_CHAR(trade_records, 'FM999,999,999') FROM db_stats
UNION ALL
SELECT 'Food Balance Records', TO_CHAR(food_balance_records, 'FM999,999,999') FROM db_stats;