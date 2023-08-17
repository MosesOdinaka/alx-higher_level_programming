-- This code creates a new MySQL database named 'hbtn_0d_usa' on the local server, if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- This code creates a new table named 'cities' in the 'hbtn_0d_usa' database, if it does not already exist
-- The table has three columns: 'id' of type INT with a UNIQUE constraint, NOT NULL constraint, AUTO_INCREMENT attribute, and PRIMARY KEY constraint, 'state_id' of type INT with a NOT NULL constraint and a FOREIGN KEY constraint that references the 'id' column of the 'states' table in the 'hbtn_0d_usa' database, and 'name' of type VARCHAR(256) with a NOT NULL constraint
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
       id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
       state_id INT NOT NULL,
       FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id),
       name VARCHAR(256) NOT NULL);
