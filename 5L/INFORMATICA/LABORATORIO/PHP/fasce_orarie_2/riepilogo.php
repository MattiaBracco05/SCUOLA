<?php 
    //Avvio la sessione
    session_start();
    
    if (!isset($_SESSION["disp"])) {
        echo "<center><a href='index.html'>TORNA ALLA SCHERMATA" . " PRINCIPALE e REGISTRA QUALCHE DISPONIBILITA'</a></center>";
    }
    else {
        $contatori = array (
            "lunedi" => array (
                "9-11" => 0,
                "11-13" => 0,
                "14-16" => 0,
                "16-18" => 0,
            ),
            "martedi" => array (
                "9-11" => 0,
                "11-13" => 0,
                "14-16" => 0,
                "16-18" => 0,
            ),
            "mercoledi" => array (
                "9-11" => 0,
                "11-13" => 0,
                "14-16" => 0,
                "16-18" => 0,
            ),
            "giovedi" => array (
                "9-11" => 0,
                "11-13" => 0,
                "14-16" => 0,
                "16-18" => 0,
            ),
            "venerdi" => array (
                "9-11" => 0,
                "11-13" => 0,
                "14-16" => 0,
                "16-18" => 0,
            ),
        );
        
        $maxDisp = array();
        $qtaDisp = 0;
        //Ciclo per le persone che hanno dato disponibilità -->
        foreach ($_SESSION["disp"] as $arr_disp_persona) {

            //Ciclo per le disponibilità della persona (chiave => valore --> giorno => orario)
            foreach ($arr_disp_persona as $giorno => $arr_orari) {
                foreach ($arr_orari as $orario) {

                    //Aumento il contatore di quel orario in quel giorno
                    $contatori[$giorno][$orario] += 1;
                    $qta = $contatori[$giorno][$orario];
                    
                    //Se la disponibilità appena registrata è uguale alla disponibilità massima
                    if ($qta == $qtaDisp) {
                        //Mi salvo disponibilita
                        $qtaDisp = $qta;
                        //Aggiungo il giorno all'array delle massime disponibilità
                        $maxDisp[$giorno][$orario] = $qta;
                    }
                    //Altrimenti (se la disponibilità appena registrata è maggiore) -->
                    else if ($qta > $qtaDisp) {
                        //Resetto l'array
                        $maxDisp = array();
                        //Mi salvo la disponibilità
                        $qtaDisp = $qta;
                        //Mi salvo la disponibilità nelle disponibilità massime
                        $maxDisp[$giorno][$orario] = $qta;
                    }
                }
            }
        }
        
        //Creo l'array dove salvo le persone mancanti
        $riepilogoMancanti = array();
        
        //Ciclo per i giorni dove ci sono registrate delle disponibilità (chiave => valore --> giorno => orari)
        foreach ($maxDisp as $giorno => $orari) {
            //Inizializzo il contatore dei mancanti a 0
            $contatoreMancanti = 0;

            //Ciclo per gli orari dove sono registrate delle disponibilità (chiave => valore --> orario => disponibilità)
            foreach ($orari as $orario => $qtaDisp) {

                //Ciclo per le disponbilità delle persone
                foreach($_SESSION["disp"] as $persona => $disp){
                    
                    //Se la persona non ha disponibilità per questo giorno o non ha disponibilità per quest'ora -->
                    if (!isset($disp[$giorno]) || !in_array($orario, $disp[$giorno])) {
                        $riepilogoMancanti[$giorno][$orario][$contatoreMancanti] = $persona;
                    }
                    
                    //Altrimenti (non manca) -->
                    else{
                        //Serve per dire che non manvca nessuno
                        $riepilogoMancanti[$giorno][$orario][$contatoreMancanti] = null;
                    }

                    //Incremento il contatore dei mancanti
                    $contatoreMancanti++;
                } 
            }
        }
?>
<html>
    <head>
        <title>Riepilogo</title>
        <style>
            .giorni {
                text-align: left;
            }
            td {
                text-align: center;
            }
            #resetButton {
                position: absolute;
                right: 30px;
                width: 80px;
                height: 50px;
            }
        </style>
    </head>
    <body>
        <div style="position: absolute; top: 0px">
            <h4>Persone registrate:</h4>
            <ul>
        <?php 
            foreach(array_keys($_SESSION["disp"]) as $persona ){
                echo "<li>".$persona."</li>";
            }
        ?>
            </ul>
        </div>
        <center>
            <button id="resetButton"><a href="resettaSessione.php">Resetta tabella</a></button>
            <table border="1px">
                <tr>
                    <td></td>
                    <th>9 - 11</th>
                    <th>11 - 13</th>
                    <th>14 - 16</th>
                    <th>16 - 18</th>
                </tr>
                <tr>
                    <th class="giorni">Lunedi</th>
                    <td><?php echo $contatori["lunedi"]["9-11"]; ?></td>
                    <td><?php echo $contatori["lunedi"]["11-13"]; ?></td>
                    <td><?php echo $contatori["lunedi"]["14-16"]; ?></td>
                    <td><?php echo $contatori["lunedi"]["16-18"]; ?></td>
                </tr>
                <tr>
                    <th class="giorni">Martedi</th>
                    <td><?php echo $contatori["martedi"]["9-11"]; ?></td>
                    <td><?php echo $contatori["martedi"]["11-13"]; ?></td>
                    <td><?php echo $contatori["martedi"]["14-16"]; ?></td>
                    <td><?php echo $contatori["martedi"]["16-18"]; ?></td>
                </tr>
                <tr>
                    <th class="giorni">Mercoledi</th>
                    <td><?php echo $contatori["mercoledi"]["9-11"]; ?></td>
                    <td><?php echo $contatori["mercoledi"]["11-13"]; ?></td>
                    <td><?php echo $contatori["mercoledi"]["14-16"]; ?></td>
                    <td><?php echo $contatori["mercoledi"]["16-18"]; ?></td>
                </tr>
                <tr>
                    <th class="giorni">Giovedi</th>
                    <td><?php echo $contatori["giovedi"]["9-11"]; ?></td>
                    <td><?php echo $contatori["giovedi"]["11-13"]; ?></td>
                    <td><?php echo $contatori["giovedi"]["14-16"]; ?></td>
                    <td><?php echo $contatori["giovedi"]["16-18"]; ?></td>
                </tr>
                <tr>
                    <th class="giorni">Venerdi</th>
                    <td><?php echo $contatori["venerdi"]["9-11"]; ?></td>
                    <td><?php echo $contatori["venerdi"]["11-13"]; ?></td>
                    <td><?php echo $contatori["venerdi"]["14-16"]; ?></td>
                    <td><?php echo $contatori["venerdi"]["16-18"]; ?></td>
                </tr>
            </table>
            <h2>Fasce con massime disponibilita</h2>
            <div style="font-family: cursive">
            <?php 
                foreach($riepilogoMancanti as $giorno => $orari){
                    foreach($orari as $orario => $persone){
                        echo "<b>$giorno</b> alle <b>$orario</b><br />";
                        $contatoreMancanti = 0;

                        foreach($persone as $persona){
                            if($persona != null){
                                echo "Manca $persona\n";
                                $contatoreMancanti++;
                            }
                        }
                        if($contatoreMancanti == 0){ echo "Non manca nessuno.<br />";
                        }else{ echo "<br /><br />"; }
                    }
                }
            ?>
            </div>
            <br><br>
            <a href="index.html">REGISTRA UNA NUOVA DISPONIBILITA'</a>
        </center>
    </body>
</html>
<?php 
    }
?>
