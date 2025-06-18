-- Track data availability trends over time
WITH yearly_stats AS (
    SELECT 
        year,
        COUNT(DISTINCT area_code_id) as countries_reporting,
        COUNT(DISTINCT item_code_id) as items_reported,
        COUNT(DISTINCT element_code_id) as elements_used,
        COUNT(*) as total_records
    FROM production_crops_livestock
    WHERE year >= 1990
    GROUP BY year
)
SELECT 
    year,
    countries_reporting,
    items_reported,
    elements_used,
    TO_CHAR(total_records, 'FM999,999,999') as total_records,
    ROUND(total_records::numeric / countries_reporting, 0) as avg_records_per_country,
    ROUND((countries_reporting - LAG(countries_reporting) OVER (ORDER BY year))::numeric / 
          LAG(countries_reporting) OVER (ORDER BY year) * 100, 1) as country_change_pct
FROM yearly_stats
ORDER BY year DESC;