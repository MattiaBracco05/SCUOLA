<?php
session_start();

//Includo il file "utenti.php" dove è presente la'rray associativo degli utenti
include("utenti.php");

//Se è stato effettuato il logout --> distruggo la sessione
if (isset($_GET["logout"])) {
    session_unset();
    session_destroy();
    header("Location: index.php");
    exit();
}

//Se è già stato effettuato il login --> mi sposto al file benveuto.php
if (isset($_SESSION["username"])) {
    header("Location: benvenuto.php");
    exit();
}

//Controllo delle credenziali
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    //Ricavo i valori inseriti dall'utente
    $username = $_POST["username"];
    $password = $_POST["password"];
    $colore = $_POST["colore"];

    //Controllo se nell'array ci sono delle chiavi che corrispondo, se si -->
    if (array_key_exists($username, $utenti) && $utenti[$username][0] == $password) {
        //Salvo nella sessione "username" il nome utente e nella sessione "colore" il colore inserito
        $_SESSION["username"] = $username;
        $_SESSION["colore"] = $colore;

        //Mi sposto al file benvenuto.php
        header("Location: benvenuto.php");
        exit();
    }
    //Altrimenti --> messaggio di errore
    else {
        $messaggioErrore = "Login fallito. Utente non trovato o password errata.";
    }
}
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>

<body>

    <h2>Form di Autenticazione</h2>

    <!-- Messaggio di errore -->
    <?php if (isset($messaggioErrore)): ?>
        <p style="color: red;">
            <?php echo $messaggioErrore; ?>
        </p>
    <?php endif; ?>

    <!-- Inizio del form -->
    <form action="index.php" method="post">

        <!-- Input del nome utente -->
        <label for="username">Nome Utente:</label>
        <input type="text" name="username" required><br>

        <!-- Input della password -->
        <label for="password">Password:</label>
        <input type="password" name="password" required><br>

        <!-- Input del colore preferito -->
        <label for="colore">Colore Preferito:</label>
        <input type="text" name="colore" required><br>

        <!-- Button pe rinviare i dati del form -->
        <input type="submit" value="Login">

    </form>
    <!-- Fine del form -->

</body>

</html>