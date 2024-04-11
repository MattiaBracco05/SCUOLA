<?php
    //Includo il file database.php
    include './database.php';

    //Controllo se provengo dal form, se sì -->
    if ($_SERVER['REQUEST_METHOD'] == "POST") {

        //Elimino le tabelle
        $tabellaUtenti = "DROP TABLE IF EXISTS Utenti;";
        $tabellaPost = "DROP TABLE IF EXISTS Post;";

        //Connessione al DB
        Database :: connessione();

        //TABELLA POST
        //Se sono state eliminate --> mex di successo
        if (Database :: eseguiQuery($tabellaPost)) {
            echo "Tabella Post eliminata con successo!";
        }
        //Altrimenti --> Messaggio di errore
        else {
            echo "Tabella Posts impossibile da eliminare!";
        }

        echo "<br> <br>";

        //TABELLA UTENTI
        //Se sono state eliminate --> mex di successo
        if (Database :: eseguiQuery($tabellaUtenti)) {
            echo "Tabella user eliminata con successo!";
        }
        //Altrimenti --> Messaggio di errore
        else {
            echo "Tabella user impossibile da eliminare!";
        }

        //Ricarico la pagina ogni 1.5s
        header("refresh:1.5;url=../index.html");
    } 
    
    //Altrimenti --> Messaggio di errore
    else {
        echo "Non vieni dal form!";
    }
?>