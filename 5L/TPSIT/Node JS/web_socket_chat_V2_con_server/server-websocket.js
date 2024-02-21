//Aggiunge un utente a una stanza (room)
//socket.join(room);

//Invia un messaggio al client
//socket.emit('hello', 'can you hear me?', 1, 2, 'abc');

//Invia un messaggio in broadcast (a tutti tranne il mittente)
//socket.broadcast.emit('broadcast', 'hello friends!');
 
//Invia un messaggio a tutti (compreso il mittente)
//socket.sockets.emit("msg", {"dato1":"prova","dato2":"messaggio"});

//Invio un messaggio a tutti gli utenti (tranne il mittente) presenti nella stanza (room) 'game'
//socket.to('game').emit('nice game', "let's play a game");

//Invio un messaggio a tutti gli utenti (tranne il mittente) presenti nelle stanze 'game1' and/or in 'game2'
//socket.to('game1').to('game2').emit('nice game', "let's play a game (too)");

//Invio un messaggio a tutti gli utenti (compreso il mittente) presenti nella stanza (room) 'game'
//io.in('game').emit('big-announcement', 'the game will start soon');

const server = require("http").createServer().listen(3000)

//Elenco (array) dove salverò i nickname delle persone presenti nella chat (globale)
let elencoNick = []

//Macro EVEN_CONNECTION
let EVEN_CONNECTION = "cnnection";

const io = require('socket.io')(server, {
  cors: {
    origin: '*',
  }
});

io.on("connection", (socketClient) => {
    socketClient.on("invionick", (dati) => {
        /*
        IF per il controllo se "elencoNick" include già i dati (nickname) (per la precisione controllo se non include (!) i dati)
        Se è cosi (True --> non include i dati) --> push dei dati (nickname) nell'array (elencoNick)
        */
        if (!elencoNick.includes(dati)) {
            elencoNick.push(dati)
        }
        //Console.log dei dati 
        console.log(dati)
        //Invio l'array con l'elenco dei nickname
        socketClient.emit("elenconick", elencoNick)
    })
})