<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sterlina Market</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            text-align: center;
            padding: 20px;
        }

        h1 {
            color: #333;
        }

        form {
            max-width: 400px;
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
    <h1>Benvenuto al Sterlina Market</h1>

    <form action="carrello.php" method="post">
        <label for="nome">Nome:</label>
        <input type="text" name="nome" placeholder="inserisci il nome" required>

        <label for="cognome">Cognome:</label>
        <input type="text" name="cognome" placeholder="inserisci il cognome" required>

        <label for="pezzi">Numero di pezzi nel carrello:</label>
        <input type="text" name="pezzi" placeholder="inserisci il numero di articoli" required>

        <input type="submit" value="Vai alla cassa">
    </form>
</body>
</html>

