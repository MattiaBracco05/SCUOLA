<?php
    //Includo il file database.php
    include './database.php';

    //Controllo se provengo dal form, se sì -->
    if($_SERVER['REQUEST_METHOD'] == "POST"){
        //Ricavo i parametri inseriti dall'utente
        $nomeUtente = $_POST['nome'];
        $emailPost = $_POST['email'];

        //Inserisco l'utente appena creato
        $inserisciUtente = "INSERT INTO Utenti (Username, Email) VALUES ('$nomeUtente', '$emailPost');";

        //Collegamento al DB
        Database :: connessione();

        //Se è stato inserito --> mex di successo
        if(Database :: eseguiQuery($inserisciUtente)){
            echo "Utente Inserito con successo!";
        }
        //Altrimenti --> Messaggio di errore
        else {
            echo "Errore nell'inserimento dell'utente!";
        }

        //Ricarico la pagina ogni 1.5s
        header("refresh:1.5;url=../html/AggiungiUtenti.html");
    }

    //Altrimenti --> Messaggio di errore
    else {
        echo "Non provieni dal form!";
    }
?>