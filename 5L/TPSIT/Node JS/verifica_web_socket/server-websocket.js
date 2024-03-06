//Creo il server e lo metto in ascolto sulla porta 3000
const server = require("http").createServer().listen(3000);

//Qui salvo i prodotti
let prodotti = [];
//Qui salvo gli operatori
let operatori = {};

//Cors origin
const io = require('socket.io')(server, {
  cors: {
    origin: '*',
  }
});

//Quando il server è connesso
io.on('connection', (socketClient) => {

  //Quando viene aggiunto un nuovo operatore (nuova connessione) -->
  socketClient.on('aggiungiNome', (nomeOperatore) => {
      operatori[socketClient.id] = nomeOperatore;
      //.emit con 'listaOperatori' (aggiorna gli operatori connessi)
      io.emit('listaOperatori', Object.values(operatori));
  });

  //Quando viene aggiunto un prodotto -->
  socketClient.on('aggiungiProdotto', (prodotto) => {
      prodotto.operator = operatori[socketClient.id];
      prodotti.push(prodotto);
      //.emit con 'listaPrdotti' (aggiorna i prodotti e notifica gli utenti che sono state apportate delle modifiche)
      io.emit('listaProdotti', prodotti);
  });

  //Quando viene eliminato un prodotto -->
  socketClient.on('eliminaProdotto', (index) => {
      prodotti.splice(index, 1);
      //.emit con 'listaProdotti' (aggiorna i prodotti e notifica gli utenti che sono state apportate delle modifiche)
      io.emit('listaProdotti', prodotti);
  });

  //Invio la lista dei prodotti e degli operatori collegati al client (client.html) appena si connette
  socketClient.emit('listaProdotti', prodotti);
  socketClient.emit('listaOperatori', Object.values(operatori));
});
