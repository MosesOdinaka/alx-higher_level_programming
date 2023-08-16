-- Displays the top 3 cities with the highest average temperature during July and August, ordered by temperature (descending)
SELECT city, AVG(temp_f) AS avg_temp
FROM temperatures
WHERE MONTH(recorded_date) IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;