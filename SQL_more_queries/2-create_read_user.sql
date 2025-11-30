-- Script that creates the database hbtn_0d_2 and the user user_0d_2.
-- The user 'user_0d_2' is granted only SELECT privilege on 'hbtn_0d_2'.
-- The script does not fail if the database or the user already exists.

-- 1. Create the database hbtn_0d_2 if it does not already exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- 2. Create the user user_0d_2 on localhost if they do not exist,
-- and set the password to 'user_0d_2_pwd'.
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- 3. Grant only SELECT privilege on all tables within the hbtn_0d_2 database to the new user.
-- The 'hbtn_0d_2'.* syntax means "all tables in hbtn_0d_2".
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- 4. Apply the changes immediately to ensure the grants are active.
FLUSH PRIVILEGES;
