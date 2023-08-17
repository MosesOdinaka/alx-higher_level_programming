-- This code selects the 'id' and 'name' columns from the 'cities' table
-- The rows are filtered by the 'state_id' column, which must match the 'id' of a row in the 'states' table where the 'name' is "California"
-- The results are sorted by the 'id' column in ascending order
SELECT id, name FROM cities
WHERE state_id = (
      SELECT id FROM states
      WHERE name = "California")
ORDER BY id;
