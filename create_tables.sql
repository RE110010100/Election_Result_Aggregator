-- Drop table if exists for clean setup
DROP TABLE IF EXISTS national_results;
DROP TABLE IF EXISTS state_results;

-- Create tables for aggregations
CREATE TABLE national_results (
    year INT,
    party VARCHAR(50),
    total_votes BIGINT
);

CREATE TABLE state_results (
    year INT,
    state VARCHAR(50),
    party VARCHAR(50),
    total_votes BIGINT
);
