-- This code creates a new table named 'force_name' in the current database, if it does not already exist
-- The table has two columns: 'id' of type INT and 'name' of type VARCHAR(256) which cannot be NULL
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
