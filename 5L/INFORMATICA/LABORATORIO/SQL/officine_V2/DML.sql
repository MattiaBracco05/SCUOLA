-- 5L Bracco Mattia

-- Seleziono il DB
USE Officina;

-- Inserisco i dati nella tabella "Cliente"
INSERT INTO Cliente VALUES('a','Mario','Rossi','Roma',12,12021,'Saluzzo','CN');
INSERT INTO Cliente VALUES('b','Luca','Bianchi','Antica',7,12190,'Verzuolo','CN');
INSERT INTO Cliente VALUES('c','Marco','Verdi','Provinciale',30,12922,'Pinerolo','TO');
INSERT INTO Cliente VALUES('d','Tommaso','Besso','Copernico',10,13912,'Pinerolo','TO');
INSERT INTO Cliente VALUES('e','Marta','Macari','Luglio',22,12021,'Saluzzo','CN');
INSERT INTO Cliente VALUES('f','Giada','Gossa','XXV Aprile',34,12100,'Cuneo','CN');
INSERT INTO Cliente VALUES('g','Andrea','Fabrizi','Roma',33,12100,'Cuneo','CN');
INSERT INTO Cliente VALUES('h','Marilena','Consiglio','Provinciale',20,12190,'Verzuolo','CN');
INSERT INTO Cliente VALUES('i','Alessio','Giannelli','Dante',44,13912,'Pinerolo','TO');
INSERT INTO Cliente VALUES('l','Mario','Rosso','Roma',14,12021,'Saluzzo','CN');

-- Inserisco i dati nella tabella "Costruttore"
INSERT INTO Costruttore VALUES('Cost1','Fiat');
INSERT INTO Costruttore VALUES('Cost2','Renault');
INSERT INTO Costruttore VALUES('Cost3','Ford');
INSERT INTO Costruttore VALUES('Cost4','Citroen');
INSERT INTO Costruttore VALUES('Cost5','Dacia');
INSERT INTO Costruttore VALUES('Cost6','Nissan');

-- Inserisco i dati nella tabella "Modello"
INSERT INTO Modello VALUES('Mod1','Clio',2005,'Cost2');
INSERT INTO Modello VALUES('Mod2','Fiesta',2000,'Cost3');
INSERT INTO Modello VALUES('Mod3','Panda',2001,'Cost1');
INSERT INTO Modello VALUES('Mod4','Twingo',2019,'Cost2');
INSERT INTO Modello VALUES('Mod5','Focus',2010,'Cost3');
INSERT INTO Modello VALUES('Mod6','500',1960,'Cost1');
INSERT INTO Modello VALUES('Mod7','Focus',2001,'Cost3');
INSERT INTO Modello VALUES('Mod8','Duster',2021,'Cost5');
INSERT INTO Modello VALUES('Mod9','C3',2009,'Cost4');
INSERT INTO Modello VALUES('Mod10','Clio',2020,'Cost2');
INSERT INTO Modello VALUES('Mod11','Micra',2020,'Cost6');

-- Inserisco i dati nella tabella "Auto"
INSERT INTO Auto VALUES('AX567SJ',2006,75,'Info1','noepoca','Mod1','b');
INSERT INTO Auto VALUES('BG234II',1970,75,'Info2','epoca','Mod6','a');
INSERT INTO Auto VALUES('BH123GJ',2004,100,'Info1','noepoca','Mod2','c');
INSERT INTO Auto VALUES('BW443WR',2001,75,'Info4','noepoca','Mod3','d');
INSERT INTO Auto VALUES('BB098AF',2020,75,'Info2','noepoca','Mod4','a');
INSERT INTO Auto VALUES('NM685FF',2021,90,'Info1','noepoca','Mod10','c');
INSERT INTO Auto VALUES('AC657NN',2020,90,'Info3','noepoca','Mod10','e');
INSERT INTO Auto VALUES('AG678FD',2012,80,'Info1','noepoca','Mod5','e');
INSERT INTO Auto VALUES('BV345HH',1963,70,'Info3','epoca','Mod6','f');
INSERT INTO Auto VALUES('AL667UU',2010,90,'Info4','noepoca','Mod9','f');
INSERT INTO Auto VALUES('DC556YU',2002,100,'Info2','noepoca','Mod7','g');
INSERT INTO Auto VALUES('AA453GG',2002,90,'Info3','noepoca','Mod7','h');
INSERT INTO Auto VALUES('AD111OO',2021,100,'Info2','noepoca','Mod11','h');
INSERT INTO Auto VALUES('AB556BB',2021,75,'Info4','noepoca','Mod11','i');
INSERT INTO Auto VALUES('CA332MM',2021,100,'Info4','noepoca','Mod8','b');
INSERT INTO Auto VALUES('AX887PP',2021,90,'Info2','noepoca','Mod11','f');
INSERT INTO Auto VALUES('AZ448TT',2001,75,'Info3','noepoca','Mod3','h');

-- Inserisco i dati nella tabella "Pezzo"
INSERT INTO Pezzo VALUES('Pezzo1','Motore',499.50,1);
INSERT INTO Pezzo VALUES('Pezzo2','Marmitta',100,1);
INSERT INTO Pezzo VALUES('Pezzo3','Marmitta',150,3);
INSERT INTO Pezzo VALUES('Pezzo4','Pastiglie freni',150,4);
INSERT INTO Pezzo VALUES('Pezzo5','Sospensione',260,2);
INSERT INTO Pezzo VALUES('Pezzo6','Tergicristalli',50,3);
INSERT INTO Pezzo VALUES('Pezzo7','Ammortizzatori',300,4);
INSERT INTO Pezzo VALUES('Pezzo8','Motore',650,1);

-- Inserisco i dati nella tabella "Intervento"
INSERT INTO Intervento VALUES('Int1','cambio','2020-11-11',499.50,'DC556YU');
INSERT INTO Intervento VALUES('Int2','cambio','2020-10-28',100,'AX887PP');
INSERT INTO Intervento VALUES('Int3','riparazione','2019-01-31',900,'BB098AF');
INSERT INTO Intervento VALUES('Int4','riparazione','2020-04-14',300,'BW443WR');
INSERT INTO Intervento VALUES('Int5','sostituzione','2021-01-31',800,'AX567SJ');
INSERT INTO Intervento VALUES('Int6','riparazione','2021-02-18',600,'AL667UU');
INSERT INTO Intervento VALUES('Int7','sostituzione','2021-09-22',1099.50,'AA453GG');
INSERT INTO Intervento VALUES('Int8','cambio','2021-08-01',200,'AL667UU');
INSERT INTO Intervento VALUES('Int9','riparazione','2021-01-31',520,'AX567SJ');
INSERT INTO Intervento VALUES('Int10','cambio','2021-01-31',300,'AD111OO');

-- Inserisco i dati nella tabella "Utilizza"
INSERT INTO Utilizza VALUES('Int1','Pezzo1',1);
INSERT INTO Utilizza VALUES('Int2','Pezzo2',1);
INSERT INTO Utilizza VALUES('Int3','Pezzo3',2);
INSERT INTO Utilizza VALUES('Int4','Pezzo4',2);
INSERT INTO Utilizza VALUES('Int5','Pezzo8',1);
INSERT INTO Utilizza VALUES('Int6','Pezzo7',2);
INSERT INTO Utilizza VALUES('Int7','Pezzo1',1);
INSERT INTO Utilizza VALUES('Int8','Pezzo6',4);
INSERT INTO Utilizza VALUES('Int9','Pezzo5',2);
INSERT INTO Utilizza VALUES('Int6','Pezzo4',2);
INSERT INTO Utilizza VALUES('Int5','Pezzo4',1);
INSERT INTO Utilizza VALUES('Int7','Pezzo7',2);
INSERT INTO Utilizza VALUES('Int10','Pezzo3',2);

-- Stampo i dati
SELECT * FROM Cliente;
SELECT * FROM Costruttore;
SELECT * FROM Modello;
SELECT * FROM Auto;
SELECT * FROM Pezzo;
SELECT * FROM Intervento;
SELECT * FROM Utilizza;
