import http from "http"
import url from "url"
import {somma, differenza, moltiplicazione, divisione} from "./modulo.js"

/*
Nel file "package.json" alla riga 5 dichiaro come "type" "module"
Questo non deve esseredichiarato nello script! ma prima (per esempio dopo la descrizione (description))
*/

http.createServer((req, res) => {

    let parametri = url.parse(req.url, true)
    let num1 = parseInt(parametri.query.num1)
    let num2 = parseInt(parametri.query.num2)
    let operazione = parametri.query.operazione
    console.log(num1)
    switch (operazione) {
        case "somma":
            res.end(somma(num1, num2).toString())
            break;
        case "differenza":
            res.end(differenza(num1, num2).toString())
            break;
        case "moltiplicazione":
            res.end(moltiplicazione(num1, num2).toString())
            break;
        case "divisione":
            res.end(divisione(num1, num2).toString())
            break;
        default:
            res.end("Errore")
            break;
    }
}).listen(3000)