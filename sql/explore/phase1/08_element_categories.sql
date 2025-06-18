-- Elements grouped by measurement category
WITH unique_elements AS (
    SELECT DISTINCT element_code, element
    FROM elements
)
SELECT 
    CASE 
        WHEN element LIKE '%production%' OR element LIKE '%harvest%' THEN '01. Production'
        WHEN element LIKE '%yield%' THEN '02. Productivity'
        WHEN element LIKE '%area%' THEN '03. Area/Land'
        WHEN element LIKE '%import%' OR element LIKE '%export%' THEN '04. Trade'
        WHEN element LIKE '%price%' OR element LIKE '%value%' THEN '05. Economic/Price'
        WHEN element LIKE '%stock%' OR element LIKE '%inventory%' THEN '06. Stocks'
        WHEN element LIKE '%food%' OR element LIKE '%feed%' OR element LIKE '%waste%' THEN '07. Utilization'
        WHEN element LIKE '%emission%' OR element LIKE '%CO2%' THEN '08. Environmental'
        WHEN element LIKE '%calori%' OR element LIKE '%protein%' OR element LIKE '%fat%' THEN '09. Nutritional'
        WHEN element LIKE '%population%' OR element LIKE '%capita%' THEN '10. Per Capita'
        ELSE '11. Other'
    END as element_category,
    COUNT(*) as element_count,
    STRING_AGG(element, '; ' ORDER BY element LIMIT 5) as examples
FROM unique_elements
GROUP BY element_category
ORDER BY element_category;