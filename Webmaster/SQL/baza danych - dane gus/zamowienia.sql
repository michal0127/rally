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

DROP TABLE IF EXISTS tbpowierzchnie;
CREATE TABLE tbpowierzchnie
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    powierzchnia_miasta DECIMAL,
    powierzchnia_zielona DECIMAL,
    data_aktualizacji DATE,
    id_miasta INTEGER,
    FOREIGN KEY (id_miasta) REFERENCES tbmiasta(id_miasta)
);

DROP TABLE IF EXISTS tbdane_gus;
CREATE TABLE tbdane_gus
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    liczba_mieszkancow INTEGER,
    liczba_kobiet INTEGER,
    grupa_wiekowa TEXT(17),
    data_aktualizacji DATE,
    id_miasta INTEGER,
    FOREIGN KEY (id_miasta) REFERENCES tbmiasta(id_miasta)
);
