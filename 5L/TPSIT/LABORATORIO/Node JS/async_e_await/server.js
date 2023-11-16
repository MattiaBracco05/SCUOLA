//Questa funzione in realtà sara inserita in un modulo (non come in questo esempio nel file server.js)

/*
"async"
    - può essere usato su tutte le funzioni
    - async NON CREA FUNZIONI ASINCRONE!
*/
const somma = async()=> {

    /*
    "await"
        - può essere usato SOLO con le funzioni asincrone (come la fetch) e funziona solo con le funzoni async (come "somma" in questo caso)
        - await mi ritorna una promise
    */
    await fetch('https://v2.jokeapi.dev/joke/Programming')
    .then(res => res.json())
    .then(json => console.log(json.joke));
}

/*
Digitando "somma()." vedo che ho 3 opzioni disponibili:
    - .then --> stampo il mio nome (tramite un console log) dopo (then) aver eseguito tutta la funzione "somma"
    - .finally
    - .catch
*/
somma().then(console.log("Mattia Bracco"))