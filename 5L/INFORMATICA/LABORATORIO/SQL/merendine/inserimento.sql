-- %L Bracco Mattia

-- Seleziono il database da utilizzare
USE merendine;

INSERT INTO Merende VALUES ("Kin01", "Kinder Bueno", 2.5);
INSERT INTO Merende VALUES ("Kin02", "Kinder Maxi", 1.5);

INSERT INTO Scuole VALUES ("AA001", "Rivoira");
INSERT INTO Scuole VALUES ("AA002", "Denina");
INSERT INTO Scuole VALUES ("AA003", "Pellico");

INSERT INTO Macchinette VALUES ("Dist01", "Distr", "AA001");
INSERT INTO Macchinette VALUES ("Dist02", "Distr", "AA002");

INSERT INTO Posizioni VALUES ("Pos01", 10, "Kin01", "Dist01");
INSERT INTO Posizioni VALUES ("Pos02", 20, "Kin02", "Dist02");

\! echo '\nTabelle create'
SHOW tables;

\! echo '\nDati inseriti nella tabella "Merende"'
SELECT * FROM Merende;

\! echo '\nDati inseriti nella tabella "Scuole"'
SELECT * FROM Scuole;

\! echo '\nDati inseriti nella tabella "Macchinette"'
SELECT * FROM Macchinette;

\! echo '\nDati inseriti nella tabella "Posizioni"'
SELECT * FROM Posizioni;
