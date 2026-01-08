DROP TABLE IF EXISTS warehouse.dim_date;

CREATE TABLE warehouse.dim_date (
    date_id         integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    date            date NOT NULL UNIQUE,
    year            int,
    month           int,
    day             int,
    day_of_week     int,
    day_of_week_name text,
    week            int,
    quarter         int
);

INSERT INTO warehouse.dim_date (
    date,
    year,
    month,
    day,
    day_of_week,
    day_of_week_name,
    week,
    quarter
)
SELECT DISTINCT
    CAST(d AS date)                             AS date,
    EXTRACT(YEAR  FROM d)                       AS year,
    EXTRACT(MONTH FROM d)                       AS month,
    EXTRACT(DAY   FROM d)                       AS day,
    EXTRACT(DOW   FROM d)                       AS day_of_week,
    TO_CHAR(d, 'Day')                           AS day_of_week_name,
    EXTRACT(WEEK  FROM d)                       AS week,
    EXTRACT(QUARTER FROM d)                     AS quarter
FROM (
    SELECT order_date AS d FROM staging.raw_orders
    UNION
    SELECT ship_date  AS d FROM staging.raw_orders
) t
WHERE d IS NOT NULL;
