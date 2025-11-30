-- Script that lists all records of the table second_table,
-- excluding rows where the name is NULL or empty.
-- Results display the score and the name, ordered by score (descending).
SELECT `score`, `name`
FROM `second_table`
WHERE `name` IS NOT NULL
ORDER BY `score` DESC;
