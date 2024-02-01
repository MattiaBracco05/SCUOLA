-- 5L Bracco Mattia

--DROP database mostraCanina;

CREATE DATABASE IF NOT EXISTS mostraCanina;
USE mostraCanina;

-- Creazione della tabella Cani
CREATE TABLE Cani (
    ID_cane INT PRIMARY KEY,
    Nome VARCHAR(50) NOT NULL,
    Peso FLOAT NOT NULL,
    Altezza FLOAT NOT NULL,
    DataDiNascita DATE NOT NULL,
    NomeRazza VARCHAR(50) NOT NULL
);

-- Creazione della tabella Razze
CREATE TABLE Razze (
    NomeRazza VARCHAR(50) PRIMARY KEY,
    PesoStandard FLOAT NOT NULL,
    AltezzaStandard FLOAT NOT NULL
);

-- Creazione della tabella Giudici
CREATE TABLE Giudici (
    ID_giudice INT PRIMARY KEY
);

-- Creazione della tabella Padroni
CREATE TABLE Padroni (
    CF VARCHAR(16) PRIMARY KEY,
    NomePadrone VARCHAR(50) NOT NULL,
    CognomePadrone VARCHAR(50) NOT NULL
);

-- Creazione della tabella Giudica
CREATE TABLE Giudica (
    ID_cane INT,
    ID_giudice INT,
    Voto FLOAT NOT NULL,
    PRIMARY KEY (ID_cane, ID_giudice)
);

\! echo '\nTabelle create'
show tables

\! echo '\nTabella "Cani"'
DESCRIBE Cani;

\! echo '\nTabella "Razze"'
DESCRIBE Razze;

\! echo '\nTabella "Padroni"'
DESCRIBE Padroni;

\! echo '\nTabella "Giudici"'
DESCRIBE Giudici;

\! echo '\nTabella "Giudica" (relazione tra "Giudici" e "Cani")'
DESCRIBE Giudica;
