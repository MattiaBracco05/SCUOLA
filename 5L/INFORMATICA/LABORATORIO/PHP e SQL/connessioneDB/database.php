<?php

class Database {
	private static $host = "localhost";
	private static $username = "root";
	private static $password = "";
	private static $database = "esConnDDLDMLQL";
	private static $connection;

	//METODO per la connessione al database
	public static function connect() {
		self :: $connection = new mysqli(self :: $host, self :: $username, self :: $password, self :: $database);
		//Controllo se si è verificato un errore
		if (self :: $connection -> connect_error) {
			die("Connessione fallita: " . self :: $connection -> connect_error);
			return false;
		}
		//Se no --> connessione riuscita
		echo "Connessione al database riuscita.";
		return true;
	}

	//METODO per eseguire query
	public static function executeQuery($query) {
		$result = self :: $connection -> query($query);
		if (!$result) {
			echo "Errore nella query: " . self :: $connection -> error;
		}
		return $result;
	}

	//METODO per creare le tabelle nel database
	public static function createTables() {
		//Creo le tabelle
		echo "<br>Creo le tabelle...<br>";
		
		//Creo la tabella "users"
		$query = "CREATE TABLE IF NOT EXISTS users (
					id INT AUTO_INCREMENT PRIMARY KEY,
					username VARCHAR(50) NOT NULL,
					email VARCHAR(50) NOT NULL);";
					
		//se la tabella "users" è stata creata con successo --> Messaggio e Creo la tabella "posts"
		if (self :: executeQuery($query)) {
			echo "Tabella users creata con successo.";
			$query = "CREATE TABLE IF NOT EXISTS posts (
					id INT AUTO_INCREMENT PRIMARY KEY,
					user_id INT,
					FOREIGN KEY (user_id) REFERENCES users(id),
					title VARCHAR(100) NOT NULL,
					content TEXT NOT NULL);";
		
			//Se la tabella "posts" è stata creata con successo --> Messaggio
			if (self :: executeQuery($query)) {
				echo "<br>Tabella posts creata con successo.<br>";
				return true;
			}
			//Altrimenti --> Messaggio di errore (tabella "posts")
			else {
				echo "<br>Errore durante la creazione della tabella posts: " . self :: $connection -> error;
				return false;
			}
			
		}
		//Altrimenti --> Messaggio di errore (tabella "users")
		else {
			echo "<br>Errore durante la creazione della tabella users: " . self :: $connection -> error;
			return false;
		}
	}

	//METODO per inserire i dati nelle tabelle
	public static function populateTables() {
		
		//INSERISCO I DATI NELLA TABELLA "users"
		$success = true;
		//Ciclo for (ciclo per 30 volte)
		for ($i = 1; $i <= 30; $i++) {
			$nome = "Utente $i";
			$email = "email$i@example.com";
			$query = "INSERT INTO users (username, email) VALUES ('$nome', '$email')";
			
			//Controllo se si è verificato un errore
			if (!self :: executeQuery($query)) {
				//Messaggio di errore
				echo "<br>Errore durante il popolamento della tabella users: " . self :: $connection -> error;
				//Imposto "success" a "False"
				$success = false;
				//Interrompo il ciclo for
				break;
			}
		}
		//Fine ciclo for
		
		//INSERISCO I DATI NELLA TABELLA "posts"
		//Se "success" = "True" -->
		if ($success) {
			//Ciclo for (ciclo per 30 volte)
			for ($i = 1; $i <= 30; $i++) {
				$user_id = $i;
				$title = "Post $i";
				$content = "Contenuto del post $i";
				$query = "INSERT INTO posts (user_id, title, content) VALUES ('$user_id', '$title', '$content')";
				
				//Controllo se si è verificato un errore
				if (!self :: executeQuery($query)) {
					//Messaggio di errore
					echo "<br>Errore durante il popolamento della tabella posts: " . self::$connection->error;
					//Imposto "success" a "False"
					$success = false;
					//Interrompo il ciclo for
					break;
				}
			}
			//Fine ciclo for
		}
		
		//Se "success" = "True" --> Messaggio (di successo)
		if ($success) {
			echo "Dati inseriti con successo.<br>";
		}
		return $success;
	}

	//METODO per disconnettersi dal database
	public static function disconnect() {
		self :: $connection -> close();
		echo "Connessione chiusa.<br>";
	}
}

?>

