<!DOCTYPE html>
<html>
<head>
	<title>Risultato Interrogazione</title>
</head>
<body>
	<h1>Risultato Interrogazione</h1>
    <?php
    //Array associativo multidimensionale con dati degli studenti
    $studenti = array(
    	"studente1" => array(
			"cognome" => "Rossi",
			"nomi" => "Mario",
			"matematica" => 85,
			"italiano" => 78,
			"scienze" => 92,
			"storia" => 70,
			"inglese" => 88
    	),
		"studente2" => array(
			"cognome" => "Bianchi",
			"nomi" => "Laura",
			"matematica" => 75,
			"italiano" => 84,
			"scienze" => 90,
			"storia" => 72,
			"inglese" => 89
		),
    );

    //Verifico se sono stati inviati dati dal form
    if (isset($_POST['cognome']) && isset($_POST['materia'])) {
		$cognome = $_POST['cognome'];
		$materia = $_POST['materia'];

        //Cerca lo studente nell'array associativo (tramite un for each)
        foreach ($studenti as $studente) {
			//Controllo se il cognome inserito corrisponde
		    if ($studente['cognome'] == $cognome) {
		        echo "Nome: " . $studente['nomi'] . "<br>";
		        echo "Voto preso in " . $materia . ": " . $studente[$materia] . "<br>";
		        break;
		    }
        }
    } else {
        echo "Inserisci un cognome e seleziona una materia.";
    }
    ?>
</body>
</html>

