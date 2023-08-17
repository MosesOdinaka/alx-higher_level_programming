-- This code creates a new MySQL database 'hbtn_0d_2' on the local server, if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- This code creates a new MySQL user 'user_0d_2' on the local server, if it does not already exist, with the password 'user_0d_2_pwd'
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- This code grants the SELECT privilege to the user 'user_0d_2' on all tables in the 'hbtn_0d_2' database on the local server
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
-- This code reloads the privileges from the grant tables in the MySQL system database
FLUSH PRIVILEGES;
