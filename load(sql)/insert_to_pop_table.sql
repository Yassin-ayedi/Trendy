INSERT INTO dim_date (full_date, year, month, day)
SELECT DISTINCT 
    CAST(CONCAT(year,'-',month,'-',day) AS DATE) AS full_date,
    year,
    month,
    day
FROM stg_social_popularity st
WHERE NOT EXISTS (
    SELECT 1 
    FROM dim_date d
    WHERE d.full_date = CAST(CONCAT(st.year,'-',st.month,'-',st.day) AS DATE)
);


INSERT INTO dim_tools (tool_name)
SELECT DISTINCT tool
FROM stg_social_popularity st
WHERE NOT EXISTS (
    SELECT 1 FROM dim_tools t
    WHERE t.tool_name = st.tool
);


INSERT INTO dim_domains (domain_name)
SELECT DISTINCT job
FROM stg_social_popularity st
WHERE NOT EXISTS (
    SELECT 1 FROM dim_domains j
    WHERE j.domain_name = st.job
);

INSERT INTO dim_source (source_name)
SELECT DISTINCT source
FROM stg_social_popularity st
WHERE NOT EXISTS (
    SELECT 1 FROM dim_source s
    WHERE s.source_name = st.source
);

INSERT INTO fact_social_popularity (date_id, tool_id, domain_id, source_id, job_engagement, tool_mentions)
SELECT
    d.date_id,
    t.tool_id,
    j.domain_id,
    s.source_id,
    st.job_engagement,
    st.tool_mentions
FROM stg_social_popularity st
JOIN dim_date d
    ON d.year = st.year AND d.month = st.month AND d.day = st.day
JOIN dim_tools t
    ON t.tool_name = st.tool
JOIN dim_domains j
    ON j.domain_name = st.job
JOIN dim_source s
    ON s.source_name = st.source
WHERE st.ingestion_time > (SELECT MAX(last_run_time) FROM etl_metadata);

UPDATE etl_metadata
SET last_run_time = CURRENT_TIMESTAMP

