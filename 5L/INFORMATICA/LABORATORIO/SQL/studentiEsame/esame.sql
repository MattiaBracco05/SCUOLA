-- 5L Bracco Mattia

DROP DATABASE EsamiStudenti;

-- Creo il database e lo imposto per utilizzarlo
CREATE DATABASE IF NOT EXISTS EsamiStudenti;
USE EsamiStudenti;

-- Creo le tabelle...
-- Tabella Esami
CREATE TABLE IF NOT EXISTS Esami (
	ID_Esame INT NOT NULL,
	NomeEsame VARCHAR(25) NOT NULL,
	Crediti INT NOT NULL,
	Aula VARCHAR(25) NOT NULL,
	Orario VARCHAR(25) NOT NULL,
	
	-- Chiave primaria
	PRIMARY KEY (ID_Esame)
);

-- Tabella Studenti
CREATE TABLE IF NOT EXISTS Studenti (
	ID_Studente INT NOT NULL,
	Cognome VARCHAR(25) NOT NULL,
	Nome VARCHAR(25) NOT NULL,
	DataNascita DATE NOT NULL,
	Indirizzo VARCHAR(25) NOT NULL,
	CorsoLaurea VARCHAR(25) NOT NULL,
	-- Attributi per chiavi esterne
	ID_Esame INT NOT NULL,
	
	-- Chiave primaria
	PRIMARY KEY (ID_Studente),
	-- Chiavi esterne
	FOREIGN KEY (ID_Esame) REFERENCES Esami (ID_Esame)
);

\! echo '\nTabelle create'
SHOW TABLES;

\! echo '\nTabella "Esami"'
DESCRIBE Esami;

\! echo '\nTabella "Studenti"'
DESCRIBE Studenti;
