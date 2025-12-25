CREATE TABLE dim_date (
    date_id INT IDENTITY(1,1) NOT NULL,
    full_date DATE,
    year INT,
    month INT,
    day INT,
    CONSTRAINT PK_dim_date PRIMARY KEY NONCLUSTERED (date_id) NOT ENFORCED
);

CREATE TABLE dim_tools (
    tool_id INT IDENTITY(1,1) NOT NULL,
    tool_name VARCHAR(255),
    CONSTRAINT PK_dim_tools PRIMARY KEY NONCLUSTERED (tool_id) NOT ENFORCED 
);

CREATE TABLE dim_domains (
    domain_id INT IDENTITY(1,1) NOT NULL,
    domain_name VARCHAR(255),
    CONSTRAINT PK_dim_domains PRIMARY KEY NONCLUSTERED (domain_id) NOT ENFORCED 
);

CREATE TABLE dim_source (
    source_id INT IDENTITY(1,1) NOT NULL,
    source_name VARCHAR(50),
    CONSTRAINT PK_dim_source PRIMARY KEY NONCLUSTERED (source_id) NOT ENFORCED 
);

CREATE TABLE fact_social_popularity (
    popularity_id INT IDENTITY(1,1) NOT NULL,
    date_id INT NOT NULL,    
    tool_id INT NOT NULL,
    domain_id INT NOT NULL,
    source_id INT NOT NULL,
    job_engagement FLOAT,
    tool_mentions INT,
    CONSTRAINT PK_fact_social_popularity PRIMARY KEY NONCLUSTERED (popularity_id) NOT ENFORCED 
);


CREATE TABLE dim_location (
    location_id INT IDENTITY(1,1) NOT NULL,
    location_name VARCHAR(255),
    CONSTRAINT PK_dim_location PRIMARY KEY NONCLUSTERED (location_id) NOT ENFORCED 
);

CREATE TABLE fact_demand (
    demand_id INT IDENTITY(1,1) NOT NULL,
    date_id INT NOT NULL,    
    tool_id INT NOT NULL,
    domain_id INT NOT NULL,
    location_id INT NOT NULL,
    job_posting INT,
    CONSTRAINT PK_fact_demand PRIMARY KEY NONCLUSTERED (demand_id) NOT ENFORCED 
);