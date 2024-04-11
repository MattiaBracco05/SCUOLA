<?php
//Includo il file "database.php"
include 'database.php';

//Connessione al database
Database :: connect();

if ($_SERVER["REQUEST_METHOD"] == "POST") {
	
	//Select di tutti i dati delle 2 tabelle unite
	$queryTab = "SELECT * FROM users, posts WHERE users.id=posts.user_id;";
	
	if (Database :: executeQuery($queryTab)) {	
	}
	//Altrimenti --> Messaggio di errore (estrazione)
	else {
		echo "<br>Errore durante l'estrazione dei dati: " . Database :: $connection -> error;
	}
	
}
//Altrimenti --> Messaggio di errore (controllo)
else {
	echo "<br>Errore durante il controllo del REQUEST_METHOD: " . Database :: $connection -> error;
}

//Disconnessione dal database
Database :: disconnect();

echo "<br><a href='./form.html'>Torna al form di inserimento dati</a><br>";
?>

