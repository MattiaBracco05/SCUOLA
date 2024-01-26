<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sterlina Market - Cassa</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            text-align: center;
            padding: 20px;
        }

        h2 {
            color: #333;
        }

        form {
            max-width: 600px;
            margin: 0 auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        label {
            display: block;
            margin-bottom: 8px;
            color: #555;
        }

        input {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }

        input[type="submit"] {
            background-color: #4caf50;
            color: white;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $nome = $_POST["nome"];
        $cognome = $_POST["cognome"];
        $pezzi = $_POST["pezzi"];
    ?>
        <h2>Ciao, <?php echo $nome . " " . $cognome; ?>. Inserisci i dettagli per ogni pezzo nel carrello:</h2>
        
        <form action="cassa.php" method="post">
            <?php
            for ($i = 1; $i <= $pezzi; $i++) {
            ?>
                <label for="prodotto_<?php echo $i; ?>">Nome Prodotto <?php echo $i; ?>:</label>
                <input type="text" placeholder="ins nome prodotto" name="prodotto_<?php echo $i; ?>" required>

                <label for="prezzo_<?php echo $i; ?>">Prezzo Prodotto <?php echo $i; ?>:</label>
                <input type="text" placeholder="ins prezzo prodotto" name="prezzo_<?php echo $i; ?>" required><br>
            <?php
            }
            ?>
            <input type="hidden" name="nome" value="<?php echo $nome; ?>">
            <input type="hidden" name="cognome" value="<?php echo $cognome; ?>">
            <input type="hidden" name="pezzi" value="<?php echo $pezzi; ?>">

            <input type="submit" value="Pagamento">
        </form>
    <?php
    }
    ?>
</body>
</html>

