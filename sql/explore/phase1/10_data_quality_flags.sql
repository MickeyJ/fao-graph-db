-- Understanding data quality indicators
SELECT 
    f.flag,
    f.description,
    COUNT(DISTINCT f.source_dataset) as datasets_using,
    -- Sample usage from production data
    COALESCE(prod_counts.record_count, 0) as production_records,
    COALESCE(prod_counts.percentage, 0) as production_percentage
FROM flags f
LEFT JOIN (
    SELECT 
        f2.flag,
        COUNT(*) as record_count,
        ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 2) as percentage
    FROM production_crops_livestock pcl
    JOIN flags f2 ON f2.id = pcl.flag_id
    GROUP BY f2.flag
) prod_counts ON prod_counts.flag = f.flag
GROUP BY f.flag, f.description, prod_counts.record_count, prod_counts.percentage
ORDER BY COALESCE(prod_counts.record_count, 0) DESC;