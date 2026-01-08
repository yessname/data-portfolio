DROP TABLE IF EXISTS warehouse.dim_product;

CREATE TABLE warehouse.dim_product AS
SELECT DISTINCT
    product_id,
    product_name,
    sub_category,
    category
FROM staging.raw_orders;