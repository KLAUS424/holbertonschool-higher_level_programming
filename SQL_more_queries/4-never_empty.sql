-- Script that creates the table 'id_not_null' on the MySQL server.
-- The database name is expected to be passed as an argument.
-- The script uses IF NOT EXISTS to prevent failure if the table already exists.

CREATE TABLE IF NOT EXISTS id_not_null (
    -- id column of type INT with a default value of 1.
    -- If 'id' is not specified during INSERT, it will automatically use 1.
    id INT DEFAULT 1,
    -- name column of type VARCHAR(256)
    name VARCHAR(256)
);
