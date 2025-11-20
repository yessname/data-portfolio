CREATE SCHEMA IF NOT EXISTS airbnb;

CREATE TABLE IF NOT EXISTS airbnb.listings (
    listing_id              INT PRIMARY KEY,
    host_id                 INT,
	neighbourhood_group     TEXT,
    neighbourhood           TEXT,
    latitude                DOUBLE PRECISION,
    longitude               DOUBLE PRECISION,
    room_type               TEXT,
    price                   NUMERIC(10, 2),
    minimum_nights          INT,
    number_of_reviews       INT,
    last_review             DATE,
    reviews_per_month       NUMERIC(10, 2),
	host_listings_count     INT,
    availability_365        INT
);