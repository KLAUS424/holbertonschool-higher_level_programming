-- Script that lists all records in the table 'second_table' with a score >= 10.
-- Results display the score and the name, ordered by score (descending).
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
