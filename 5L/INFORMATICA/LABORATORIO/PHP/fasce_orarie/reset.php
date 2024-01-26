<?php
//Avvio la sessione
session_start();

//Azzero i dati delle sessioni
unset($_SESSION['availabilities']);

//Ritorno alla pagina principale
header("Location: index.php");
?>