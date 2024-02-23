-- 5L Bracco Mattia

--DROP database merendine;

CREATE DATABASE IF NOT EXISTS merendine;
USE merendine;

-- Creo le tabelle...

-- Tabella Merende
CREATE TABLE IF NOT EXISTS Merende (
	CodMerenda VARCHAR(10) NOT NULL,
	NomeMerenda VARCHAR(25) NOT NULL,
	Prezzo FLOAT NOT NULL,
	
	-- Chiave primaria
	PRIMARY KEY (CodMerenda)
);

-- Tabella Scuole
CREATE TABLE IF NOT EXISTS Scuole (
	CodScuola VARCHAR(10) NOT NULL,
	NomeScuola VARCHAR(25) NOT NULL,

	-- Chiave primaria
	PRIMARY KEY (CodScuola)
);

-- Tabella Macchinette
CREATE TABLE IF NOT EXISTS Macchinette (
	CodMacchinetta VARCHAR(10) NOT NULL,
	TipoMacchinetta VARCHAR(10) NOT NULL,
	-- Attributi per chiavi esterne
	CodScuola VARCHAR(10) NOT NULL,
	
	-- Chiave primaria
	PRIMARY KEY (CodMacchinetta),
	-- Chiave esterna
	FOREIGN KEY (CodScuola) REFERENCES Scuole (CodScuola)  
);

-- Tabelle per le relazioni N:M --> (relazione N:M --> 3° tabella)
-- Tabella Posizioni
CREATE TABLE IF NOT EXISTS Posizioni (
	-- Altri attributi
	CodPos VARCHAR(10) NOT NULL,
	QtaMerendine INT NOT NULL,
	-- Attributi per chiavi esterne
	CodMerenda VARCHAR(10) NOT NULL,
	CodMacchinetta VARCHAR(10) NOT NULL,
	
	-- Chiave primaria
	PRIMARY KEY (CodPos),
	-- Chiavi esterne
	FOREIGN KEY (CodMerenda) REFERENCES Merende (CodMerenda),
	FOREIGN KEY (CodMacchinetta) REFERENCES Macchinette (CodMacchinetta)
);

\! echo '\nTabelle create'
show tables;

\! echo '\nTabella "Merende"'
DESCRIBE Merende;

\! echo '\nTabella "Scuole"'
DESCRIBE Scuole;

\! echo '\nTabella "Macchinette"'
DESCRIBE Macchinette;

\! echo '\nTabella "Posizioni"'
DESCRIBE Posizioni;
