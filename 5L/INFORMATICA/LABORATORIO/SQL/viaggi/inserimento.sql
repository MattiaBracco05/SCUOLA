-- 5L Bracco Mattia

-- Seleziono il database da utilizzare
USE Viaggi;

-- Inserisco i dati nella tabella "Destinazione"
INSERT IGNORE INTO Destinazione (CodDest, Denominazione, Moneta) VALUES
('111', 'Malaga', 'Euro'),
('112', 'New York', 'Dollaro'),
('113', 'Parigi', 'Euro'),
('114', 'Pechino', 'Yen');

-- Inserisco i dati nella tabella "Cliente"
INSERT IGNORE INTO Cliente (CodCli, CognomeCli, NomeCli, IndirizzoCli, TelCli) VALUES
('222', 'Rossi', 'Mario', 'AAA', '123'),
('223', 'Rosso', 'Antonio', 'BBB', '345'),
('224', 'Bianchi', 'Mario', 'CCC', '567'),
('225', 'Beltramo', 'Dario', 'DDD', '789');

-- Inserisco i dati nella tabella "Tour Operator"
INSERT IGNORE INTO TourOperator (CodTour, NomeTour, IndirizzoTour, TelTour) VALUES
('333', 'Alpitour', 'AAA', '011147890'),
('334', 'Francorosso', 'BBB', '017278963'),
('335', 'Viaggi Il Gabbiano', 'CCC', '017469852');

-- Inserisco i dati nella tabella "Pacchetti"
REPLACE INTO Pacchetti (CodPacch, Modalita, Prezzo, CodDest, CodTour) VALUES
('444', 'Mezza pensione', 1800, '111', '333'),
('445', 'Mezza pensione', 1200, '111', '333'),
('446', 'Pensione completa', 2800, '112', '334'),
('447', 'Pensione completa', 2900, '112', '333'),
('448', 'All-inclusive', 4800, '114', '335'),
('449', 'All-inclusive', 2990, '112', '335'),
('450', 'All-inclusive', 990, '113', '335'),
('451', 'All-inclusive', 995, '111', '335');

-- Inserisco i dati nella tabella "Acquisti"
INSERT IGNORE INTO Acquisti (CodAcq, CodCli, CodPacch, DataAcquisto) VALUES
('555', '222', '444', '2018-10-12'),
('556', '222', '445', '2018-12-12'),
('557', '222', '446', '2018-11-12'),
('558', '222', '447', '2018-10-12'),
('559', '223', '444', '2018-10-15'),
('560', '224', '445', '2018-10-18'),
('561', '224', '448', '2018-10-20'),
('562', '224', '449', '2018-10-15'),
('563', '223', '448', '2018-10-02'),
('564', '224', '450', '2018-12-12');
