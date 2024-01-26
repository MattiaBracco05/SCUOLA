<center>
    <pre>
<?php
if (isset($_POST["btnInvia"])) {

    //Se perlomeno ha inserito il nome...
    if (!empty($_POST["nome"])) {
        session_start();
        echo "<p><pre>";
        print_r($_SESSION);
        echo "</pre></p>";

        //Se la persona inserita non è mai stata inserita -->
        if (!isset($_SESSION["disp"][$_POST["nome"]])) {

            //Se ho inserito almeno un giorno e un orario -->
            if (isset($_POST["giorni"]) && isset($_POST["orari"])) {
                $disponibilita = array();

                //Ciclo per il numero di giorni
                foreach ($_POST["giorni"] as $giorno) {
                    $disponibilita[$giorno] = $_POST["orari"];
                }
                $_SESSION["disp"][$_POST["nome"]] = $disponibilita;
                echo "Disponibilità di " . $_POST["nome"] . " AGGIUNTE.\n";
            }

            //Altrimenti --> Messaggio  di errore
            else {
                echo $_POST["nome"] . " NON SEI REGISTRATO,\nSE VUOI ESSERE"
                    . " REGISTRATO INSERISCI ALMENO\nUN GIORNO E UN ORARIO !\n\n";
                session_destroy();
            }
        }
        //Altrimenti (la persona inserita è gia registrata) -->
        else {
            $disponibilita = $_SESSION["disp"][$_POST["nome"]];

            //Se ho inserito il nome ma nessun giorno o orario --> cancello la persona
            if (!isset($_POST["giorni"]) && !isset($_POST["orari"])) {
                unset($_SESSION["disp"][$_POST["nome"]]);
                echo $_POST["nome"] . " È STATO CANCELLATO.\n";
            }

            //Altrimenti (ci sono dei gionri o degli orari settati) -->
            else {
                if (isset($_POST["giorni"])) {
                    foreach ($_POST["giorni"] as $giorno) {
                        //Se quel giorno non è settato --> lo aggiungo 
                        if (!isset($disponibilita[$giorno])) {
                            $disponibilita[$giorno] = $_POST["orari"];
                            echo "Aggiunte disponibilità di " . $_POST["nome"] . " per $giorno.\n";
                        }
                        //Altrimenti (giorno già settato) -->
                        else {
                            //Se ho inserito degli orari --> sovrascrivo gli orari precedenti
                            if (!isset($_POST["orari"])) {
                                unset($disponibilita[$giorno]);
                                echo "Eliminata la/e DISPONIBILITA' di " . $_POST["nome"] . " per $giorno\n";
                            }
                            //Altrimenti (orari non settati) --> cancello quel giorno
                            else {
                                if ($disponibilita[$giorno] != $_POST["orari"]) {
                                    $disponibilita[$giorno] = $_POST["orari"];
                                    echo "Disponibilità di " . $_POST["nome"] . " AGGIORNATE" . " per $giorno\n";
                                } else {
                                    echo "Disponibilità di " . $_POST["nome"] . " LASCIATE UGUALI" . " per $giorno\n";
                                }
                            }
                        }
                    }
                    //Se sono rimaste delle disponibilità in quel giorno -->
                    if (count($disponibilita) > 0) {
                        $_SESSION["disp"][$_POST["nome"]] = $disponibilita;
                    }
                    //Altrimenti (il giorno è rimasto senza disponibilità) --> lo cancello
                    else {
                        unset($_SESSION["disp"][$_POST["nome"]]);
                        echo $_POST["nome"] . " È STATO CANCELLATO.\n";
                    }
                }
                //Altrimenti (non ha inserito i giorni) --> Messaggio di errore
                else {
                    echo "Ehi dovresti inserire PERLOMENO i giorni !!!\n"
                        . "(a meno che tu non voglia cancellare la persona)\n";
                }
            }
        }
    }
    //Altrimenti (non ha inserito i dati) --> Messaggio di errore
    else {
        echo "DEVI INSERIRE I DATI !!!\n";
    }
}
//Altrimenti (non è arrivato dall'index) --> Messaggio di errore
else {
    echo "Come sei arrivato qui !?\n";
}

?>
<a href='index.html'>CLICCA PER TORNARE ALLA PAGINA INIZIALE</a><br>
<?php
//se avesse cancellato un nome dalla lista, e la lista è vuota
// non deve avere la possibilità di andare nel RIEPILOGO
if (isset($_SESSION["disp"])) {
    $qtaDisp = count($_SESSION["disp"]);
    if ($qtaDisp == 0) {
        session_destroy();
    } else {
        ?>
                <a href='riepilogo.php'>CLICCA PER ANDARE AL RIEPILOGO</a>
            <?php
    }
}
?>
</pre>
</center>