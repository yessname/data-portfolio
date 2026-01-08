DROP TABLE IF EXISTS warehouse.fact_sales;

CREATE TABLE warehouse.fact_sales AS
SELECT
    s.row_id,
    s.order_id,
    s.customer_id,
    s.product_id,
    loc.location_id,
    od.date_id  AS order_date_id,
    sd.date_id  AS ship_date_id,
    sm.ship_mode_id,
    s.sales,
    s.quantity,
    s.discount,
    s.profit
FROM staging.raw_orders s
JOIN warehouse.dim_customer  c  ON s.customer_id = c.customer_id
JOIN warehouse.dim_product   p  ON s.product_id  = p.product_id
JOIN warehouse.dim_location  loc
  ON  s.country     = loc.country
  AND s.city        = loc.city
  AND s.state       = loc.state
  AND s.region      = loc.region
  AND s.postal_code = loc.postal_code
LEFT JOIN warehouse.dim_date od ON s.order_date = od.date
LEFT JOIN warehouse.dim_date sd ON s.ship_date  = sd.date
LEFT JOIN warehouse.dim_ship_mode sm ON s.ship_mode = sm.ship_mode;
