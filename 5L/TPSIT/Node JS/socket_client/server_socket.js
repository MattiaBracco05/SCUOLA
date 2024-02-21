const net = require ("net")

/*
Il 1° parametro è la porta
Il 2° parametro è l'indirizzo IP
Il 3° parametro è una funzione callback ( () => {} )
*/
const mioSocket = net.connect(4000, "127.0.0.1", () => {
        console.log("CLIENT COLLEGATO")
    })

    mioSocket.write("Ciaooo")
    mioSocket.on("data", (msg) => {

})