-- Countries with most comprehensive data coverage
WITH country_stats AS (
    SELECT 
        ac.area_code,
        ac.area,
        COUNT(DISTINCT pcl.year) as years_in_production,
        COUNT(DISTINCT pcl.item_code_id) as items_in_production,
        COUNT(DISTINCT tcl.year) as years_in_trade,
        COUNT(DISTINCT fbs.year) as years_in_food_balance,
        COALESCE(COUNT(DISTINCT pcl.year), 0) + 
        COALESCE(COUNT(DISTINCT tcl.year), 0) + 
        COALESCE(COUNT(DISTINCT fbs.year), 0) as total_year_coverage
    FROM area_codes ac
    LEFT JOIN production_crops_livestock pcl ON ac.id = pcl.area_code_id
    LEFT JOIN trade_crops_livestock tcl ON ac.id = tcl.area_code_id
    LEFT JOIN food_balance_sheets fbs ON ac.id = fbs.area_code_id
    WHERE ac.area NOT LIKE '%World%' 
        AND ac.area NOT LIKE '%Africa%'
        AND ac.area NOT LIKE '%Asia%'
        AND ac.area NOT LIKE '%Europe%'
        AND ac.area NOT LIKE '%America%'
        AND ac.area NOT LIKE '%income%'
    GROUP BY ac.area_code, ac.area
)
SELECT 
    area_code,
    area as country,
    years_in_production as prod_years,
    items_in_production as prod_items,
    years_in_trade as trade_years,
    years_in_food_balance as fb_years,
    total_year_coverage as total_coverage
FROM country_stats
WHERE total_year_coverage > 0
ORDER BY total_year_coverage DESC, items_in_production DESC
LIMIT 50;