-- yaml_node_migration.cypher.sql.jinja2
-- Create ItemCode nodes from item_codes
UNWIND $data AS row
CREATE (n:ItemCode {
    id: row.id,
    item_code: row.item_code,
    item: row.item,
    item_code_cpc: row.item_code_cpc,
    item_code_fbs: row.item_code_fbs,
    item_code_sdg: row.item_code_sdg,
    source_dataset: row.source_dataset
})
RETURN count(n)