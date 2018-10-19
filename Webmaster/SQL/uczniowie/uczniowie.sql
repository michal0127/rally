DROP TABLE IF EXISTS ucziowie;
CREATE TABLE uczniowie
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    imie TEXT(20),
    nazwisko TEXT(20),
    plec BOOLEAN,
    id_klasa INTEGER,
    egz_hum NUMERIC NOT NULL DEFAULT 0,
    egz_mat NUMERIC NOT NULL DEFAULT 0,
    egz_jez NUMERIC NOT NULL DEFAULT 0,
    FOREIGN KEY (id_klasa) REFERENCES klasy(id)
);

DROP TABLE IF EXISTS klasy;
CREATE TABLE klasy
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    klasa TEXT(4),
    rok_naboru INTEGER,
    rok_matury INTEGER
);

DROP TABLE IF EXISTS przedmioty;
CREATE TABLE przedmioty
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    przedmiot TEXT,
    nazwisko_naucz TEXT,
    imie_naucz TEXT,
    plec_naucz BOOLEAN
);

DROP TABLE IF EXISTS oceny;
CREATE TABLE oceny
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    datad DATE,
    id_uczen INTEGER,
    id_przedmiot INTEGER,
    ocena INTEGER,
    FOREIGN KEY (id_uczen) REFERENCES klasy(id),
    FOREIGN KEY (id_przedmiot) REFERENCES przedmioty(id)
);
