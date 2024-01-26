<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sterlina Market - Pagamento</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f7f7f7;
            text-align: center;
            margin: 0;
            padding: 0;
        }

        h2 {
            color: #333;
        }

        table {
            width: 80%;
            margin: 20px auto;
            border-collapse: collapse;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            background-color: #fff;
        }

        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }

        th {
            background-color: #4caf50;
            color: white;
        }

        p {
            color: #555;
            margin-top: 20px;
        }

        a {
            display: inline-block;
            padding: 10px 20px;
            margin-top: 20px;
            background-color: #4caf50;
            color: white;
            text-decoration: none;
            font-weight: bold;
            border-radius: 5px;
        }

        a:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $nome = $_POST["nome"];
        $cognome = $_POST["cognome"];
        $pezzi = $_POST["pezzi"];
        $prodotti = array();
        $prodotti2 = array();

        for ($i = 1; $i <= $pezzi; $i++) {
            $prodotto = $_POST["prodotto_" . $i];
            $prezzo = $_POST["prezzo_" . $i];
            $prodotti[] = array("prodotto" => $prodotto, "prezzo" => $prezzo);
            $prodotti2[] = array("prodotto" => $prodotto, "prezzo" => $prezzo);
        }

        // Ordina per nome
        usort($prodotti, function ($a, $b) {
            return strcmp($a["prodotto"], $b["prodotto"]);
        });

        // Ordina per prezzo
        usort($prodotti2, function ($a, $b) {
            return $a["prezzo"] - $b["prezzo"];
        });

        // Calcola il totale
        $totale = array_reduce($prodotti, function ($acc, $prodotto) {
            return $acc + $prodotto["prezzo"];
        }, 0);
    ?>
        <h2>Riepilogo Ordine</h2>
        <table border="1">
            <tr>
                <th>Prodotto (Nome)</th>
                <th>Prezzo</th>
                <th></th>
                <th>Prodotto (Prezzo)</th>
                <th></th>
            </tr>
            <?php
            for ($i=0; $i<count($prodotti); $i++) {
            ?>
                <tr>
                    <td><?php echo $prodotti[$i]["prodotto"]; ?></td>
                    <td><?php echo $prodotti[$i]["prezzo"]; ?></td>
                    <td></td>
                    <td><?php echo $prodotti2[$i]["prodotto"]; ?></td>
                    <td><?php echo $prodotti2[$i]["prezzo"]; ?></td>
                </tr>
            <?php
            }
            ?>
        </table>

        <p>Totale: <?php echo $totale; ?></p>
        <p><a href="accesso.php">Nuovo Acquisto</a></p>
    <?php
    }
    ?>
</body>
</html>

