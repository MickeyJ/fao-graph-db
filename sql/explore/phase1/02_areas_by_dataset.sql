-- Area codes distribution across datasets
SELECT 
    source_dataset,
    COUNT(DISTINCT area_code) as unique_areas,
    COUNT(DISTINCT area) as unique_names,
    COUNT(*) as total_rows,
    STRING_AGG(DISTINCT 
        CASE 
            WHEN area LIKE '%World%' THEN 'Global'
            WHEN area LIKE '%Africa%' OR area LIKE '%Asia%' THEN 'Regional'
            WHEN area LIKE '%income%' THEN 'Economic'
            ELSE NULL
        END, ', '
    ) as special_types_included
FROM area_codes
GROUP BY source_dataset
ORDER BY unique_areas DESC;