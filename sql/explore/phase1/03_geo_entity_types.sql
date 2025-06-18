-- sql/phase1/03_geographic_entity_types.sql (FIXED STRING_AGG)
-- Types of geographic entities in the database
WITH unique_areas AS (
    SELECT DISTINCT area_code, area, area_code_m49
    FROM area_codes
),
categorized_areas AS (
    SELECT 
        area_code,
        area,
        area_code_m49,
        CASE 
            WHEN area LIKE '%World%' THEN '1. Global'
            WHEN area LIKE '%Africa%' OR area LIKE '%Asia%' OR area LIKE '%Europe%' 
                 OR area LIKE '%America%' OR area LIKE '%Oceania%' THEN '2. Regional Aggregate'
            WHEN area LIKE '%income%' OR area LIKE '%developed%' THEN '3. Economic Group'
            WHEN area LIKE '%(%)%' THEN '4. Territory/Special'
            WHEN area_code_m49 IS NULL THEN '5. Country (no M49)'
            ELSE '6. Country (with M49)'
        END as area_type
    FROM unique_areas
)
SELECT 
    area_type,
    COUNT(*) as count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 2) as percentage,
    (SELECT STRING_AGG(area, ', ' ORDER BY area) 
     FROM (SELECT area FROM categorized_areas ca2 
           WHERE ca2.area_type = ca.area_type 
           ORDER BY area LIMIT 5) t) as examples
FROM categorized_areas ca
GROUP BY area_type
ORDER BY area_type;