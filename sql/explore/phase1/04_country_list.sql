-- sql/phase1/04_country_list_clean.sql
-- Clean list of actual countries (excluding aggregates)
WITH country_datasets AS (
    SELECT 
        area_code,
        area,
        area_code_m49,
        COUNT(DISTINCT source_dataset) as dataset_count
    FROM area_codes
    WHERE area NOT LIKE '%World%'
        AND area NOT LIKE '%Africa%' 
        AND area NOT LIKE '%Asia%'
        AND area NOT LIKE '%Europe%'
        AND area NOT LIKE '%America%'
        AND area NOT LIKE '%Oceania%'
        AND area NOT LIKE '%income%'
        AND area NOT LIKE '%developed%'
        AND area NOT LIKE '%transition%'
        AND area NOT LIKE '%(excluding intra-trade)%'
        AND area NOT LIKE '%FAO%'
        AND area NOT LIKE '%OECD%'
    GROUP BY area_code, area, area_code_m49
)
SELECT 
    area_code,
    area as country_name,
    area_code_m49,
    dataset_count as appears_in_n_datasets
FROM country_datasets
ORDER BY country_name;