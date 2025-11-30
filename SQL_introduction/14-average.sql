-- Script that computes the score average of all records in the table 'second_table'.
-- The result column is renamed to 'average' using the AS keyword.
SELECT AVG(`score`) AS `average`
FROM `second_table`;
