-- Script that creates the table 'force_name' on the MySQL server.
-- The database name is expected to be passed as an argument.
-- The script uses IF NOT EXISTS to prevent failure if the table already exists.

CREATE TABLE IF NOT EXISTS force_name (
    -- id column of type INT
    id INT,
    -- name column of type VARCHAR(256) that cannot be NULL (must be provided on insert)
    name VARCHAR(256) NOT NULL
);
