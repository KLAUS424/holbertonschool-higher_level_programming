-- Script that creates the table 'unique_id' on the MySQL server.
-- The database name is expected to be passed as an argument.
-- The script uses IF NOT EXISTS to prevent failure if the table already exists.

CREATE TABLE IF NOT EXISTS unique_id (
    -- id column of type INT with a default value of 1.
    -- The UNIQUE constraint ensures that all values in this column are distinct.
    id INT DEFAULT 1 UNIQUE,
    -- name column of type VARCHAR(256)
    name VARCHAR(256)
);
