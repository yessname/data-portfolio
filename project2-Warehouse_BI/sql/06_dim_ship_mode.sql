DROP TABLE IF EXISTS warehouse.dim_ship_mode;

CREATE TABLE warehouse.dim_ship_mode (
    ship_mode_id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    ship_mode    text NOT NULL UNIQUE
);

INSERT INTO warehouse.dim_ship_mode (ship_mode)
SELECT DISTINCT
    ship_mode
FROM staging.raw_orders
WHERE ship_mode IS NOT NULL;