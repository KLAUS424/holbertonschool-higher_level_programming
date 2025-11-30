-- 14-my_genres.sql
-- Lists all genres of the TV show Dexter.

-- Select the name of the genre
SELECT DISTINCT g.name
FROM tv_genres AS g
-- Join with the tv_show_genres link table
INNER JOIN tv_show_genres AS tsg
  ON g.id = tsg.genre_id
-- Join with the tv_shows table to filter by show title
INNER JOIN tv_shows AS ts
  ON tsg.show_id = ts.id
-- Filter the results to only include the show titled 'Dexter'
WHERE ts.title = 'Dexter'
-- Order the results alphabetically by genre name
ORDER BY g.name ASC;
