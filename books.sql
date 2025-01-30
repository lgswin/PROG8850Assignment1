USE assignment1;

CREATE TABLE IF NOT EXISTS books (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255),
    PRIMARY KEY(id)
);

INSERT INTO books(name) VALUES('The Hobbit-');
INSERT INTO books(name) VALUES('Lord of the Rings-');