-- This code creates a new table named 'id_not_null' in the current database, if it does not already exist
-- The table has two columns: 'id' of type INT with a default value of 1 and 'name' of type VARCHAR(256)
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
