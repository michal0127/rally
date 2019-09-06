DROP TABLE IF EXIST nazwiska;
CREATE TABLE nazwiska
(
    Nr_ucznia INTEGER Primary KEY
    Nazwisko TEXT(25),
    Imie1 TEXT(25),
    Imie2 TEXT(25) DEFAULT NULL,
):

DROP TABLE IF EXIST dane_osobowe;
CREATE TABLE dane_osobowe
(
    Nr_ucznia INTEGER FOREIGN KEY,
    Dzien INTEGER,
    Miesiac INTEGER,
    Rok INTEGER,
    Miejsce_urodzenia TEXT(25),
    Wojewodztwo TEXT(25),
    FOREIGN KEY (Nr_ucznia) REFERENCES dane_osobowe(Nr_ucznia)
);

DROP TABLE IF EXIST oceny;
CREATE TABLE oceny
(
    Nr_ucznia INTEGER FOREIGN KEY,
    Zachowanie DECIMAL DEFAULT NULL,
    Religia_Etyka DECIMAL DEFAULT NULL,
    Jpolski DECIMAL DEFAULT NULL,
    Jangielski DECIMAL DEFAULT NULL,
    Jniemiecki DECIMAL DEFAULT NULL,
    Matematyka DECIMAL DEFAULT NULL,
    Hitoria DECIMAL DEFAULT NULL,
    Geografia DECIMAL DEFAULT NULL,
    Biologia DECIMAL DEFAULT NULL,
    Fizyka DECIMAL DEFAULT NULL,
    Chemia DECIMAL DEFAULT NULL,
    Technika DECIMAL DEFAULT NULL,
    Informatyka DECIMAL DEFAULT NULL,
    Plastyka DECIMAL DEFAULT NULL,
    PO DECIMAL DEFAULT NULL,
    WF DECIMAL DEFAULT NULL,
    FOREIGN KEY (Nr_ucznia) REFERENCES dane_osobowe(Nr_ucznia)
);
);
