//Posso creare un array con le parentesi quadre "[]"
let nome = []

//Posso creare un array con il comando "new Array()"
let cognome = new Array()

//Posso creare un array contenente un object literal
let nome2 = new Array({nome: "Mario", cognome:"Rossi", eta:20})

//-----------------------------------------------------------------------------------------------------------------------------------

/*
Per stampare i valori devo usare la poszione "[0]" perchè si tratta di un array (contenente con Object Literal)
in seguito usare ".nome" per stampare il dato che voglio (nel mio caso nome)
*/
console.log(nome2[0].nome)

//Creo il mio object literal (da caricare sull'array)
let mioObjectLiteral = {
    nome: "Luca",
    cognome: "Bianchi",
    eta: 45
    //Inserisco tutte le informazioni di cui ho bisogno...
}

//Aggiungo il mio object literal in coda all'array (nome 2)
nome2.push(mioObjectLiteral)

//-----------------------------------------------------------------------------------------------------------------------------------