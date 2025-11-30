-- 15-comedy_only.sql
-- Lists all TV shows that belong to the genre Comedy.

-- Select the title of the TV show
SELECT ts.title
FROM tv_shows AS ts
-- Join with the tv_show_genres link table
INNER JOIN tv_show_genres AS tsg
  ON ts.id = tsg.show_id
-- Join with the tv_genres table to filter by genre name
INNER JOIN tv_genres AS tg
  ON tsg.genre_id = tg.id
-- Filter the results to only include the genre titled 'Comedy'
WHERE tg.name = 'Comedy'
-- Order the results alphabetically by the show title
ORDER BY ts.title ASC;
