<?php
session_start();

//Controllo che l'utente sia autenutiato, se no lo rimando al file index.php
if (!isset($_SESSION["username"])) {
    header("Location: index.php");
    exit();
}

//Mi salvo in una variabile il valore del colore preferito (contenuto nella sessione)
$colorePreferito = $_SESSION["colore"];
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Benvenuto</title>
</head>

<body>
    <!-- Stampo il messaggio di benvenuto -->
    <h2>Benvenuto,<?php echo $_SESSION["username"]; ?>!</h2>

    <!-- Stampo il messaggio con il colore preferito -->
    <p>Il tuo colore preferito è<?php echo $colorePreferito; ?>.</p>

    <!-- Collegamento per tornare indietro (logout) -->
    <a href="index.php?logout=true">Logout</a>

</body>

</html>