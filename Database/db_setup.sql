-- Prepare MySQL server for the projct

CREATE DATABASE IF NOT EXISTS taskvault_db;
CREATE USER IF NOT EXISTS 'taskvault_user'@'localhost' IDENTIFIED BY 'osamanazar47';
GRANT ALL PRIVILEGES ON `taskvault_db`.* TO 'taskvault_user'@'localhost';
GRANT SELECT ON `preformance_schema`.* TO 'taskvault_user'@'localhost';
FLUSH PRIVILEGES;
