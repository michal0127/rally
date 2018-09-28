DROP TABLE IF EXIST dane_osobowe;
CREATE TABLE dane_osobowe
(
    Nr_ucznia INTEGER PRIMARY KEY,
    Dzien INTEGER,
    Miesiac INTEGER,
    Rok INTEGER,
    Miejsce_urodzenia TEXT(25),
    Wojewodztwo TEXT(25)
);

DROP TABLE IF EXIST nazwiska;
CREATE TABLE nazwiska
(
    Nr_ucznia INTEGER FOREIGN KEY,
    Nazwisko TEXT(25),
    Imie1 TEXT(25),
    Imie2 TEXT(25) DEFAULT NULL,
    FOREIGN KEY (Nr_ucznia) REFERENCES dane_osobowe(Nr_ucznia)
):

DROP TABLE IF EXIST oceny;
CREATE TABLE oceny
(
    Nr_ucznia INTEGER FOREIGN KEY,
    Zachowanie INTEGER,
    Religia_Etyka INTEGER,
    Jpolski INTEGER,
    Jangielski INTEGER,
    Jniemiecki INTEGER,
    Matematyka INTEGER,
    Hitoria INTEGER,
    Geografia INTEGER,
    Biologia INTEGER,
    Fizyka INTEGER,
    Chemia INTEGER,
    Technika INTEGER,
    Informatyka INTEGER,
    Plastyka INTEGER,
    PO INTEGER,
    WF TEXT,
    FOREIGN KEY (Nr_ucznia) REFERENCES dane_osobowe(Nr_ucznia)
);
);
