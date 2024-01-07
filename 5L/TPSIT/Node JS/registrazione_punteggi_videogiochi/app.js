const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const port = 3000;

app.set("views", "./views");
app.set("view engine", "ejs");

//Per utilizzare il passaggio di parametri in POST
app.use(express.json());
app.use(express.urlencoded({
    extended: true
}))

//Dove salvo i punteggi registrati
let punteggi = [];

//Carico la pagina (template) del form
app.get('/', (req, res) => {
  res.render('form');
});

//Gestione dei dati inseriti nel form
app.post('/submit', (req, res) => {
    const nomeGioco = req.body.nomeGioco;
    const punteggioGioco = parseInt(req.body.punteggioGioco);

    //Cerco se il gioco è già stato registrato
    const registrato = punteggi.findIndex(item => item.nomeGioco === nomeGioco);

    //Se il gioco è già stato registrato -->
    if (registrato !== -1) {
        //Controllo se il punteggio è maggiore di quello già presente -->
        if (punteggi[registrato].punteggioGioco < punteggioGioco) {
            //Se sì --> aggiorno il punteggio (se no --> mantengo quello precedente)
            punteggi[registrato].punteggioGioco = punteggioGioco;
        }
    }

    //Altrimenti --> registro il gioco
    else {
        punteggi.push({ nomeGioco, punteggioGioco });
    }

    //Redrict ai risultati
    res.redirect('/risultati');
});

//Pagina di riepilogo dei punteggi
app.get('/risultati', (req, res) => {
  let maxpunteggioGioco = 0;
  let maxpunteggioGiocoGame = '';

  //Cerco il punteggio massimo e il relativo gioco
  punteggi.forEach(item => {
    if (item.punteggioGioco > maxpunteggioGioco) {
      maxpunteggioGioco = item.punteggioGioco;
      maxpunteggioGiocoGame = item.nomeGioco;
    }
  });

  //Carico la pagina (template) dei risultati
  res.render('risultati', { punteggi, maxpunteggioGioco, maxpunteggioGiocoGame });
});


//Avvio il server
app.listen(port, () => {
  console.log("Servizio in esecuzione sulla porta 3000");
});
