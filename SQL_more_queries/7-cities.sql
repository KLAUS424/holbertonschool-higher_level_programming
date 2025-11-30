-- Script that creates the database hbtn_0d_usa and the table cities.

-- 1. Create the database hbtn_0d_usa if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- 2. Use the created (or existing) database
USE hbtn_0d_usa;

-- 3. Create the table cities if it does not already exist
CREATE TABLE IF NOT EXISTS cities (
    -- id: INT, unique, auto generated, can't be null and is a primary key
    id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
    -- state_id: INT, can't be null
    state_id INT NOT NULL,
    -- name: VARCHAR(256) can't be null
    name VARCHAR(256) NOT NULL,
    -- FOREIGN KEY constraint: state_id must reference a valid id in the states table
    FOREIGN KEY (state_id) REFERENCES states(id)
);
