-- yaml_node_indexes.sql.jinja2
-- Indexes for AreaCode nodes
CREATE INDEX IF NOT EXISTS idx_area_codes_id
ON fao_graph."AreaCode" (id);

CREATE INDEX IF NOT EXISTS idx_area_codes_area_code 
ON fao_graph."AreaCode" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"area_code"'::agtype])
);

CREATE INDEX IF NOT EXISTS idx_area_codes_sd_production_crops_livestock
ON fao_graph."AreaCode" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
)
WHERE agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype]) = '"production_crops_livestock"'::agtype;


CREATE INDEX IF NOT EXISTS idx_area_codes_sd_emissions_agriculture_energy
ON fao_graph."AreaCode" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
)
WHERE agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype]) = '"emissions_agriculture_energy"'::agtype;


CREATE INDEX IF NOT EXISTS idx_area_codes_sd_emissions_agriculture_energy
ON fao_graph."AreaCode" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
)
WHERE agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype]) = '"emissions_agriculture_energy"'::agtype;


CREATE INDEX IF NOT EXISTS idx_area_codes_sd_food_balance_sheets
ON fao_graph."AreaCode" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
)
WHERE agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype]) = '"food_balance_sheets"'::agtype;


CREATE INDEX IF NOT EXISTS idx_area_codes_sd_food_balance_sheets
ON fao_graph."AreaCode" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
)
WHERE agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype]) = '"food_balance_sheets"'::agtype;


CREATE INDEX IF NOT EXISTS idx_area_codes_sd_food_balance_sheets
ON fao_graph."AreaCode" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
)
WHERE agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype]) = '"food_balance_sheets"'::agtype;


CREATE INDEX IF NOT EXISTS idx_area_codes_sd_food_security_data
ON fao_graph."AreaCode" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
)
WHERE agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype]) = '"food_security_data"'::agtype;


CREATE INDEX IF NOT EXISTS idx_area_codes_sd_food_security_data
ON fao_graph."AreaCode" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
)
WHERE agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype]) = '"food_security_data"'::agtype;


CREATE INDEX IF NOT EXISTS idx_area_codes_sd_prices
ON fao_graph."AreaCode" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
)
WHERE agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype]) = '"prices"'::agtype;



-- Compound index for node lookups
CREATE INDEX IF NOT EXISTS idx_area_codes_properties
ON fao_graph."AreaCode" USING GIN (properties);