-- This query selects the title and genre_id columns from the tv_shows and
-- tv_show_genres tables, respectively. It performs a LEFT JOIN on the two
-- tables using the show_id column from tv_show_genres and the id column
-- from tv_shows. The results are then ordered by the title column from
-- tv_shows and the genre_id column from tv_show_genres.
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
