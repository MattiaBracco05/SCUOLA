<?php
	//Inizializzazione di un array
	$auto = ['Ferrari', 'Porsche', 'Lamborghini'];

	//Accesso agli elementi dell'array tramite indice
	echo "Primo elemento: " .$auto[0];
	echo "<br> Secondo elemento: " .$auto[1];
	echo "<br> Terzo elemento: " .$auto[2] ."<br>";

	//Utilizzo di alcune funzioni speciali per accedere agli elementi
	echo "<br> Utilizzo 'Next'";
	echo "<br> Elemento corrente: " .current($auto) .", indice: " .key($auto) ."<br>";
	next($auto);
	
	echo "<br> Utilizzo 'Prev'";
	echo "<br> Elemento corrente: " .current($auto) .", indice: " .key($auto) ."<br>";
	prev($auto);
	
	echo "<br> Utilizzo 'Reset'";
	echo "<br> Elemento corrente: " .current($auto) .", indice: " .key($auto) ."<br>";
	reset($auto);
	
	echo "<br> Utilizzo 'End'";
	echo "<br> Elemento corrente: " .current($auto) .", indice: " .key($auto) ."<br>";
	end($auto);
	
	echo "<br> Utilizzo 'Current'";
	echo "<br> Elemento corrente: " .current($auto) .", indice: " .key($auto) ."<br>";
?>

