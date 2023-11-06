<?php
//Controllo che ci siano dei valori inseriti (posso accedere a "login.php" solo dal file "index.html"
if (isset($_GET["user"]) && isset($_GET["password"])) {
	$user = $_GET["user"];
	$pw = $_GET["password"];

	//Creo l'array chiamatao "database"
	$database = array();

	//Ciclo e aggiungo 5 utenti all'array database
	for ($i = 1; $i <= 5; $i++) {
		$psw = rand($i, ($i + 1) * 5);
		$database[] = array(
			"user" => "utente" . $i,
			"password" => $psw ,
			"passwordcrip" => md5($psw),
		);
	}

	//Imposto updated a "False"
	$updated = false;

	//Ciclo con il foreach per gli elementi (utenti) presenti nell'array
	foreach ($database as $num => &$data) {
		//COntrollo se l'user inserito corrisponde con l'user salvato
		if ($data["user"] == $user) {
			$nc = $num;
			//Imposto updated al valore "True"
			$updated = true;
			break; 
		}
	}
	
	//Se updated = True -->
	if ($updated) {
		//Ricavo la password e la cripto con md5
		$database[$nc]["password"] = $pw;
		$database[$nc]["passwordcrip"] = md5($pw);
		
		//Stampo la password cambiata
		echo "Password cambiata per l'utente: $user<br>";
		
		//Stampo l'array dell'user per cui ho appena cambiato la password
		echo "<pre>";
		print_r($database[$nc]);
		echo "</pre>";
	}
	//Altrimenti --> Messaggio di errore
	else {
		echo "Utente non trovato nel  database.";
	}
    
    //Stampo l'array "database"
    echo "<pre>";
    print_r($database);
    echo "</pre>";
}

//Altrimenti --> Stampo accesso negato (in caso l'utente tenti di accedere direttamente alla pagina .php senza pssare da index.html)
elseif (!isset($_GET["invio"])) {
	echo "<pre>";
	echo "<h1>Accesso negato!</h1>";
	echo "</pre>";  
}
?>
