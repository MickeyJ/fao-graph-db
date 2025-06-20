-- Create Donor nodes from donors
SELECT * FROM cypher('fao_graph', $
    CREATE (n:Donor {
        id: row.id,
        donor_code: row.donor_code,
        donor: row.donor,
        donor_code_m49: row.donor_code_m49,
        source_dataset: row.source_dataset,
    })   
$) AS (result agtype)
FROM donors row;