<?php
session_start();

//Calcolo delle statistiche
$conteggioDisponibilita = [];

foreach ($_SESSION['availabilities'] as $availability) {
    foreach ($availability['days'] as $day) {
        foreach ($availability['times'] as $time) {
            $option = "$day-$time";
            if (!isset($conteggioDisponibilita[$option])) {
                $conteggioDisponibilita[$option] = ['tot' => 1, 'persona' => [$availability['name']]];
            } else {
                $conteggioDisponibilita[$option]['tot']++;
                $conteggioDisponibilita[$option]['persona'][] = $availability['name'];
            }
        }
    }
}

//Ordino in base al numero di persone disponibili
arsort($conteggioDisponibilita); 

$disponibilitaMAX = 0;
$disponibilitaMAX_opzioni = [];

//Ciclo per le disponibilità registrate
foreach ($conteggioDisponibilita as $option => $data) {
    $tot = $data['tot'];
    if ($tot >= $disponibilitaMAX) {
        $disponibilitaMAX = $tot;
        $disponibilitaMAX_opzioni[] = ['option' => $option, 'persona' => $data['persona']];
    } else {
        //Posso interrompere il ciclo (array ordinato decrescente)
        break;
    }
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Riepilogo Disponibilità</title>
</head>
<body>

<h2>Riepilogo delle Disponibilità</h2>

<!-- Inizio della tabella di ripeilogo delle disponibilità -->
<table border="1">
    <tr>
        <th>Opzione Giorno-Fascia Oraria</th>
        <th>Numero di Persone Disponibili</th>
    </tr>
    <?php
    foreach ($conteggioDisponibilita as $option => $data) {
        echo "<tr><td>$option</td><td>{$data['tot']}</td></tr>";
    }
    ?>
</table>
<!-- Fine della tabella di ripeilogo delle disponibilità -->


<h3>Opzioni con il massimo numero di persone disponibili:</h3>

<!-- Inizio stampa opzione con la massima disponibilità -->
<ul>
    <?php
    foreach ($disponibilitaMAX_opzioni as $data) {
        echo "<li>{$data['option']} - Persone presenti: " . implode(', ', $data['persona']) . "</li>";
    }
    ?>
</ul>
<!-- Fine stampa opzione con la massima disponibilità -->


<h3>Nomi di chi NON è presente nelle fasce orarie più votate:</h3>

<!-- Inizio stampa nomi non presenti nelle fasce orarie più votate -->
<ul>
    <?php
    foreach ($_SESSION['availabilities'] as $availability) {
        $name = $availability['name'];
        $isPresent = false;
        foreach ($disponibilitaMAX_opzioni as $data) {
            if (in_array($name, $data['persona'])) {
                $isPresent = true;
                break;
            }
        }
        if (!$isPresent) {
            echo "<li>$name</li>";
        }
    }
    ?>
</ul>
<!-- Fine stampa nomi non presenti nelle fasce orarie più votate -->

<!-- Button per azzerare i dati -->
<form action="reset.php" method="post">
    <input type="submit" value="AZZERA DATI">
</form>

</body>
</html>
