<?php
session_start();

//Se si è gia effettuato il login --> mi sposto alla pagina di booking
if (isset($_SESSION['logged_in']) && $_SESSION['logged_in']) {
    header("Location: booking.php");
    exit();
}

//Altrimenti bisgona efettuare il login
if ($_SERVER['REQUEST_METHOD'] === 'POST') {

    //Ricavo i valori inseriti dall'utente
    $username = $_POST['username'];
    $password = $_POST['password'];

    //Controllo le credenziali, se corrette -->
    if ($username === 'admin' && $password === 'admin') {
        $_SESSION['logged_in'] = true;

        //Cookie con durata di 2 minuti (120 secondi)
        setcookie('user', $username, time() + 120);
        header("Location: booking.php");
        exit();
    }

    //Altrimenti --> messaggio di errore
    else {
        echo "Credenziali non valide";
    }
}
?>