-- This code selects the 'id' and 'name' columns from the 'cities' table, and the 'name' column from the 'states' table
-- The rows from the 'cities' table are joined with the rows from the 'states' table where the value of the 'state_id' column in the 'cities' table matches the value of the 'id' column in the 'states' table
-- The results are sorted by the 'id' column of the 'cities' table in ascending order
SELECT cities.id, cities.name, states.name FROM cities
JOIN states ON cities.state_id=states.id
ORDER BY cities.id;
