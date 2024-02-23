-- 5L Bracco Mattia

--DROP DATABASE Mercantile;

CREATE DATABASE IF NOT EXISTS Mercantile;
USE Mercantile;

-- Creo le tabelle...

-- Tabella Navi
CREATE TABLE Navi (
	CodiceNave INT NOT NULL AUTO_INCREMENT,
	NomeNave VARCHAR(25) NOT NULL,
	Stazza INT NOT NULL,
	Lunghezza INT NOT NULL,
	AnnoCostruzione DATE NOT NULL,
	PotenzaMotori INT NOT NULL,
	
	-- Chiave primaria
	PRIMARY KEY (CodiceNave)
);

-- Tabella Porti
CREATE TABLE Porti (
	CodicePorto INT NOT NULL AUTO_INCREMENT,
	NomePorto VARCHAR(25) NOT NULL,
	
	-- Chiave primaria
	PRIMARY KEY (CodicePorto)
);

-- Tabella Personale
CREATE TABLE Personale (
	CodiceFiscale CHAR(16) NOT NULL,
	NomePersonale VARCHAR(25) NOT NULL,
	CognomePersonale VARCHAR(25) NOT NULL,
	LuogoNascita VARCHAR(25) NOT NULL,
	DataNascita DATE NOT NULL,
	
	-- Chiave primaria
	PRIMARY KEY (CodiceFiscale)
);

-- Tabella Viaggi
CREATE TABLE Viaggi (
	ID_Viaggio INT NOT NULL AUTO_INCREMENT,
	DataPartenza DATE NOT NULL,
	OraPartenza DATE NOT NULL,
	DataArrivo DATE NOT NULL,
	OraArrivo DATE NOT NULL,
	PesoTotale INT NOT NULL,
	-- Attrivuti per chiavi esterne
	CodiceNave INT NOT NULL,
	CodicePortoPartenza INT NOT NULL,
	CodicePortoArrivo INT NOT NULL,	
	
	-- Chiave primaria
	PRIMARY KEY (ID_Viaggio),
	-- Chiavi esterne
	FOREIGN KEY (CodiceNave) REFERENCES Navi (CodiceNave),
	FOREIGN KEY (CodicePortoPartenza) REFERENCES Porti (CodicePorto),
	FOREIGN KEY (CodicePortoArrivo) REFERENCES Porti (CodicePorto)
);

-- Tabella Messaggi
CREATE TABLE Messaggi (
	ID_Messaggio INT NOT NULL AUTO_INCREMENT,
	Latitudine INT NOT NULL,
	Longitudine INT NOT NULL,
	Direzione CHAR(4) NOT NULL,
	Velocita INT NOT NULL,
	DataMessaggio DATE NOT NULL,
	OraMessaggio DATE NOT NULL,
	NoteCapitano VARCHAR(50),
	-- Attributi per chiavi esterne
	ID_Viaggio INT NOT NULL,
	
	-- Chiave primaria
	PRIMARY KEY (ID_Messaggio),
	-- Chiave esterna
	FOREIGN KEY (ID_Viaggio) REFERENCES Viaggi (ID_Viaggio)
);

-- Tabelle per le relazioni N:M (N:M --> 3° Tabella)

-- Tabella Presente
CREATE TABLE Presente (
	CodiceFiscale CHAR(16) NOT NULL,
	ID_Viaggio INT NOT NULL,
	-- Altri attributi
	Ruolo VARCHAR(10) NOT NULL,
	
	-- Chiave primaria
	PRIMARY KEY (CodiceFiscale, ID_Viaggio),
	-- Chiavi esterne
	FOREIGN KEY (CodiceFiscale) REFERENCES Personale (CodiceFiscale),
	FOREIGN KEY (ID_Viaggio) REFERENCES Viaggi (ID_Viaggio)
);

\! echo '\nTabelle create'
show tables;

\! echo '\nTabella "Navi"'
DESCRIBE Navi;

\! echo '\nTabella "Porti"'
DESCRIBE Porti;

\! echo '\nTabella "Personale"'
DESCRIBE Personale;

\! echo '\nTabella "Viaggi"'
DESCRIBE Viaggi;

\! echo '\nTabella "Messaggi"'
DESCRIBE Messaggi;

\! echo '\nTabella "Presente"'
DESCRIBE Presente;
