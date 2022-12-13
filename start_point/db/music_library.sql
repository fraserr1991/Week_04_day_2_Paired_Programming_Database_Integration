DROP TABLE IF EXISTS albums;

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE albums (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(255),
    genre VARCHAR(255),
    artist VARCHAR(255)
    
);

INSERT INTO albums (name, genre, artist) VALUES ('Midnight Organ Fight', 'Indie', 'Frightened Rabbit');
INSERT INTO albums (name, genre, artist) VALUES ('Isles', 'Electro', 'Bicep')
