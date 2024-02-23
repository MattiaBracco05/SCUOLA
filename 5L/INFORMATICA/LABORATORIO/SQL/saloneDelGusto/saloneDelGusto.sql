-- Creazione del database se non esiste
CREATE DATABASE IF NOT EXISTS SaloneDelGusto;

-- Selezione del database
USE SaloneDelGusto;

-- TABELLA AZIENDA
CREATE TABLE IF NOT EXISTS Azienda (
    NomeAzienda VARCHAR(16) NOT NULL,
    PRIMARY KEY (NomeAzienda)
);

-- TABELLA STAND
CREATE TABLE IF NOT EXISTS Stand (
    ID_Stand INT NOT NULL AUTO_INCREMENT,
    ZonaStand VARCHAR(16) NOT NULL,
    Superficie INT NOT NULL,
    NomeAzienda VARCHAR(16) NOT NULL,
    PRIMARY KEY (ID_Stand),
    FOREIGN KEY (NomeAzienda) REFERENCES Azienda(NomeAzienda)
);

-- TABELLA VISITATORE
CREATE TABLE IF NOT EXISTS Visitatore (
    ID_Visitatore INT AUTO_INCREMENT NOT NULL,
    NomeVisitatore VARCHAR(16) NOT NULL,
    EtaVisitatore INT NOT NULL,
    PRIMARY KEY (ID_Visitatore)
);

-- TABELLA PRODOTTO
CREATE TABLE IF NOT EXISTS Prodotto (
    ID_Prodotto INT AUTO_INCREMENT NOT NULL,
    Caratteristiche VARCHAR(16) NOT NULL,
    Tipologia VARCHAR(16) NOT NULL,
    NomeAzienda VARCHAR(16) NOT NULL,
    ID_Stand INT NOT NULL,
    PRIMARY KEY (ID_Prodotto),
    FOREIGN KEY (NomeAzienda) REFERENCES Azienda(NomeAzienda),
    FOREIGN KEY (ID_Stand) REFERENCES Stand(ID_Stand)
);

-- TABELLA ASSAGGIA
CREATE TABLE IF NOT EXISTS Assaggia (
    NumeroAssaggi INT NOT NULL,
    ID_Visitatore INT NOT NULL,
    ID_Prodotto INT NOT NULL,
    PRIMARY KEY (ID_Visitatore, ID_Prodotto),
    FOREIGN KEY (ID_Visitatore) REFERENCES Visitatore(ID_Visitatore),
    FOREIGN KEY (ID_Prodotto) REFERENCES Prodotto(ID_Prodotto)
);

-- Mostra le tabelle create
SHOW TABLES;

-- Descrizione della tabella Azienda
\! echo '\nTabella "Azienda"'
DESCRIBE Azienda;

-- Descrizione della tabella Stand
\! echo '\nTabella "Stand"'
DESCRIBE Stand;

-- Descrizione della tabella Visitatore
\! echo '\nTabella "Visitatore"'
DESCRIBE Visitatore;

-- Descrizione della tabella Prodotto
\! echo '\nTabella "Prodotto"'
DESCRIBE Prodotto;

-- Descrizione della tabella Assaggia
\! echo '\nTabella "Assaggia"'
DESCRIBE Assaggia;
