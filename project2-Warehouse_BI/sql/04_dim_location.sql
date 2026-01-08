DROP TABLE IF EXISTS warehouse.dim_location;

CREATE TABLE warehouse.dim_location (
    location_id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    country     text,
    city        text,
    state       text,
    region      text,
    postal_code int,
    UNIQUE (country, city, state, region, postal_code)
);

INSERT INTO warehouse.dim_location (country, city, state, region, postal_code)
SELECT DISTINCT
    country,
    city,
    state,
    region,
    postal_code
FROM staging.raw_orders;
