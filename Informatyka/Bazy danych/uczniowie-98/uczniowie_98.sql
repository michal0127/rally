DROP TABLE IF EXISTS uczniowie;
CREATE TABLE uczniowie (
	id_ucz CHAR(8) PRIMARY KEY,
	imie VARCHAR(30) NOT NULL CHECK (ime <> ''),
	nazwisko VARCHAR(30) NOT NULL CHECK (nazwisko <> ''),
	klasa CHAR (5) DEFAULT ''
);

DROP TABLE IF EXISTS przedmioty;
CREATE TABLE przedmioty (
	id_przedm INTEGER PRIMARY KEY AUTO_INCREMENT,
	nazwa VARCHAR(60) NOT NULL CHECK (nazwa <> ''),
);

DROP TABLE IF EXISTS oceny;
CREATE TABLE (
    id_oceny INTEGER PRIMARY KEY AUTO_INCREMENT,
    data DATE NOT NULL,
    id_ucz CHAR(8),
    id_przedm INTEGER,
    ocena DECIMAL(3,2),
    FOREIGN KEY (id_ucz) REFERENCES uczniowie(id_ucz)
    ON DELETE CASCADE,
    FOREIGN KEY (id_przedm)
    ON DELETE SET NULL
    );
