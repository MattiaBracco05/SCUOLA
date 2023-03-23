//IMPORTO IL MODULO HTTP
let mioServer = require("http")

//CREO IL SERVER CHE RIMANE IN ASCOLTO SULLA PORTA 3000
mioServer.createServer((req, res) => {
    today = new Date()

    //SETTO L'HEADER PRIMA DI INVIARE IL PACCHETTO (dico al browser che payload contiene testo e html --> così facendo posso utilizzare i tag <strong></strong>)
    res.setHeader("content-type", "text/html")
    res.write("Giorno della settimana: " + today.getDay() + " | \n")
    res.write("Data: " + today.getDate() + "/" + today.getMonth() + "/" + today.getFullYear() + " | \n")
    res.write("Ora: " + today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds() + " | \n")


    //MESSAGGIO DI RISPOSTA DAL SERVER
    res.end("<strong>IO SONO IL WEB SERVICE</strong>")
}).listen(3000)