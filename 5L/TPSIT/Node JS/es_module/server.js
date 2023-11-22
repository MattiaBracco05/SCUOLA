import http from "http"

/*
Posso importare le funzioni che solo mi servono elencandole nelle "{}"
Questo si chiama "destrutturazione"
*/

import {somma, differenza} from "./modulo.js"

/*
Nel file "package.json" alla riga 5 dichiaro come "type" "module"
Questo non deve esseredichiarato nello script! ma prima (per esempio dopo la descrizione (description))
*/

http.createServer((req, res) => {

    res.end(somma(5,7).toString())

}).listen(3000)