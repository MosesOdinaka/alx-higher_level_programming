-- This code creates a new MySQL user 'user_0d_1' on the local server, if it does not already exist, with the password 'user_0d_1_pwd'
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- This code grants all privileges to the user 'user_0d_1' on all databases and tables on the local server
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
-- This code reloads the privileges from the grant tables in the MySQL system database
FLUSH PRIVILEGES;
