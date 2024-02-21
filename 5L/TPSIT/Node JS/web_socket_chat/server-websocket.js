const { EventEmitter } = require("stream")

//Creo il server
let server = require("http").createServer().listen("3000")

/*
Il modulo socket.io non ha la funzione ".listen()"
Lavora con il server (modulo http)
*/
let io = require("socket.io")(server, {
    
    //Do il permesso (a tutti i client ("*") di collegarsi al server)
    cors: {
        origin:"*"
    }
})

/*
Comunicazione del socket con client
".on" è una funzione per gestire gli eventi
*/
io.on("connection", (socketConClient) => {

    /*
    La funzione ".emit" ha 2 parametri:
    - il 1° è il nome dell'evento
    - il 2° è il parametro (messaggio)
    La funzione ".emit" lavora sempre con la funzione ".on" --> La funzione ".emit" crea l'evento e la funzione ".on" lo recupera
    */
    socketConClient.broadcast.emit("pippo", "Ciao, come stai?")

})
