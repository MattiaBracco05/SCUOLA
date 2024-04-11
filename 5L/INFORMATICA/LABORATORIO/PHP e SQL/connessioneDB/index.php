<?php
include 'database.php';

//Connessione al database
if (Database :: connect()) {

	//Creazione delle tabelle -->
	if (Database :: createTables()) {
        
		//Inserimento dei dati nelle tabelle -->
		if (Database::populateTables()) {
			echo "Tutto è stato eseguito con successo<br>";
		}
		//Altriemnti --> Messaggio di errore (inserimento)
		else {
			echo "Errore durante il popolamento delle tabelle<br>";
		}
	
	//Altrimenti --> Messaggio di errore (creazione)	
	} else {
		echo "Errore durante la creazione delle tabelle<br>";
	}

//Altrimenti --> Messaggio di errore (connessione)
} else {
    echo "Errore durante la connessione al database<br>";
}

//Disconnessione dal database
Database :: disconnect();

echo "<br><a href='./form.html'>Vai al form di inserimento dati</a><br>";
?>

