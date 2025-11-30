-- Script that creates a table named 'first_table' in the current database.
-- The database name is passed as an argument to the mysql command.
-- The IF NOT EXISTS clause prevents the script from failing if the table already exists.
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
