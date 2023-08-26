-- creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa)
-- creates database and table with foreign key
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE DATABASE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256),
    FOREIGN KEY (state_id) REFERENCES states(id)
);