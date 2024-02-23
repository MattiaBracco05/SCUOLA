-- %L Bracco Mattia

-- Seleziono il database da utilizzare
USE merendine;

INSERT INTO Merende (CodMerenda, NomeMerenda, Prezzo) VALUES ("Kin01", "Kinder Bueno", 2.5);
INSERT INTO Merende (CodMerenda, NomeMerenda, Prezzo) VALUES ("Kin02", "Kinder Maxi", 1.5);

INSERT INTO Scuole (CodScuola, NomeScuola) VALUES ("AA001", "Rivoira");
INSERT INTO Scuole (CodScuola, NomeScuola) VALUES ("AA002", "Denina");
INSERT INTO Scuole (CodScuola, NomeScuola) VALUES ("AA003", "Pellico");

INSERT INTO Macchinette (CodMacchinetta, TipoMacchinetta, CodScuola) VALUES ("Dist01", "Distr", "AA001");
INSERT INTO Macchinette (CodMacchinetta, TipoMacchinetta, CodScuola) VALUES ("Dist02", "Distr", "AA002");

INSERT INTO Posizioni (CodPos, QtaMerendine, CodMerenda, CodMacchinetta) VALUES ("Pos01", 10, "Kin01", "Dist01");
INSERT INTO Posizioni (CodPos, QtaMerendine, CodMerenda, CodMacchinetta) VALUES ("Pos02", 20, "Kin02", "Dist02");

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
