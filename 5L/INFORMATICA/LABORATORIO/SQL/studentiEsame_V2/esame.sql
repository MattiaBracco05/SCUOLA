-- 5L Bracco Mattia

-- DROP DATABASE IF EXISTS EsamiStudenti;

-- Creo il DB
CREATE DATABASE IF NOT EXISTS EsamiStudenti;
-- Seleziono il DB
USE EsamiStudenti;

-- Tabella "Esami"
CREATE TABLE IF NOT EXISTS Esami (
	ID_Esame INT NOT NULL AUTO_INCREMENT,
	NomeEsame VARCHAR(40) NOT NULL,
	Crediti INT(2) NOT NULL,
	Aula VARCHAR(40) NOT NULL,
	Orario VARCHAR(40) NOT NULL,
	
	-- Chiave primaria
	PRIMARY KEY (ID_Esame)
);

-- Tabella "Studenti"
CREATE TABLE IF NOT EXISTS Studenti (
	ID_Studente INT NOT NULL,
	Nome VARCHAR(40) NOT NULL,
	Cognome VARCHAR(40) NOT NULL,
	DataNascita DATE NOT NULL,
	Indirizzo VARCHAR(40) NOT NULL,
	CorsoLaurea VARCHAR(40) NOT NULL,
	-- Attributi per chiavi esterne
	ID_Esame INT NOT NULL,

	
	-- Chiave primaria
	PRIMARY KEY (ID_Studente),
	-- Chiavi estere
	FOREIGN KEY (ID_Esame) REFERENCES Esami(ID_Esame) ON DELETE CASCADE
);

\! echo '\nTabelle create'
SHOW TABLES;

\! echo '\nTabella "Esami"'
DESCRIBE Esami;

\! echo '\nTabella "Studenti"'
DESCRIBE Studenti;
