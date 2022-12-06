//creo un oggetto alunni che contiene nome, cognome, età, ect..
let alunni = {
    nome:"",
    cognome:"",
    eta:0
}

//inserisco i dati nell'oggetto che ho creato prima
alunni.nome = "Mario";
alunni.cognome = "Rossi";
alunni.eta = 14;

//creo un array della classe
let classe4C = new Array();

//inserisco l'ogetto (alunni) dentro l'array (classe4C)
classe4C.push(alunni)

//stampo in console un messaggio
const {cognome, nome} = alunni;
console.log(`Benvenuto ${cognome} ${nome}`) //devo utilizzare l'accento grave (`) (inserisco con  AltGr + accento)!