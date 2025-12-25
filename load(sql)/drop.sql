TRUNCATE TABLE fact_social_popularity;
TRUNCATE TABLE dim_date;
TRUNCATE TABLE dim_tools;
TRUNCATE TABLE dim_domains;
TRUNCATE TABLE dim_source;
-- If exists
TRUNCATE TABLE etl_metadata;
INSERT INTO etl_metadata (last_run_time)
VALUES ('1900-01-01 00:00:00');