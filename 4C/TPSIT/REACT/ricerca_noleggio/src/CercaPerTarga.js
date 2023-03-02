import React, { useEffect, useState } from 'react'

const URL = "https://raw.githubusercontent.com/andgio1976/autonoleggio/main/dati"
let mieiVeicoli = new Array()

const CercaPerTarga = () => {

    //USE STATE
    const [nomeRicerca, setNomeRicerca] = useState('');
    const [risultato, setRisulatato] = useState([])

    //USE EFFECT PER LA CONNESSIONE
    useEffect(() => {
        connessione();
        }, [])

    const connessione =()=> {
        console.log("CONNESSIONE FILE JSON")
        //FETCH
        fetch(URL)
            .then((testo) => testo.json())
            .then((mioJSON) => {

                //COMANDO MAP --> ciclo per il numero di città presenti nel file JSON
                mioJSON.map((element, index) => {
                    mieiVeicoli.push(element)
                })
            })
      }

      console.log(mieiVeicoli)

    //FUNZIONE alertNome (RICHIAMATA ALLA PRESSIONE DEL BUTTON CONFERMA)
    const alertNome = (event) => {
        event.preventDefault();
        alert(`Targa inserita: ${nomeRicerca}`);

        //Ciclo per i veivoli
        let flag = 0
        var prezzo = 0
        //console.log(veicoli)
        for (var i=0; i<8; i++) {
            console.log("*****Sono dentro al ciclo for*****")

            //Controllo se la targa corrisponde --> se corrisponde stampo i dati
            if (nomeRicerca == mieiVeicoli[i].targa) {
                console.log("veicolo trovato")
                flag = 1;
                prezzo = prezzo + mieiVeicoli[i].tariffa * mieiVeicoli[i].cliente.giorni
                setRisulatato([...risultato,
                    <div class="row justify-content-center mt-3">
                        <div class="col-12">Nome: {mieiVeicoli[i].cliente.nome} Cognome: {mieiVeicoli[i].cliente.cognome} Anno: {mieiVeicoli[i].cliente.anno}</div>
                        <div class="col-12">Marca: {mieiVeicoli[i].marca} Modello: {mieiVeicoli[i].modello} Tariffa: {mieiVeicoli[i].tariffa}</div>
                    </div>])
            }
        }

        //Se la targa non è stata trovata --> messaggio di errore
        if (flag == 0) {
            setRisulatato([
                <div class="row justify-content-center mt-3">
                    <div class="col-12">Targa non trovata</div>
                </div>])
        } else {
            setRisulatato([...risultato,
                <div class="row justify-content-center mt-3">
                    <div class="col-12">Prezzo noleggio: {prezzo}€</div>
                </div>])
        }

    }

    //RETURN --> Stampa a video
    return (
        <div>
            <h1>Cerca per targa</h1>
            {/* FORM */}
            <form onSubmit={alertNome}>

                {/* INPUT TEXT */}
                <label>
                    <input type="text" value={nomeRicerca} placeholder={"Inserisci una targa"} onChange={(e) => setNomeRicerca(e.target.value)} />
                </label>
                {/* BUTTON PER CONFERMARE */}
                <input type="submit" value={"CONFERMA"} />

                {/* RISULTATO */}
                {risultato}

            </form>
        </div>
  )
}

export default CercaPerTarga