-- Compare production trends across regions over time
WITH regional_production AS (
  SELECT 
    ac.area as region,
    ic.item,
    pcl.year,
    pcl.value as total_production
  FROM production_crops_livestock pcl
  JOIN area_codes ac ON ac.id = pcl.area_code_id
  JOIN item_codes ic ON ic.id = pcl.item_code_id
  JOIN elements ec ON ec.id = pcl.element_code_id
  LEFT JOIN flags f ON f.id = pcl.flag_id
  WHERE 
    -- Use FAO's continental aggregates
    ac.area_code IN ('5100', '5200', '5300', '5400', '5500')  -- Africa, Americas, Asia, Europe, Oceania
    AND (LOWER(ic.item) LIKE '%wheat%' 
    OR LOWER(ic.item) LIKE '%rice%' 
    OR LOWER(ic.item) LIKE '%maize%'
    OR LOWER(ic.item) LIKE '%corn%'
    OR LOWER(ic.item) LIKE '%barley%'
    OR LOWER(ic.item) LIKE '%sorghum%')
    AND LOWER(ec.element) LIKE '%production%'
    AND pcl.year BETWEEN 2010 AND 2023
    AND pcl.value IS NOT NULL
    AND f.flag IN ('A', 'X', 'E')
),
production_with_lag AS (
  SELECT 
    region,
    item,
    year,
    total_production,
    LAG(total_production) OVER (PARTITION BY region, item ORDER BY year) as prev_year_production
  FROM regional_production
)
SELECT 
  region,
  item,
  year,
  total_production,
  prev_year_production,
  ROUND(((total_production - prev_year_production) / 
        NULLIF(prev_year_production, 0) * 100)::numeric, 2) as yoy_change_percent
FROM production_with_lag
WHERE prev_year_production IS NOT NULL
ORDER BY region, item, year;