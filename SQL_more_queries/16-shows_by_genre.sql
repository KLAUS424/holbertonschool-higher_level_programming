-- 16-shows_by_genre.sql
-- Lists all shows and all genres linked to that show, displaying NULL if no genre exists.

-- Select the show title and the genre name
SELECT ts.title, tg.name
FROM tv_shows AS ts
-- Use a LEFT JOIN to ensure all shows are included, even those without genres.
-- Join tv_shows with tv_show_genres (link table)
LEFT JOIN tv_show_genres AS tsg
  ON ts.id = tsg.show_id
-- Join the link table with tv_genres. If tsg.genre_id is NULL, tg.name will be NULL.
LEFT JOIN tv_genres AS tg
  ON tsg.genre_id = tg.id
-- Order the results primarily by show title and secondarily by genre name
ORDER BY ts.title ASC, tg.name ASC;
