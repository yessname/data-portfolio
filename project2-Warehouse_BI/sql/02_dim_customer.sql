DROP TABLE IF EXISTS warehouse.dim_customer;

CREATE TABLE warehouse.dim_customer AS
SELECT DISTINCT
    customer_id,
    customer_name,
    segment
FROM staging.raw_orders;

ALTER TABLE warehouse.dim_customer
    ADD CONSTRAINT pk_dim_customer PRIMARY KEY (customer_id);