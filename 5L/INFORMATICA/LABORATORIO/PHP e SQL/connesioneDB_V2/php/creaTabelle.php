<?php
    //Includo il file database.php
    include './database.php';

    //Controllo se provengo dal form, se sì -->
    if($_SERVER['REQUEST_METHOD'] == "POST"){

        //Creo la tabella utenti
        $tabellaUtenti = "CREATE TABLE IF NOT EXISTS Utenti (
            ID INT AUTO_INCREMENT,
            Username VARCHAR(25) NOT NULL,
            Email VARCHAR(25) NOT NULL,
            PRIMARY KEY (ID)
        );";

        //Creo la tabella post
        $tabellaPost = "CREATE TABLE IF NOT EXISTS Post (
            ID INT AUTO_INCREMENT,
            UserID INT,
            Titolo VARCHAR(25) NOT NULL,
            Messaggio TEXT NOT NULL,
            PRIMARY KEY (ID),
            FOREIGN KEY (userID) REFERENCES Utenti(ID)
        );";

        //Connessione al DB
        Database :: connessione();

        //Creo la tabella utenti
        Database :: creaTabelle($tabellaUtenti);
        //Creo la tabella post
        Database :: creaTabelle($tabellaPost);
        
        //Ricarico la pagina ogni 1.5s
        header("refresh:1.5;url=../index.html");
    }

    //Altrimenti --> Messaggio di errore
    else {
        echo "Non provieni dal form!";
    }
?>