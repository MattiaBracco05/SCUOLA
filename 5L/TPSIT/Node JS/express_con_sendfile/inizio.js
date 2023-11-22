//In questo caso non ho più bisogno di importare il modulo "http" in quanto uso già "express"
var express = require("express")

//Istaznio app
var app = new express ();

//Creo un middleware
app.get("/", (req, res) => {
    res.send("Benvenuto")
})

//Creo un 2° middleware per la 2° pagina del sito
app.get("/secondapagina", (req, res) => {
    res.sendFile(__dirname + "/index.html")
})

/*
Posso creare qaunti middleware voglio...
Posso crearli con:
    - GET --> digito la pagina nell'URL (127.0.0.1:3001/secondapagina)
    - POST --> l'utente passa dei parametri al server usanto method="POST"
    - USE
*/

/*
Istaznio il mio server
app.listen è una callback con il numero della porta su cui il servizio è attivo (nel mio caso ho scelto la 3001)
*/
var server = app.listen(3001, () => {

    //Console.log che mi dice che il server è in esecuzione sulla porta 3001
    console.log("Server in esecuzione sulla porta 3001")
})