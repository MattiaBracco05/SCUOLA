-- 5L Bracco Mattia

--DROP database concerti;

CREATE DATABASE IF NOT EXISTS concerti;
USE concerti;

-- Creo le tabelle...

-- Tabella DIRETTORI
CREATE TABLE DIRETTORI (
    CF VARCHAR(16) NOT NULL,
    Nome VARCHAR(25) NOT NULL,
    Cognome VARCHAR(25) NOT NULL,
    
    -- Chiave primaria
    PRIMARY KEY (CF)
);

-- Tabella ORCHESTRE
CREATE TABLE ORCHESTRE (
    NomeOrchestra VARCHAR(25) NOT NULL,
    Città VARCHAR(25) NOT NULL,
    -- Attributi per chiavi esterne
    CF_Direttore VARCHAR(16) NOT NULL,
    
    -- Chiave primaria
    PRIMARY KEY (NomeOrchestra),
    -- Chiavi esterne
    FOREIGN KEY (CF_Direttore) REFERENCES DIRETTORI(CF)
);

-- Tabella ORCHESTRALI
CREATE TABLE ORCHESTRALI (
    NumMatricola INT NOT NULL,
    Nome VARCHAR(25) NOT NULL,
    Cognome VARCHAR(25) NOT NULL,
    
    -- Chiave primaria
    PRIMARY KEY (NumMatricola)
);

-- Tabella STRUMENTI
CREATE TABLE STRUMENTI (
    ID_Strumento INT NOT NULL,
    Nome VARCHAR(25) NOT NULL,
    -- Attributi per chiavi esterne
    NumMatricola INT NOT NULL,
    
    -- Chiave primaria
    PRIMARY KEY (ID_Strumento),
    -- Chiavi esterne
    FOREIGN KEY (NumMatricola) REFERENCES ORCHESTRALI(NumMatricola)
);

-- Tabella SALE
CREATE TABLE SALE (
    ID_Sala INT NOT NULL,
    Nome VARCHAR(25) NOT NULL,
    Capienza INT NOT NULL,
    
    -- Chiave primaria
    PRIMARY KEY (ID_Sala)
);

-- Tabella CONCERTI
CREATE TABLE CONCERTI (
    ID_Concerto INT NOT NULL,
    Descrizione VARCHAR(100) NOT NULL,
    Titolo VARCHAR(25) NOT NULL,
    -- Attributi per chiavi esterne
    NomeOrchestra VARCHAR(25) NOT NULL,
    
    -- Chiave primaria
    PRIMARY KEY (ID_Concerto),
    -- Chiavi esterne
    FOREIGN KEY (NomeOrchestra) REFERENCES ORCHESTRE(NomeOrchestra)
);

-- Tabella PEZZI
CREATE TABLE PEZZI (
    ID_Pezzo INT NOT NULL,
    Titolo VARCHAR(25) NOT NULL,
    Durata INT NOT NULL,
    
    -- Chiave primaria
    PRIMARY KEY (ID_Pezzo)
);

-- Tabella AUTORI
CREATE TABLE AUTORI (
    ID_Autore INT NOT NULL,
    Nome VARCHAR(25) NOT NULL,
    
    -- Chiave primaria
    PRIMARY KEY (ID_Autore)
);

-- Tabelle per le relazioni N:M (N:M --> 3° tabella)
-- Tabella TENUTO
CREATE TABLE TENUTO (
    ID_Concerto INT NOT NULL,
    ID_Sala INT NOT NULL,
    -- Altri attributi
    DataEsibizione INT NOT NULL,
    
    -- Chiave primaria
    PRIMARY KEY (ID_Concerto, ID_Sala),
    -- Chiavi esterne
    FOREIGN KEY (ID_Concerto) REFERENCES CONCERTI(ID_Concerto),
    FOREIGN KEY (ID_Sala) REFERENCES SALE(ID_Sala)
);

-- Tabella COMPOSTA
CREATE TABLE COMPOSTA (
    NomeOrchestra VARCHAR(25) NOT NULL,
    NumMatricola INT NOT NULL,
    
    -- Chiave primaria
    PRIMARY KEY (NomeOrchestra, NumMatricola),
    -- Chiavi esterne
    FOREIGN KEY (NomeOrchestra) REFERENCES ORCHESTRE(NomeOrchestra),
    FOREIGN KEY (NumMatricola) REFERENCES ORCHESTRALI(NumMatricola)
);

-- Tabella RAPPRESENTA
CREATE TABLE RAPPRESENTA (
    ID_Concerto INT NOT NULL,
    ID_Pezzo INT NOT NULL,
    
    -- Chiave primaria
    PRIMARY KEY (ID_Concerto, ID_Pezzo),
    -- Chiavi esterne
    FOREIGN KEY (ID_Concerto) REFERENCES CONCERTI(ID_Concerto),
    FOREIGN KEY (ID_Pezzo) REFERENCES PEZZI(ID_Pezzo)
);

-- Tabella SCRIVE
CREATE TABLE SCRIVE (
    ID_Pezzo INT NOT NULL,
    ID_Autore INT NOT NULL,
    
    -- Chiave primaria
    PRIMARY KEY (ID_Pezzo, ID_Autore),
    -- Chiavi esterne
    FOREIGN KEY (ID_Pezzo) REFERENCES PEZZI(ID_Pezzo),
    FOREIGN KEY (ID_Autore) REFERENCES AUTORI(ID_Autore)
);

\! echo '\nTabelle create'
show tables;

\! echo '\nTabella "DIRETTORI"'
DESCRIBE DIRETTORI;

\! echo '\nTabella "ORCHESTRE"'
DESCRIBE ORCHESTRE;

\! echo '\nTabella "ORCHESTRALI"'
DESCRIBE ORCHESTRALI;

\! echo '\nTabella "STRUMENTI"'
DESCRIBE STRUMENTI;

\! echo '\nTabella "SALE"'
DESCRIBE SALE;

\! echo '\nTabella "CONCERTI"'
DESCRIBE CONCERTI;

\! echo '\nTabella "PEZZI"'
DESCRIBE PEZZI;

\! echo '\nTabella "AUTORI"'
DESCRIBE AUTORI;

\! echo '\nTabella "TENUTO"'
DESCRIBE TENUTO;

\! echo '\nTabella "COMPOSTA"'
DESCRIBE COMPOSTA;

\! echo '\nTabella "RAPPRESENTA"'
DESCRIBE RAPPRESENTA;

\! echo '\nTabella "SCRIVE"'
DESCRIBE SCRIVE;


