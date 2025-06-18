-- Data completeness for major countries in recent years
WITH recent_coverage AS (
    SELECT 
        ac.area,
        pcl.year,
        COUNT(DISTINCT ic.item_code) as items_covered,
        COUNT(DISTINCT ec.element_code) as elements_covered,
        COUNT(*) as total_records
    FROM production_crops_livestock pcl
    JOIN area_codes ac ON ac.id = pcl.area_code_id
    JOIN item_codes ic ON ic.id = pcl.item_code_id
    JOIN elements ec ON ec.id = pcl.element_code_id
    WHERE pcl.year >= 2018
        AND ac.area IN ('United States of America', 'China', 'India', 'Brazil', 
                        'Germany', 'France', 'United Kingdom of Great Britain and Northern Ireland',
                        'Japan', 'Canada', 'Australia', 'Argentina', 'Mexico',
                        'Indonesia', 'Türkiye', 'Italy', 'Spain', 'Nigeria', 'Egypt')
    GROUP BY ac.area, pcl.year
)
SELECT 
    area as country,
    MAX(CASE WHEN year = 2018 THEN items_covered END) as items_2018,
    MAX(CASE WHEN year = 2019 THEN items_covered END) as items_2019,
    MAX(CASE WHEN year = 2020 THEN items_covered END) as items_2020,
    MAX(CASE WHEN year = 2021 THEN items_covered END) as items_2021,
    MAX(CASE WHEN year = 2022 THEN items_covered END) as items_2022,
    ROUND(AVG(items_covered), 1) as avg_items,
    SUM(total_records) as total_records_5yr
FROM recent_coverage
GROUP BY area
ORDER BY avg_items DESC;