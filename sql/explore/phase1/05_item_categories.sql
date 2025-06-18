-- sql/phase1/05_item_categories_overview.sql (FIXED STRING_AGG)
-- Major commodity categories in the database
WITH unique_items AS (
    SELECT DISTINCT item_code, item, item_code_cpc, item_code_fbs, item_code_sdg
    FROM item_codes
),
categorized_items AS (
    SELECT 
        item_code,
        item,
        CASE 
            WHEN item LIKE '%wheat%' OR item LIKE '%rice%' OR item LIKE '%maize%' 
                 OR item LIKE '%barley%' OR item LIKE '%cereal%' THEN '01. Cereals'
            WHEN item LIKE '%meat%' OR item LIKE '%beef%' OR item LIKE '%pork%' 
                 OR item LIKE '%poultry%' OR item LIKE '%chicken%' THEN '02. Meat'
            WHEN item LIKE '%milk%' OR item LIKE '%cheese%' OR item LIKE '%butter%' 
                 OR item LIKE '%dairy%' OR item LIKE '%yoghurt%' THEN '03. Dairy'
            WHEN item LIKE '%egg%' THEN '04. Eggs'
            WHEN item LIKE '%fish%' OR item LIKE '%aqua%' THEN '05. Fish/Aquaculture'
            WHEN item LIKE '%vegetable%' OR item LIKE '%tomato%' OR item LIKE '%potato%' 
                 OR item LIKE '%onion%' THEN '06. Vegetables'
            WHEN item LIKE '%fruit%' OR item LIKE '%apple%' OR item LIKE '%banana%' 
                 OR item LIKE '%orange%' OR item LIKE '%grape%' THEN '07. Fruits'
            WHEN item LIKE '%oil%' OR item LIKE '%fat%' THEN '08. Oils & Fats'
            WHEN item LIKE '%sugar%' OR item LIKE '%sweetener%' THEN '09. Sugar & Sweeteners'
            WHEN item LIKE '%coffee%' OR item LIKE '%tea%' OR item LIKE '%cocoa%' THEN '10. Beverages'
            WHEN item LIKE '%fertilizer%' THEN '11. Fertilizers'
            WHEN item LIKE '%pesticide%' THEN '12. Pesticides'
            WHEN item LIKE '%emission%' OR item LIKE '%CO2%' OR item LIKE '%CH4%' 
                 OR item LIKE '%N2O%' OR item LIKE '%greenhouse%' THEN '13. Emissions/Climate'
            WHEN item LIKE '%land%' OR item LIKE '%forest%' THEN '14. Land Use'
            WHEN item LIKE '%feed%' THEN '15. Animal Feed'
            WHEN item LIKE '%seed%' THEN '16. Seeds'
            WHEN item LIKE '%energy%' OR item LIKE '%biofuel%' THEN '17. Energy/Biofuels'
            WHEN item LIKE '%population%' OR item LIKE '%GDP%' THEN '18. Socioeconomic'
            WHEN item LIKE '%total%' OR item LIKE '%aggregate%' OR item LIKE '%+%' THEN '19. Aggregates'
            ELSE '20. Other'
        END as commodity_category
    FROM unique_items
)
SELECT 
    commodity_category,
    COUNT(*) as item_count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 2) as percentage
FROM categorized_items
GROUP BY commodity_category
ORDER BY commodity_category;