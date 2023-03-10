CREATE USER 'fastapinem'@'localhost' IDENTIFIED BY 'nem';
GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD
on *.* TO 'fastapinem'@'localhost' WITH GRANT OPTION;

FLUSH PRIVILEGES;

CREATE DATABASE IF NOT EXISTS flight_scanner_database;
