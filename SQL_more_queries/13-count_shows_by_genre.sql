-- aaaa
SELECT tv_generes.name AS genere, COUNT(show_id) AS number_of_shows
FROM tv_generes JOIN tv_show_generes ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre ORDER BY number_of_shows DESC;