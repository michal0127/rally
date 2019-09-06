DROP TABLE IF EXISTS tbmiasta;
CREATE TABLE tbmiasta
(
    id_miasta INTEGER PRIMARY KEY AUTOINCREMENT,
    nazwa_miasta TEXT(30),
    nazwa_wojewodztwa TEXT(37)
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
