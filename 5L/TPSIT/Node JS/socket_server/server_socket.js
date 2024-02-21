const net = require ("net")

net.createServer(
    (socket) => {

        socket.write("CIAO")

        /*
        Socket.on --> serve per gestire gli eventi
        come con JavaScript c'erano le azioni onClick, onChange...
        Viene richiamata la funzione callback che contiene il messaggio (msg)
        */
        socket.on("data", (msg)=> {

            /*
            Stampo la mia porta + il messaggio
            (toString mi serve per vedere il messaggio e non caratteri strani)
            */
            console.log(socket.remotePort + " " + msg.toString())
        })

//Il 1° parametro è la porta, il secondo è l'indirizzo IP (localhost)
}).listen(3000, "127.0.0.1")


/*
Per vedere il server da un altro computer nella stessa rete:
- Avvio Putty
- Seleziono Telnet
- Metto l'indirizzo IP (IP del prof: 172.10.196.244)
- Metto la porta
- Clicco su "Open" (o premo INVIO)
*/