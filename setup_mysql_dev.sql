-- Set database and grant
-- Creates a database and a user with a password
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

GRANT ALL ON hbnb_dev_db . * TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema . * TO 'hbnb_dev'@'localhost';
-- 989e314a-b5db-4af8-a751-37865e7e01d6

-- echo 'create City state_id="989e314a-b5db-4af8-a751-37865e7e01d6" name="San_Francisco"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py

-- e7c44fb9-9705-4663-9c8f-e89dee383d53

-- echo 'create City state_id="989e314a-b5db-4af8-a751-37865e7e01d6" name="San_Jose"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py