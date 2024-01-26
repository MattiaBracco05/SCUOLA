<?php
    //Avvio la sessione
    session_start();
    //Distruggo la sessione
    session_destroy();
    //Vado al file index.html
    header("Location:index.html");
?>