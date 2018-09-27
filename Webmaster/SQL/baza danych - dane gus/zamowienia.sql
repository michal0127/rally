DROP TABLE IF EXISTS dane_klient;
CREATE TABLE dane_klient
(
    idKlient INTEGER PRIMARY KEY AUTOINCREMENT,
    imięKlient TEXT(10),
    nazwiskoklient TEXT(15),
    Adres TEXT(37),
    KodPocztowy TEXT(7),
    miasto TEXT(30),
    # https://www.sqlpedia.pl/projektowanie-i-normalizacja-bazy-danych/
    
);

DROP TABLE IF EXISTS zamówienie;
CREATE TABLE zamówienie
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    WartZamNetto DECIMAL,
    Vat DECIMAL,
    data_zamówienia DATE,
    FOREIGN KEY (idKlient) REFERENCES dane_klient(idKlient)
);
