<?php
    //Includo il file database.php
    include './database.php';

    //Controllo se provengo dal form, se sì -->
    if($_SERVER['REQUEST_METHOD'] == "POST"){
        //Ricavo i parametri inseriti dall'utente
        $IDUtente = $_POST['ID'];
        $titoloPost = $_POST['titolo'];
        $contenutoPost = $_POST['contenuto'];

        //Aggiungo il post appena creato
        $inserisciPost = "INSERT INTO Post (UserID, Titolo, Messaggio) VALUES ('$IDUtente', '$titoloPost', '$contenutoPost');";

        //Collegamento al DB
        Database :: connessione();

        //Se è stato inserito --> mex di successo
        if(Database :: eseguiQuery($inserisciPost)){
            echo "Post Inserito con successo!";
        }
        //Altrimenti --> Messaggio di errore
        else {
            echo "Errore nell'inserimento del post!";
        }

        //Ricarico la pagina ogni 1.5s
        header("refresh:1.5;url=../html/AggiungiPost.html");
    }

    //Altrimenti --> Messaggio di errore
    else {
        echo "Non provieni dal form!";
    }
?>