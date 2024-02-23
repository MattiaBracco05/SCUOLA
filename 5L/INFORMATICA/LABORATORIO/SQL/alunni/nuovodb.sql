-- 5L Bracco Mattia - 26/01/2024

/* Per usare il file "nuovodb.sql" digito il seguente comando; ./mysql -u root < ~/Documenti/5L_Bracco/nuovodb.sql -t  (il comando "-t" serve per formattare la tabella anche seguendo il comando) */

/*
SCRIVERE DEI COMMENTI
*/

-- Questo è un commento (che posso scrivere solamente su 1 riga)

/* Questo è un commento (su una riga) */

/*
Queste righe
sono tutte e 2
dei commenti
*/

/*
DATABASE
*/

/* Elimino il database "nuovodb" */
DROP database nuovodb;

/* Creo il database "nuovodb" se non è già esistente (in questo caso non lo è perchè lo ho appena eliminato) */
CREATE DATABASE IF NOT EXISTS nuovodb;

/* Mostra l'elenco dei database (tra i quali ci sarà anche "nuovodb") */
SHOW DATABASES;

/* Seleziono il database su cui lavorare */
USE nuovodb;


/*
TABELLE
*/

/* Cancello la tabella persone */
--DROP TABLE IF EXISTS Persone;

/*
ATTENZIONE, il comando drop tabela cancella sia:
- I dati nella tabella
- La struttura della tabella
*/

/* Creo la tabella "Persone" */
CREATE TABLE `Persone` (
	-- Definisco l'ID come intero che si autoincrementa
	`id` INT NOT NULL AUTO_INCREMENT,
	
	-- La differenza tra "CHAR" e "VARCHAR" è che "CHAR" occuperà sempre 45 posti mentre "VARCHAR" ne occuperà il minimo indispensabile (ad esempio il CF lo metto come "CHAR" perchè ha una lunghezza fissa)
	-- Inoltre questi campi possono essere di tipo NULL
	`nome` CHAR(45) NULL,
	`cognome` VARCHAR(45) NULL,
	
	-- La data di nascita vado a definirla come tipo "DATE"
	`dataDiNascita` DATE NULL,
	
	-- Con "ENUM" vado a definire come valori validi i 2 presenti nella parentesi
	`sesso` ENUM('M','F') NULL,
	
	-- Un numero di telefono non devo mai memorizzarlo come intero perchè altrimenti lo "0" (0175...) verrebbe rimosso oppure il "+" (+39 123...) verrebbe considerato errore
	
	-- Vado ad impostare come PRIMARY KEY (PK) il campo "id"
	PRIMARY KEY (`id`)
);

\! echo '\nHo creato la tabella "Persone"'

/* Mostro le tabelle presenti nel database selezionato ("nuovodb") */
SHOW tables;

\! echo '\nQuesto è il contenuto della tabella "Persone"'

/* Mostro il contenuto della tabella "Persone" */
DESCRIBE Persone;

/*
MODIFICARE UNA TABELLA
*/

/* Modifico il nome della tabella (Persone --> Alunni) */
ALTER TABLE Persone RENAME Alunni;

/* Mostro le tabelle presenti nel database selezionato (adesso al posto di "Persone" ci sarà "Alunni") */
\! echo '\nRinomino la tabella "Persone" in "Alunni"'
\! echo 'Mostro le tabelle presenti nel database selezionato (adesso al posto di "Persone" ci sarà "Alunni")'
SHOW tables;

/* Cambio il campo nome da "CHAR(45)" a "VARCHAR(50)" */
ALTER TABLE Alunni CHANGE nome nomeAlunno VARCHAR(50);

/* Mostro il contenuto aggiornato della tabella "Alunni" */
\! echo '\nCambio il campo nome da "CHAR(45)" a "VARCHAR(50)"'
\! echo 'Mostro il contenuto aggiornato della tabella "Alunni"'
DESCRIBE Alunni;

/* Aggiungo il campo ("indirizzo") alla tabella "Alunni" */
ALTER TABLE Alunni ADD indirizzo VARCHAR(25) NOT NULL;

/* Mostro il contenuto aggiornato della tabella "Alunni" */
\! echo '\nAggiungo in campo "indirizzo" alla tabella "Alunni"'
\! echo 'Mostro il contenuto aggiornato della tabella "Alunni"'
DESCRIBE Alunni;

/* Elimino il campo ("indirizzo") dalla tabella "Alunni" */
ALTER TABLE Alunni DROP indirizzo;

/* Mostro il contenuto aggiornato della tabella "Alunni" */
\! echo '\nElimino il campo "indirizzo" dalla tabella "Alunni"'
\! echo 'Mostro il contenuto aggiornato della tabella "Alunni"'
DESCRIBE Alunni;
