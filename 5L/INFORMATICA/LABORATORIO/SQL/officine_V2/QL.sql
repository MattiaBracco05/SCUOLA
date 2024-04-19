-- 5L Bracco Mattia

-- Seleziono il DB
USE Officina;

\! echo '\nQUERY A: Elenco delle auto di Consiglio' 
-- JOIN esplicito
SELECT Auto.Targa, Auto.AnnoImmatricolazione, Auto.CavalliFiscali, Auto.Informazioni
FROM Cliente
JOIN Auto ON Cliente.CodFiscale = Auto.CodFiscaleCliente
WHERE Cliente.Cognome = 'Consiglio';

-- JOIN implicito
SELECT Targa, AnnoImmatricolazione, CavalliFiscali, Informazioni
FROM Auto
WHERE CodFiscaleCliente IN (SELECT CodFiscale FROM Cliente WHERE Cognome = 'Consiglio');

\! echo '\nQUERY B: Elenco dei clienti che abitano a Saluzzo' 
-- JOIN esplicito
SELECT Cliente.CodFiscale, Cliente.Nome, Cliente.Cognome
FROM Cliente
WHERE Cliente.Localita = 'Saluzzo';

-- JOIN implicito
SELECT CodFiscale, Nome, Cognome
FROM Cliente
WHERE Localita = 'Saluzzo';

\! echo '\nQUERY 1: Tutti gli interventi fatti sui modelli Renault' 
-- JOIN esplicito
SELECT Intervento.Codice, Intervento.Tipo, Intervento.Data, Intervento.Costo, Intervento.Targa
FROM Intervento
JOIN Auto ON Intervento.Targa = Auto.Targa
JOIN Modello ON Auto.CodiceModello = Modello.Codice
JOIN Costruttore ON Modello.CodiceCostruttore = Costruttore.Codice
WHERE Costruttore.Nome = 'Renault';

-- JOIN implicito
SELECT I.Codice, I.Tipo, I.Data, I.Costo, I.Targa
FROM Intervento I, Auto A, Modello M, Costruttore C
WHERE I.Targa = A.Targa
    AND A.CodiceModello = M.Codice
    AND M.CodiceCostruttore = C.Codice
    AND C.Nome = 'Renault';

\! echo '\nQUERY 3: Elenco degli interventi contenenti nella descrizione “cambio”' 
SELECT *
FROM Intervento
WHERE Tipo LIKE '%cambio%';

\! echo '\nQuery 4: Elenco dei clienti aventi auto d''epoca'
-- JOIN esplicito
SELECT DISTINCT Cliente.CodFiscale, Cliente.Nome, Cliente.Cognome
FROM Cliente
JOIN Auto ON Cliente.CodFiscale = Auto.CodFiscaleCliente
WHERE Auto.Tipo = 'epoca';

-- JOIN implicito
SELECT DISTINCT C.CodFiscale, C.Nome, C.Cognome
FROM Cliente C, Auto A
WHERE C.CodFiscale = A.CodFiscaleCliente
    AND A.Tipo = 'epoca';

\! echo '\nQuery 6: Elenco di tutti i modelli Ford, ordinate per anno' 
-- JOIN esplicito
SELECT Modello.Codice, Modello.Nome, Modello.Anno, Costruttore.Nome AS Costruttore
FROM Modello
JOIN Costruttore ON Modello.CodiceCostruttore = Costruttore.Codice
WHERE Costruttore.Nome = 'Ford'
ORDER BY Modello.Anno;

-- JOIN implicito
SELECT M.Codice, M.Nome, M.Anno, C.Nome AS Costruttore
FROM Modello M, Costruttore C
WHERE M.CodiceCostruttore = C.Codice
    AND C.Nome = 'Ford'
ORDER BY M.Anno;

\! echo '\nQuery 7: Elenco di tutte le auto Fiat immatricolate nel 2001' 
-- JOIN esplicito
SELECT Auto.Targa, Auto.AnnoImmatricolazione, Auto.CavalliFiscali, Auto.Informazioni
FROM Auto
JOIN Modello ON Auto.CodiceModello = Modello.Codice
JOIN Costruttore ON Modello.CodiceCostruttore = Costruttore.Codice
WHERE Costruttore.Nome = 'Fiat'
    AND Auto.AnnoImmatricolazione = 2001;

-- JOIN implicito
SELECT Targa, AnnoImmatricolazione, CavalliFiscali, Informazioni
FROM Auto, Modello, Costruttore
WHERE Auto.CodiceModello = Modello.Codice
    AND Modello.CodiceCostruttore = Costruttore.Codice
    AND Costruttore.Nome = 'Fiat'
    AND AnnoImmatricolazione = 2001;

\! echo '\nQuery 8: Costo medio dei pezzi aventi descrizione “motore”' 
SELECT AVG(Prezzo) AS CostoMedio
FROM Pezzo
WHERE Descrizione = 'Motore';

\! echo '\nQuery 9: Elenco delle date, prezzi e tipo di intervento effettuati dal cliente Bianchi' 
-- JOIN esplicito
SELECT Intervento.Data, Intervento.Costo, Intervento.Tipo
FROM Intervento
JOIN Auto ON Intervento.Targa = Auto.Targa
JOIN Cliente ON Auto.CodFiscaleCliente = Cliente.CodFiscale
WHERE Cliente.Cognome = 'Bianchi';

-- JOIN implicito
SELECT I.Data, I.Costo, I.Tipo
FROM Intervento I, Auto A, Cliente C
WHERE I.Targa = A.Targa
    AND A.CodFiscaleCliente = C.CodFiscale
    AND C.Cognome = 'Bianchi';

\! echo '\nQuery 10: Numero auto a cui è stata sostituita la marmitta' 
SELECT COUNT(*) AS NumeroAuto
FROM Utilizza
JOIN Pezzo ON Utilizza.CodicePezzo = Pezzo.Codice
WHERE Pezzo.Descrizione = 'Marmitta';

