-- This code selects the 'title' column from the 'tv_shows' table and the 'genre_id' column from the 'tv_show_genres' table
-- The rows from the 'tv_shows' table are joined with the rows from the 'tv_show_genres' table where the value of the 'id' column in the 'tv_shows' table matches the value of the 'show_id' column in the 'tv_show_genres' table
-- The results are sorted first by the 'title' column of the 'tv_shows' table in ascending order, and then by the 'genre_id' column of the 'tv_show_genres' table in ascending order
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
