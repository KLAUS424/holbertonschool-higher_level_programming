-- Script that creates the MySQL server user 'user_0d_1' on localhost.
-- The user is granted all privileges and has the password 'user_0d_1_pwd'.
-- The script does not fail if the user already exists (using IF NOT EXISTS, if supported).

-- 1. Create the user if they do not exist.
-- Note: MySQL's CREATE USER usually raises an error if the user exists,
-- but the following two commands (CREATE and GRANT) are the standard way to ensure
-- the user has the required state without causing script failure on a fresh run.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- 2. Grant all privileges on the entire server (*.*) to the user.
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- 3. Apply the changes immediately.
FLUSH PRIVILEGES;
