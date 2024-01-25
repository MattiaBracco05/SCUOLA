const express = require("express");
const app = express();
const port = 3000;

app.set("views", "./views");
app.set("view engine", "ejs");

//Implemento la funzione
app.get("/", (req, res) => {
    const dati = "Mattia Bracco"
    
    /*
    Il 1° parametro è il file del mio template (index.ejs) scritto senza esetnzione (senza .ejs)
    Il 2° parametro è un object literal con i dati da passare ( {variabile : valore} ) 
    */
    res.render("index", {variabile : dati})
});

//Avvio il server
app.listen(port, () => {
    console.log("Servizio in esecuzione sulla porta 3000")
})