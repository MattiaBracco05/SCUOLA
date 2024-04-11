<?php
    //Includo il file database.php
    include './database.php';

    //Connessione al DB
    Database :: connessione();

    //Ricavo le tabelle
    $tabellaUtenti = 'SELECT * FROM Utenti;';
    $tabellaPost = 'SELECT * FROM Post;';

    //Ricavo i dati delle tabelle
    $datiUtenti = Database :: eseguiQuery($tabellaUtenti) -> fetch_all(MYSQLI_ASSOC);
    $datiPost = Database :: eseguiQuery($tabellaPost) -> fetch_all(MYSQLI_ASSOC);
?>

<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../css/style.css">
    <link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css' integrity='sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm' crossorigin='anonymous'>
    <title>Mostra tabelle</title>
</head>
<body>

    <!-- Inizio della navbar -->
    <div class="nav-bar d-flex justify-content-around col-12">
        <a href="../index.html">Home</a>
        <a href="../html/AggiungiPost.html">Aggiungi post</a>
        <a href="../html/AggiungiUtenti.html">Aggiungi utenti</a>
        <a href="./VisualizzaDb.php">Visualizza db</a>
    </div>
    <!-- Fine della navbar -->

    <!-- Inizio della riga -->
    <div class="table-container mt-5">

        <!-- Inizio della tabella -->
        <table class="table">
            <!-- Header -->
            <thead class="thead-light">
                <tr>
                    <th scope="col" class="text-center">ID</th>
                    <th scope="col" class="text-center">Username</th>
                    <th scope="col" class="text-center">Email</th>
                </tr>
            </thead>
            <!-- Body -->
            <tbody class="elementi-tabella">
                <?php
                    //Ciclo for each -->
                    for($i=0; $i < count($datiUtenti); $i++){
                        echo"<tr>";
                        echo "<td class='text-center'>". $datiUtenti[$i]['ID'] ."</td>";
                        echo "<td class='text-center'>". $datiUtenti[$i]['Username'] ."</td>";
                        echo "<td class='text-center'>". $datiUtenti[$i]['Email'] ."</td>";
                        echo"</tr>";
                    }
                ?>
            </tbody>
        </table>
        <!-- Fine della tabella -->
    </div>
    <!-- Fine della riga -->

    <!-- Inizio della riga -->
    <div class="table-container mt-5">
        <!-- Inizio della tabella -->
        <table class="table">
            
            <!-- Header -->
            <thead class="thead-light">
                <tr>
                    <th scope="col" class="text-center">ID</th>
                    <th scope="col" class="text-center">User</th>
                    <th scope="col" class="text-center">Titolo</th>
                    <th scope="col" class="text-center">Messaggio</th>
                </tr>
            </thead>
            <!-- Body -->
            <tbody class="elementi-tabella">
                <?php
                    //Ciclo for each -->
                    for($i=0; $i < count($datiPost); $i++){
                        echo"<tr>";
                        echo "<td class='text-center'>". $datiPost[$i]['ID'] ."</td>";
                        echo "<td class='text-center'>". $datiPost[$i]['UserID'] ."</td>";
                        echo "<td class='text-center'>". $datiPost[$i]['Titolo'] ."</td>";
                        echo "<td class='text-center'>". $datiPost[$i]['Messaggio'] ."</td>";
                        echo"</tr>";
                    }
                ?>
            </tbody>
        </table>
        <!-- Fine della tabella -->
    </div>
    <!-- Fine della riga -->


    <script src='https://code.jquery.com/jquery-3.2.1.slim.min.js' integrity='sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN' crossorigin='anonymous'></script>
    <script src='https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js' integrity='sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q' crossorigin='anonymous'></script>
    <script src='https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js' integrity='sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl' crossorigin='anonymous'></script>
</body>
</html>