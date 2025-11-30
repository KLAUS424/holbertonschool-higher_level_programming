-- Script that updates the score of Bob to 10 in the table 'second_table'.
-- We use the name field in the WHERE clause, as the id is restricted.
UPDATE `second_table`
SET `score` = 10
WHERE `name` = 'Bob';
