-- Script that creates the database hbtn_0d_usa and the table states.

-- 1. Create the database hbtn_0d_usa if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- 2. Use the created (or existing) database
USE hbtn_0d_usa;

-- 3. Create the table states if it does not already exist
CREATE TABLE IF NOT EXISTS states (
    -- id: INT, unique, auto generated, can't be null and is a primary key
    id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
    -- name: VARCHAR(256) can't be null
    name VARCHAR(256) NOT NULL
);
