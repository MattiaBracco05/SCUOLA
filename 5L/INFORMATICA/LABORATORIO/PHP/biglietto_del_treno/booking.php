<?php
session_start();

//Se non ho effettuato il login --> rimando alla pagina di login
if (!isset($_SESSION['logged_in'])) {
    echo "<pre>";
	echo "<h1>Accesso negato!</h1>";
	echo "</pre>";
    header("Location: ./index.html");
    exit();
} else {
    //Ricevo i valori del form
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $prezzoBase = $_POST['prezzoInserito'];
        $tipologiaTreno = $_POST['trenoScelto'];

        //Calcolo il sovrapprezzo in base al tipo di treno
        switch ($tipologiaTreno) {

            //Case treno di 2° classe
            case "secondaClasse":
                $sovrapprezzo = $prezzoBase * 0.07;
                $nomeTreno = "Freccia rossa 2° classe";
                break;

            //Case treno di 1° classe
            case "primaClasse":
                $sovrapprezzo = $prezzoBase * 0.12;
                $nomeTreno = "Freccia rossa 1° classe";
                break;

            //Case treno premium
            case "premium":
                $sovrapprezzo = $prezzoBase * 0.18;
                $nomeTreno = "Freccia rossa premium";
                break;

            //Default
            default:
                $sovrapprezzo = 0;
                $nomeTreno = "Errore!, Tipologia del treno non valida";
        }

        //Calcolo il prezzo totale
        $prezzoTotale = $prezzoBase + $sovrapprezzo;

        //Stampo a video il prezzo totale e il treno selezionato
        echo "Il prezzo totale del biglietto è di {$prezzoTotale} € e il treno selezionato è il {$nomeTreno}";
    }
}
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>5L Bracco Booking</title>
</head>

<body>
    <h2>Pagina di Booking</h2>

    <!-- Inzio del form (prezzo treno) -->
    <form method="post" action="./booking.php">

        <!-- Label e input text del prezzo di partenza del treno -->
        <label>Prezzo base:</label>
        <input type="number" id="prezzoInserito" name="prezzoInserito" required><br>

        <!-- Label e select del tipo di treno -->
        <label for="trenoScelto">Tipologia del treno:</label>
        <select id="trenoScelto" name="trenoScelto" required>
            <option value="secondaClasse">Freccia rossa 2° classe</option>
            <option value="primaClasse">Freccia rossa 1° classe</option>
            <option value="premium">Freccia rossa premium</option>
        </select>
        <br>

        <!-- Button submit -->
        <input type="submit" value="Calcola sovrapprezzo">

    </form>
    <!-- Fine del form (prezzo treno) -->

    <!-- Inizio del form (logout) -->
    <form method="post" action="./logout.php">

        <!-- Button submit -->
        <input type="submit" value="Logout">

    </form>
    <!-- Fine del form (logout) -->

</body>

</html>