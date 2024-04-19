-- 5L Bracco Mattia

-- Creo il DB
DROP DATABASE IF EXISTS Officina;
CREATE DATABASE IF NOT EXISTS Officina;
-- Seleziono il DB
USE Officina;

-- Creo le tabelle...

-- Tabella "Cliente"
CREATE TABLE Cliente (
    CodFiscale CHAR(1),
    Nome VARCHAR(25) NOT NULL,
    Cognome VARCHAR(25) NOT NULL,
    Indirizzo VARCHAR(25) NOT NULL,
    Numero INT NOT NULL,
    CAP INT NOT NULL,
    Localita VARCHAR(25) NOT NULL,
    Provincia CHAR(2) NOT NULL,
    
    -- Chiave primaria
    PRIMARY KEY (CodFiscale)
);

-- Tabella "Costruttore"
CREATE TABLE Costruttore (
    Codice CHAR(5),
    Nome VARCHAR(25) NOT NULL,
    
    -- Chiave primaria
    PRIMARY KEY (Codice)
);

-- Tabella "Modello"
CREATE TABLE Modello (
    Codice CHAR(5) NOT NULL,
    Nome VARCHAR(50) NOT NULL,
    Anno INT,
    -- Attributi per chiavi esterne
    CodiceCostruttore CHAR(5),
    
    -- Chiave primaria
    PRIMARY KEY (Codice),
    -- Chiavi esterne
    FOREIGN KEY (CodiceCostruttore) REFERENCES Costruttore(Codice)
);

-- Tabella "Auto"
CREATE TABLE Auto (
    Targa CHAR(7) NOT NULL,
    AnnoImmatricolazione INT NOT NULL,
    CavalliFiscali INT NOT NULL,
    Informazioni VARCHAR(50) NOT NULL,
    Tipo VARCHAR(10) NOT NULL,
    
    -- Attributi per chiavi esterne
    CodiceModello CHAR(5),
    CodFiscaleCliente CHAR(1),
    
    -- Chiave primaria
    PRIMARY KEY (Targa),
    -- Chiavi esterne
    FOREIGN KEY (CodiceModello) REFERENCES Modello(Codice),
    FOREIGN KEY (CodFiscaleCliente) REFERENCES Cliente(CodFiscale)
);

-- Tabella "Pezzo"
CREATE TABLE Pezzo (
    Codice CHAR(6) NOT NULL,
    Descrizione VARCHAR(50) NOT NULL,
    Prezzo DECIMAL(8,2) NOT NULL,
    Tipo INT NOT NULL,
    
    -- Chiave primaria
    PRIMARY KEY (Codice)
);

-- Tabella "Intervento"
CREATE TABLE Intervento (
    Codice CHAR(5) NOT NULL,
    Tipo VARCHAR(20) NOT NULL,
    Data DATE NOT NULL,
    Costo DECIMAL(8, 2) NOT NULL,
    -- Attributi per chiavi esterne
    Targa CHAR(7),
    
    -- Chiave primaria
    PRIMARY KEY (Codice),
    -- Chiavi esterne
    FOREIGN KEY (Targa) REFERENCES Auto(Targa)
);

-- Creo le tabelle per le relazioni N:M (Relazione N:M --> 3° Tabella)
-- Tabella "Utilizza"
CREATE TABLE Utilizza (
    CodiceIntervento CHAR(5),
    CodicePezzo CHAR(6),
    -- Altri attributi
    Quantita INT,
    
    -- Chiave primaria
    PRIMARY KEY (CodiceIntervento, CodicePezzo),
    -- Chiavi esterne
    FOREIGN KEY (CodiceIntervento) REFERENCES Intervento(Codice),
    FOREIGN KEY (CodicePezzo) REFERENCES Pezzo(Codice)
);

\! echo '\nTabelle create'
SHOW TABLES;

\! echo '\nTabella "Cliente"'
DESCRIBE Cliente;

\! echo '\nTabella "Costruttore"'
DESCRIBE Costruttore;

\! echo '\nTabella "Modello"'
DESCRIBE Modello;

\! echo '\nTabella "Auto"'
DESCRIBE Auto;

\! echo '\nTabella "Pezzo"'
DESCRIBE Pezzo;

\! echo '\nTabella "Intervento"'
DESCRIBE Intervento;

\! echo '\nTabella "Utilizza"'
DESCRIBE Utilizza;
