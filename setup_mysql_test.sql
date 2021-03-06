-- Prepares a MySQL server for the project
-- Create database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Creates user if not found
CREATE USER 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grants privileges                                                     
GRANT USAGE ON *.* TO 'hbnb_test'@'localhost';
-- Givse privileges to user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Gives select privileges to user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
