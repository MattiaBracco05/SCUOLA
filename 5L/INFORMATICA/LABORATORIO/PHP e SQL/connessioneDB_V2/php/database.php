<?php
    //Parametri del DB
    class Database {
        private static $host = "localhost";
        private static $username = "root";
        private static $password = "";
        private static $database = "esConnDDLDMLQL";
        private static $connessione;

        //Metodo per la connessione al DB
        public static function connessione(){
            self :: $connessione = new mysqli(
                self :: $host, 
                self :: $username, 
                self :: $password, 
                self :: $database
            );
        }

        //Metodo esegui Query
        public static function eseguiQuery($query){
            $res = self :: $connessione -> query($query);

            if (!$res) {
                echo "Errore nella query: " . self :: $connessione -> error;
            }

            return $res;
        }

        //Metodo per creare le tabelle
        public static function creaTabelle($tabella){
            if(!self :: eseguiQuery($tabella)){
                echo "Errore nella creazione della tabella";
            } else {
                echo "Tabella creata con successo";
                echo "<br> <br>";
            }
        }

    }
?>