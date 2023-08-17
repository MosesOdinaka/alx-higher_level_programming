-- This code creates a new MySQL database named 'hbtn_0d_usa' on the local server, if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- This code creates a new table named 'states' in the 'hbtn_0d_usa' database, if it does not already exist
-- The table has two columns: 'id' of type INT with a UNIQUE constraint, NOT NULL constraint, AUTO_INCREMENT attribute, and PRIMARY KEY constraint, and 'name' of type VARCHAR(256) with a NOT NULL constraint
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
       id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(256) NOT NULL);
