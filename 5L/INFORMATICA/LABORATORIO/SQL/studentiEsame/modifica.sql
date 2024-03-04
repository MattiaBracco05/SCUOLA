-- 5L Bracco Mattia

-- Seleziono il database da utilizzare
USE EsamiStudenti;

-- INSERIMENTO DEI DATI

-- Inserisco un nuovo record nella tabella "Esami" collegato ad "Analisi" con 15 crediti
INSERT INTO Esami (ID_Esame, NomeEsame, Crediti, Aula, Orario) VALUES (6, 'Analisi', 15, 'Aula 101', '08:00-10:00');

-- Inserisco un nuovo record nella tabella "Studenti" collegato all'esame di "Analisi"
INSERT INTO Studenti (ID_Studente, Cognome, Nome, DataNascita, Indirizzo, CorsoLaurea, ID_Esame) VALUES (10, 'Rossi', 'Mario', '2000-05-15', 'Via Roma 123', 'Ingegneria Informatica', 6);

/*
Modifico i crediti per l'esame di "Analisi" nella tabella "Esami" usando "ON DUPLICATE KEY UPDATE"
Se un record con lo stesso "ID_Esame" esiste già --> i crediti vengono aggiornati a "15"
Altrimenti --> viene inserito un nuovo record.
*/
INSERT INTO Esami (ID_Esame, NomeEsame, Crediti, Aula, Orario) VALUES (6, 'Analisi', 15, 'Aula 101', '08:00-10:00') ON DUPLICATE KEY UPDATE Crediti = VALUES(Crediti);

/*
Modifico i dati dello studente con "ID_Studente=6" utilizzando "REPLACE"
Se uno studente con lo stesso "ID_Studente" esiste già --> il suo record viene sostituito con quello nuovo
Altrimenti --> viene inserito un nuovo record con l' "ID_Studente" specificato.
*/
REPLACE INTO Studenti (ID_Studente, Cognome, Nome, DataNascita, Indirizzo, CorsoLaurea, ID_Esame) VALUES (6, 'Bianchi', 'Luigi', '2001-03-20', 'Via Milano 456', 'Ingegneria Civile', 3);

-- MODIFICA DEI DATI

-- Modifico il cognome di "Verdoni Carlo" in "Marroni"
UPDATE Studenti SET Cognome = 'Marroni' WHERE Cognome = 'Verdoni' AND Nome = 'Carlo';

-- Modifico tutti i record del corso di Laurea in "Medicina" nella tabella "Studenti", impostando "ID_Esame=2"
UPDATE Studenti SET ID_Esame = 2 WHERE CorsoLaurea = 'Medicina';

-- Modifico l’orario del corso di "Impianti Elettrici" nella tabella "Esami", sostituendolo con "Mar-Gio 08-10"
UPDATE Esami SET Orario = 'Mar-Gio 08-10' WHERE NomeEsame = 'Impianti Elettrici';

-- Incremento i crediti di "Sistemi Operativi" di "2" utilizzando il comando "UPDATE"
UPDATE Esami SET Crediti = Crediti + 2 WHERE NomeEsame = 'Sistemi Operativi';

-- Modifico il record dello studente "5" inserendo gli stessi valori
REPLACE INTO Studenti (ID_Studente, Cognome, Nome, DataNascita, Indirizzo, CorsoLaurea, ID_Esame)  VALUES (5, 'Rossi', 'Mario', '2000-05-15', 'Via Roma 123', 'Ingegneria Informatica', 3);

-- STAMPO LE TABELLE AGGIORNATE
\! echo '\nTabelle aggiornate dopo inserimento dei dati'
SHOW TABLES;

\! echo '\nTabella "Esami" aggiornata'
DESCRIBE Esami;

\! echo '\nTabella "Studenti" aggiornata'
DESCRIBE Studenti;

\! echo '\nDati inseriti nella tbella "Esami"'
SELECT * FROM Esami;

\! echo '\nDati inseriti nella tabella "Studenti"'
SELECT * FROM Studenti;
