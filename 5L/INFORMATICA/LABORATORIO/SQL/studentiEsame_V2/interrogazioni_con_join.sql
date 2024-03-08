-- 5L Bracco Mattia

-- Seleziono il database da utilizzare
USE EsamiStudenti;

-- (1)
SELECT Cognome, Nome, NomeEsame
FROM Studenti, Esami
WHERE Esami.ID_Esame = Studenti.ID_Esame AND (NomeEsame = 'Sistemi Operativi' OR NomeEsame = 'Impianti Elettrici');

-- (2)
SELECT Cognome, Nome, NomeEsame, Crediti
FROM Studenti, Esami
WHERE Esami.ID_Esame = Studenti.ID_ESAME AND CorsoLaurea = 'Medicina';

-- (3)
SELECT Cognome, Nome, NomeEsame, Crediti
FROM Studenti, Esami
WHERE Esami.ID_Esame = Studenti.ID_Esame AND Crediti >= 7 AND Crediti<= 9; 
