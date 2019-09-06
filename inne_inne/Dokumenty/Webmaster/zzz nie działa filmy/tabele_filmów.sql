DROP TABLE IF EXIST tbFilmy;
CREATE TABLE tbFilmy (
    id INTEGER PRIMARY KEY,
    name TEXT,
    genre TEXT,
    year INTEGER,
    imdb_rating NUMERIC
);
