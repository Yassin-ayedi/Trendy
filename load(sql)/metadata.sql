-- Create ETL metadata table
CREATE TABLE etl_metadata
(
    last_run_time DATETIME
)
WITH
(
    DISTRIBUTION = ROUND_ROBIN
);


INSERT INTO etl_metadata (last_run_time)
VALUES ('1900-01-01 00:00:00');


