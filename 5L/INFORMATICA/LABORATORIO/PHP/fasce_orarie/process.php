<?php
//Avvio la sessione
session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    //Ricavo i valori inseriti
    $nome = $_POST['name'];
    $giorno = $_POST['days'];
    $fascia = $_POST['times'];

    //Creo un array associativo per le disponibilità dell'utente
    $dispRegistrata = [
        'name' => $nome,
        'days' => $giorno,
        'times' => $fascia
    ];

    //Disponibilità salvate nelle sessioni
    if (isset($_SESSION['availabilities'][$nome])) {
        $_SESSION['availabilities'][$nome]['days'] = array_merge($_SESSION['availabilities'][$nome]['days'], $giorno);
        $_SESSION['availabilities'][$nome]['times'] = array_merge($_SESSION['availabilities'][$nome]['times'], $fascia);
    } else {
        $_SESSION['availabilities'][$nome] = $dispRegistrata;
    }
}

//Vado al file summary.php
header("Location: summary.php");
