let http = require("http")

//Importo il mio modulo
let mioModulo = require("./modulo")

http.createServer((req, res) => {

    //Richiamo la funzione somma presente nel mio modulo richiamato come "mioModulo", utilizzo "toString" per vedere a video il risultato (altrimenti da errore)
    res.end(mioModulo.somma(5,7).toString())

}).listen(3000)