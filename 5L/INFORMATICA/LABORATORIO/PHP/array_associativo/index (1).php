<!DOCTYPE html>
<html lang="en">
	<head>
		<title>Array</title>
	</head>
	<body>
		<h1>Esempio di utilizzo degli array</h1>
		<?php
			//Definisco un array associativo con i dati della persona
			$persona = [
				'nome' => 'Mario', 
				'cognome' => 'Rossi', 
				'eta' => '35', 
				'lavoro' => 'Programmatore'
			];
			
			//Stampo l'arrat formattato
			echo "<pre>";
			print_r($persona);
			echo"</pre>";
			
			//Stampo il nome
			echo "<br>Stampo il nome...<br>";
			echo $persona['nome']."<br>";

			//Stampo il lavoro
			echo "<br>Stampo il lavoro...<br>";
			echo $persona['lavoro']."<br>";

			//Definisco un array associativo con le lingue
			$lingue = [
				'it' => 'italiano',
				'en' => 'inglese',
				'es' => 'spagnolo',
				'fr' => 'francese',
				'de' => 'tedesco',
				'ru' => 'russo'
			];
			
			//STampo l'array formattato
			echo "<pre>";
			print_r($lingue);
			echo"</pre>";

			//Utilizzo in_array
			echo "<br>Verifica se una lingua (nel mio caso spagnolo) è supportata o non supportata (utilizzo di 'in_array')...<br>";
			//Se spagnolo è presente nell'array dico che la lingua è supportata
			if (in_array('spagnolo', $lingue)) {
				echo "Lingua supportata";
			}
			//Altrimenti --> messaggio di errore (lingua non supportata)
			else {
				echo "Lingua non supportata";
			}
		?>
	</body>
</html>

