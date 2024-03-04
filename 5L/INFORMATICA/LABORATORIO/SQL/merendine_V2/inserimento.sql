-- 5L Bracco Mattia

-- Seleziono il database da utilizzare
USE merendineV2;

-- Inserimento dei dati nella tabella Scuole
LOAD DATA LOCAL INFILE './dati.csv'
INTO TABLE Scuole
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(CodScuola, NomeScuola);

-- Inserimento dei dati nella tabella Merende
LOAD DATA LOCAL INFILE './dati.csv'
INTO TABLE Merende
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(CodMerenda, NomeMerenda, Prezzo);

-- Inserimento dei dati nella tabella Macchinette
LOAD DATA LOCAL INFILE './dati.csv'
INTO TABLE Macchinette
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(CodMacchinetta, TipoMacchinetta, CodScuola);

-- Inserimento dei dati nella tabella Posizioni
LOAD DATA LOCAL INFILE './dati.csv'
INTO TABLE Posizioni
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(CodPos, QtaMerendine, CodMerenda, CodMacchinetta);
