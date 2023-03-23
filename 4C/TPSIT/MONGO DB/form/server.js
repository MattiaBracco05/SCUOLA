//IMPORTO IL MODULO HTTP
let mioServer = require("http")

//CREO IL SERVER CHE RIMANE IN ASCOLTO SULLA PORTA 3000
mioServer.createServer((req, res) => {

    //SETTO L'HEADER PRIMA DI INVIARE IL PACCHETTO (dico al browser che payload contiene testo e html --> così facendo posso utilizzare i tag <strong></strong>)
    res.setHeader("content-type", "text/html")
    res.write("Mattia Bracco - Web Service")
    res.write("<form action='https://www.google.it' method='get'><input type='text' name='q'><input type='submit' value='INVIA'></form>")
    
    //MESSAGGIO DI RISPOSTA DAL SERVER
    res.end("<strong>IO SONO IL WEB SERVICE</strong>")
}).listen(3000)