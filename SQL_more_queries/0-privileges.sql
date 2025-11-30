-- Script that lists all privileges for the MySQL users user_0d_1 and user_0d_2 on localhost.
-- It attempts to show grants for both users, even if one or both do not exist or have no grants defined yet.
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
