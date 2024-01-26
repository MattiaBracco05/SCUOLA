<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Raccolta Disponibilità</title>

    <!-- Inizio CSS per la grafica -->
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        form {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        h2 {
            text-align: center;
            color: #333;
        }

        label {
            display: block;
            margin-bottom: 8px;
            color: #555;
        }

        input[type="text"],
        select {
            width: 100%;
            padding: 8px;
            margin-bottom: 16px;
            box-sizing: border-box;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        select[multiple] {
            height: 100px;
        }

        input[type="submit"] {
            background-color: #4caf50;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }

        input[type="submit"]:hover {
            background-color: #45a049;
        }
    </style>
    <!-- Fine CSS per la grafica -->

</head>

<body>

    <h2>Form raccolta disponibilità</h2>

    <!-- Inizio del form -->
    <form action="process.php" method="post">

        <!-- Label del nome -->
        <label for="name">Nome:</label>
        <!-- Input del nome -->
        <input type="text" name="name" placeholder="Inserire nome partecipante" required>

        <!-- Label dei giorni -->
        <label for="days[]">Giorni della settimana:</label>
        <!-- Select dei giorni -->
        <select name="days[]" multiple required>
            <?php
            $days = ['Lunedì', 'Martedì', 'Mercoledì', 'Giovedì', 'Venerdì'];
            foreach ($days as $day) {
                echo "<option value='$day'>$day</option>";
            }
            ?>
        </select>

        <!-- Label della fascia oraria -->
        <label for="times[]">Fasce orarie:</label>
        <!-- Select della fascia oraria -->
        <select name="times[]" multiple required>
            <?php
            $times = ['9-11', '11-13', '14-16', '16-18'];
            foreach ($times as $time) {
                echo "<option value='$time'>$time</option>";
            }
            ?>
        </select>

        <!-- Button submit per inviare i dati del form -->
        <input type="submit" value="INVIA">

    </form>
    <!-- Fine del form -->

</body>

</html>