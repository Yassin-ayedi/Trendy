CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'Trendy!123';

CREATE DATABASE SCOPED CREDENTIAL MyDatalakeCred
WITH IDENTITY = 'Managed Identity';

CREATE EXTERNAL DATA SOURCE SocialGold
WITH (
    LOCATION = 'abfss://gold@datalakeyassin.dfs.core.windows.net'
);
