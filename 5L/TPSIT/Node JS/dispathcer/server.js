let http = require("http")
let url = require("url")

http.createServer((req, res) => {

    /*
    Dal momento che uso "True" --> ottengo un object literal --> posso accedere con .{nomeVariabile}
    Dal momento che uso "False" --> ottengo una stringa --> devo fare lo split...
    Di default l'impostazione è "False"
    */
    let mioURL = url.parse(req.url, true)

    //Switch sull'url
    switch (mioURL.path) {
        case "/":
            res.end("HOME PAGE")
            break;
        case "/pluto":
            res.end("PAGINA WEB PLUTO")
            break;
        case "/topolino":
            res.end("PAGINA WEB TOPOLINO")
            break;
        default:
            res.end("Messaggio 1")
            break;
    }
}).listen("3000")