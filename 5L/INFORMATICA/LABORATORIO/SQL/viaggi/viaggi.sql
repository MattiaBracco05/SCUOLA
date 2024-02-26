-- 5L Bracco Mattia

-- DROP DATABASE Viaggi;

-- Creo il database e lo imposto per utilizzarlo
CREATE DATABASE IF NOT EXISTS Viaggi;
USE Viaggi;

-- Creo le tabelle...
-- Tabella Destnazione
CREATE TABLE IF NOT EXISTS Destinazione (
    CodDest CHAR(3) NOT NULL,
    Denominazione VARCHAR(25) NOT NULL,
    Moneta VARCHAR(25) NOT NULL,
    
    -- Chiave primaria
    PRIMARY KEY (CodDest) 
);

-- Tabella Cliente
CREATE TABLE IF NOT EXISTS Cliente (
    CodCli CHAR(3) NOT NULL,
    CognomeCli VARCHAR(25) NOT NULL,
    NomeCli VARCHAR(25) NOT NULL,
    IndirizzoCli VARCHAR(25) NOT NULL,
    TelCli CHAR(10) NOT NULL,
    
    -- Chiave primaria
    PRIMARY KEY (CodCli)
);

-- Tabella TourOperator
CREATE TABLE IF NOT EXISTS TourOperator (
    CodTour CHAR(3) NOT NULL,
    NomeTour VARCHAR(25) NOT NULL,
    IndirizzoTour VARCHAR(25) NOT NULL,
    TelTour CHAR(10) NOT NULL,
    
    -- Chiave primaria
    PRIMARY KEY (CodTour)
);

-- Tabella Pacchetti
CREATE TABLE IF NOT EXISTS Pacchetti (
    CodPacch CHAR(3) NOT NULL,
    Modalita VARCHAR(25) NOT NULL,
    Prezzo INT NOT NULL,
    -- Attributi per chiavi esterne
    CodDest VARCHAR(4) NOT NULL,
    CodTour VARCHAR(4) NOT NULL,
   
    -- Chiave primaria
    PRIMARY KEY (CodPacch),
    
    -- Chiavi esterne
    FOREIGN KEY (CodDest) REFERENCES Destinazione(CodDest),
    FOREIGN KEY (CodTour) REFERENCES TourOperator(CodTour)
);

-- Creo le tabelle per le relazioni N:M --> (relazione N:M --> 3° tabella)
-- Tabella Acquisti
CREATE TABLE IF NOT EXISTS Acquisti (
    CodCli CHAR(3) NOT NULL,
    CodPacch CHAR(3) NOT NULL,
    -- Altri attributi
    CodAcq CHAR(3) NOT NULL,
    DataAcquisto DATE NOT NULL,
    
    -- Chiave primaria
    PRIMARY KEY (CodAcq),
    -- Chiavi esterne
    FOREIGN KEY (CodCli) REFERENCES Cliente (CodCli),
    FOREIGN KEY (CodPacch) REFERENCES Pacchetti (CodPacch)
);

\! echo '\nTabelle create'
show tables;

\! echo '\nTabella "Destinazione"'
DESCRIBE Destinazione;

\! echo '\nTabella "Cliente"'
DESCRIBE Cliente;

\! echo '\nTabella "TourOperator"'
DESCRIBE TourOperator;

\! echo '\nTabella "Pacchetti"'
DESCRIBE Pacchetti;

\! echo '\nTabella "Acquisti"'
DESCRIBE Acquisti;
