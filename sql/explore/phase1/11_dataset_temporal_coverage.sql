-- Temporal coverage and data volume by major dataset
WITH dataset_stats AS (
    SELECT 'production_crops_livestock' as dataset, 
           MIN(year) as min_year, 
           MAX(year) as max_year, 
           COUNT(DISTINCT year) as years_covered,
           MAX(year) - MIN(year) + 1 as year_span,
           COUNT(DISTINCT area_code_id) as countries,
           COUNT(DISTINCT item_code_id) as items,
           COUNT(DISTINCT element_code_id) as elements,
           COUNT(*) as total_records
    FROM production_crops_livestock
    
    UNION ALL
    
    SELECT 'trade_crops_livestock', 
           MIN(year), MAX(year), COUNT(DISTINCT year), MAX(year) - MIN(year) + 1,
           COUNT(DISTINCT area_code_id), COUNT(DISTINCT item_code_id), COUNT(DISTINCT element_code_id),
           COUNT(*)
    FROM trade_crops_livestock
    
    UNION ALL
    
    SELECT 'food_balance_sheets',
           MIN(year), MAX(year), COUNT(DISTINCT year), MAX(year) - MIN(year) + 1,
           COUNT(DISTINCT area_code_id), COUNT(DISTINCT item_code_id), COUNT(DISTINCT element_code_id),
           COUNT(*)
    FROM food_balance_sheets
    
    UNION ALL
    
    SELECT 'prices',
           MIN(year), MAX(year), COUNT(DISTINCT year), MAX(year) - MIN(year) + 1,
           COUNT(DISTINCT area_code_id), COUNT(DISTINCT item_code_id), COUNT(DISTINCT element_code_id),
           COUNT(*)
    FROM prices
    
    UNION ALL
    
    SELECT 'emissions_totals',
           MIN(year), MAX(year), COUNT(DISTINCT year), MAX(year) - MIN(year) + 1,
           COUNT(DISTINCT area_code_id), COUNT(DISTINCT item_code_id), COUNT(DISTINCT element_code_id),
           COUNT(*)
    FROM emissions_totals
)
SELECT 
    dataset,
    min_year,
    max_year,
    years_covered,
    ROUND(years_covered * 100.0 / year_span, 1) as coverage_percent,
    countries,
    items,
    elements,
    TO_CHAR(total_records, 'FM999,999,999') as total_records,
    TO_CHAR(ROUND(total_records::numeric / countries), 'FM999,999') as avg_records_per_country
FROM dataset_stats
ORDER BY total_records DESC;