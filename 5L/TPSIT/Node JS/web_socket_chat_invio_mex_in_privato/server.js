// http://172.10.197.70:3000
const server=require("http").createServer().listen(3000)
let elencoNick = []
let elencoMsg = []
const EVENT_CONNECTION = "connection";
const EVENT_SENDNICK = "invionick";
const EVENT_LISTNICK = "elenconick";
const EVENT_SENDMSG = "inviamsg";
const EVENT_LISTMSG = "elencomsg";


const io = require('socket.io')(server, {
  cors: {
    origin: '*',
  }
});

io.on(EVENT_CONNECTION ,(socketClient)=>{
    socketClient.on(EVENT_SENDNICK,(nick)=>{
      if(!elencoNick.includes(nick)){
        elencoNick.push(nick)
      }
      //   console.log("NickName: " + nick)
      socketClient.broadcast.emit(EVENT_LISTNICK ,elencoNick)
    }) 
    socketClient.on(EVENT_SENDMSG,(msg)=>{
      
        console.log("Message ricevuto: " + socketClient.handshake.address + " : " + msg.nickName + " " + msg.message )
        // console.log("elencoMsg lungo: " + elencoMsg.length)
        elencoMsg.push(msg)
        // console.log("elencoMsg lungo: " + elencoMsg.length)
        for (let index = 0; index < elencoMsg.length; index++) {
          console.log("nickname " + elencoMsg[index].nickName + " message: " + elencoMsg[index].message)     
        }
        socketClient.broadcast.emit(EVENT_LISTMSG ,elencoMsg)
      }) 
})