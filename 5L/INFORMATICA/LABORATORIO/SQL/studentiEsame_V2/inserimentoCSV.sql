-- 5L Bracco Mattia

-- Seleziono il DB
USE EsamiStudenti

-- Carico i dati nella tabella "Esami"
LOAD DATA INFILE '/tmp/CSV/EsamiStudenti/Esami.csv'
INTO TABLE Esami FIELDS TERMINATED BY ',' IGNORE 1 LINES (ID_Esame, NomeEsame, Crediti, Aula, Orario);

-- Carico i dati nella tabella "Studenti"
LOAD DATA INFILE '/tmp/CSV/EsamiStudenti/Studenti.csv'
INTO TABLE Studenti FIELDS TERMINATED BY ',' ENCLOSED BY '"' IGNORE 1 LINES (ID_Studente, Cognome, Nome, DataNascita, Indirizzo, CorsoLaurea, ID_Esame);
