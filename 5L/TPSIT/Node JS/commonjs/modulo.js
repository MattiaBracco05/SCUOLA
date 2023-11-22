//let pippo = 0 //Variabile locale al modulo

//Funzione SOMMA
const somma=(num1, num2) => {
    let totale = num1 + num2
    return (totale)
}

//Funzione DIFFERENZA
const differenza=(num1, num2) => {
    let totale = num1 - num2
    return (totale)
}

/*
In alterantiva posso dichiarae le funzioni con exports.{nomeDellaFunzione} al posto di const
In questo caso evito di inserire alla fine "module.exports{...}"
*/
module.exports={somma, differenza}