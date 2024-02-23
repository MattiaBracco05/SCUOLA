-- 5L Bracco Mattia

--DROP database officine;

CREATE DATABASE IF NOT EXISTS officine;
USE officine;

-- Creo le tabelle...

-- Tabella Proprietario
CREATE TABLE Proprietario (
    CFP CHAR(16) NOT NULL,
    nomeP VARCHAR(25) NOT NULL,
    cognP VARCHAR(25) NOT NULL,
    indP VARCHAR(50) NOT NULL,
    telefP CHAR(10) NOT NULL,
    
    -- Chiave primaria
    PRIMARY KEY (CFP)
);

-- Tabella Veicolo
CREATE TABLE Veicolo (
    targaV CHAR(7) NOT NULL,
    modelloV VARCHAR(25) NOT NULL,
    tipoV VARCHAR(25) NOT NULL,
    immatricV DATE NOT NULL,
    -- Attributi per chiavi esterne
    CFP CHAR(16) NOT NULL,
    
    -- Chiave primaria
    PRIMARY KEY (targaV),
    -- Chiavi esterne
    FOREIGN KEY (CFP) REFERENCES Proprietario (CFP)
);

-- Tabella Officina
CREATE TABLE Officina (
    nomeO VARCHAR(25) NOT NULL,
    indO VARCHAR(25) NOT NULL,
    Ndip INT NOT NULL,
    
    -- Chiave primaria
    PRIMARY KEY (nomeO, indO)
);

-- Tabella Dipendente
CREATE TABLE Dipendente (
    CFD CHAR(16) NOT NULL,
    nomeD VARCHAR(25) NOT NULL,
    cognD VARCHAR(25) NOT NULL,
    indD VARCHAR(25) NOT NULL,
    telD CHAR(10) NOT NULL,
    
    -- Chiave primaria
    PRIMARY KEY (CFD)
);

-- Tabella Ripara
CREATE TABLE Ripara (
    IDrip INT NOT NULL AUTO_INCREMENT,
    data DATE NOT NULL,
    ora TIME NOT NULL,
    codice INT NOT NULL,
    -- Attributi per chiavi esterne
    nomeO VARCHAR(25) NOT NULL,
	indO VARCHAR(25) NOT NULL,
    targaV CHAR(7) NOT NULL,
    
    -- Chiave primaria
    PRIMARY KEY (IDrip),
    -- Chiavi esterne
    FOREIGN KEY (nomeO, indO) REFERENCES Officina (nomeO, indO),
    FOREIGN KEY (targaV) REFERENCES Veicolo (targaV)
);

-- Tabella Dirige
CREATE TABLE Dirige (
    DataI DATE,
    DataF DATE,
    -- Attributi per chiavi esterne
    nomeO VARCHAR(25),
    indO VARCHAR(25),
    CFD CHAR(16),
    
    -- Chiave primaria
    PRIMARY KEY (nomeO, indO, CFD),
    -- Chiavi esterne
    FOREIGN KEY (nomeO, indO) REFERENCES Officina (nomeO, indO),
    FOREIGN KEY (CFD) REFERENCES Dipendente (CFD)
);

-- Tabella Lavora
CREATE TABLE Lavora (
    DataI DATE,
    DataF DATE,
    -- Attributi per chiavi esterne
    nomeO VARCHAR(25),
    indO VARCHAR(25),
    CFD CHAR(16),
    
    -- Chiave primaria
    PRIMARY KEY (nomeO, indO, CFD),
    -- Chiavi esterne
    FOREIGN KEY (nomeO, indO) REFERENCES Officina (nomeO, indO),
    FOREIGN KEY (CFD) REFERENCES Dipendente (CFD)
);


\! echo '\nTabelle create'
show tables;

\! echo '\nTabella "Proprietario"'
DESCRIBE Proprietario;

\! echo '\nTabella "Veicolo"'
DESCRIBE Veicolo;

\! echo '\nTabella "Officina"'
DESCRIBE Officina;

\! echo '\nTabella "Dipendente"'
DESCRIBE Dipendente;

\! echo '\nTabella "Ripara"'
DESCRIBE Ripara;

\! echo '\nTabella "Dirige"'
DESCRIBE Dirige;

\! echo '\nTabella "Lavora"'
DESCRIBE Lavora;


