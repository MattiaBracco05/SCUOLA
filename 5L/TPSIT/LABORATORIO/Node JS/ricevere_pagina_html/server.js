//IMPORTO IL MODULO HTTP
let mioServer = require("http")
let fs = require("fs")

//CREO IL SERVER CHE RIMANE IN ASCOLTO SULLA PORTA 3000
mioServer.createServer((req, res) => {
    today = new Date()

    //SETTO L'HEADER PRIMA DI INVIARE IL PACCHETTO (dico al browser che payload contiene testo e html --> così facendo posso utilizzare i tag <strong></strong>)
    res.setHeader("content-type", "text/html")
    let contenutoFile = fs.readFileSync("./index.html")
    
    //MESSAGGIO DI RISPOSTA DAL SERVER
    res.end(contenutoFile)
}).listen(3000)