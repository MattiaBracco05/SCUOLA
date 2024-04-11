<?php
include 'database.php';

// Connessione al database
Database::connect();

if ($_SERVER["REQUEST_METHOD"] == "POST") {
	//Recupero i dati inviati dal form
	$username = $_POST["username"];
	$email = $_POST["email"];
	$title = $_POST["title"];
	$content = $_POST["content"];
	
	//echo "<br>INSERT INTO users (username, email) VALUES ('$username', '$email')<br>";
	
	//Eseguo query per inserire l'utente nella tabella users
	$queryUser = "INSERT INTO users (username, email) VALUES ('$username', '$email');";
	if (Database :: executeQuery($queryUser)) {
		echo "<br>Utente $username aggiunto con successo.<br>";
		
		//Eseguo query per inserire il post nella tabella posts
		$queryPost = "INSERT INTO posts (user_id, title, content) VALUES (LAST_INSERT_ID(), '$title', '$content');";
		if (Database :: executeQuery($queryPost)) {
			echo "Dati inseriti con successo.<br>";
		}
		//Altrimenti --> Messaggio di errore (inserimento post)
		else {
			echo "<br>Errore durante l'inserimento del post: " . Database :: $connection -> error;
		}
		
	}
	//Altrimenti --> Messaggio di errore (inserimento user)
	else {
		echo "<br>Errore durante l'inserimento dell'utente: " . Database :: $connection -> error;
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

