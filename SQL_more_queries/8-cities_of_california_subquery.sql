-- Script that lists all the cities of California that can be found in the database hbtn_0d_usa.
-- Results must be sorted in ascending order by cities.id.
-- Must use a subquery to find the state ID for 'California'.

SELECT id, name
FROM cities
WHERE state_id = (
    -- Subquery: Find the id of the state named 'California'
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;
