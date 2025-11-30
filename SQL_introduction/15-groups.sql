-- Script that lists the number of records with the same score.
-- Displays the score and the count, labeled as 'number'.
-- The results are sorted by the count (number of records) in descending order.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
