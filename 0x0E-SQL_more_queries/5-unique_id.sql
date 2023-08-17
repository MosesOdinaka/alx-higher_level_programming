-- This code creates a new table named 'unique_id' in the current database, if it does not already exist
-- The table has two columns: 'id' of type INT with a default value of 1 and 'name' of type VARCHAR(256)
-- The 'id' column has a UNIQUE constraint, which means that no two rows can have the same value in this column
CREATE TABLE IF NOT EXISTS unique_id
       (id INT DEFAULT 1,
       UNIQUE (ID),
       name VARCHAR(256));
