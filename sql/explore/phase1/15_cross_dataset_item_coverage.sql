-- Which items appear across multiple key datasets
WITH item_presence AS (
    SELECT DISTINCT 
        ic.item_code,
        ic.item,
        CASE WHEN EXISTS (SELECT 1 FROM production_crops_livestock p WHERE p.item_code_id = ic.id) THEN 1 ELSE 0 END as in_production,
        CASE WHEN EXISTS (SELECT 1 FROM trade_crops_livestock t WHERE t.item_code_id = ic.id) THEN 1 ELSE 0 END as in_trade,
        CASE WHEN EXISTS (SELECT 1 FROM food_balance_sheets f WHERE f.item_code_id = ic.id) THEN 1 ELSE 0 END as in_food_balance,
        CASE WHEN EXISTS (SELECT 1 FROM prices pr WHERE pr.item_code_id = ic.id) THEN 1 ELSE 0 END as in_prices
    FROM item_codes ic
)
SELECT 
    item_code,
    item,
    in_production,
    in_trade,
    in_food_balance,
    in_prices,
    (in_production + in_trade + in_food_balance + in_prices) as dataset_count
FROM item_presence
WHERE (in_production + in_trade + in_food_balance + in_prices) >= 2
ORDER BY dataset_count DESC, item;