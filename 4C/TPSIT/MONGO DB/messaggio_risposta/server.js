//IMPORTO IL MODULO HTTP
let mioServer = require("http")

//CREO IL SERVER CHE RIMANE IN ASCOLTO SULLA PORTA 3000
mioServer.createServer((primo, secondo) => {

    //SETTO L'HEADER PRIMA DI INVIARE IL PACCHETTO (dico al browser che payload contiene testo e html --> così facendo posso utilizzare i tag <strong></strong>)
    secondo.setHeader("content-type", "text/html")
    
    //MESSAGGIO DI RISPOSTA DAL SERVER
    secondo.end("<strong>CIAO IO SONO IL SERVER</strong>")
}).listen(3000)