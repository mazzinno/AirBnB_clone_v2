-- Check if the 'hbnb_test_db' database exists, and create it if it doesn't
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
FLUSH PRIVILEGES;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
