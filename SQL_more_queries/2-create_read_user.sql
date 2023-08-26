-- creates the database hbtn_0d_2 and the user user_0d_2
-- give only READ privileges to the new user
CREATE DATABASE hbtn_0d_2 IF NOT EXISTS;

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' 
IDENTIFIED BY 'user_0d_2_pwd';

GRANT SELECT
ON hbtn_0d_2.*
TO 'user_0d_2'@'localhost';