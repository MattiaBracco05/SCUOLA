const express = require("express");
const app = express();
const port = 3000;

app.set("views", "./views");
app.set("view engine", "ejs");

//PER UTILIZZARE I PARAMETRI IN POST
/*
Per parsare il JSON
Io ho una stringa --> la trasformo in JSON
Così posso scrivere ".nome", ".cognome", ecc. altrimenti dovrei fare la split
*/
app.use(express.json());
app.use(express.urlencoded({
    extended: true
}))


//Implemento la funzione (sta volta è APP.POST))
app.post("/recupera", (req, res) => {
    let persona = {
        nome: req.body.nome,
        cognome: req.body.cognome,
        CF: req.body.CF
    }
    /*
    Il 1° parametro è il file del mio template (index.ejs) scritto senza esetnzione (senza .ejs)
    Il 2° parametro è un object literal con i dati da passare ( {variabile : valore} ) 
    */
    res.render("index", {variabile : persona})
});

//Avvio il server
app.listen(port, () => {
    console.log("Servizio in esecuzione sulla porta 3000")
})