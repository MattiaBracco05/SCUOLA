import React, { useState, useEffect } from 'react'
import "./Marca.css"

//URL DEL FILE JSON
const URL = "https://raw.githubusercontent.com/andgio1976/maga/main/info"

//VARIABILE IN CUI SALVO I DATI DEL JSON
let mioDatabase = []

const Marca =()=> {

    //USE STATE
    const [marca, setMarca] = useState([])
    const [risultato, setRisultato] = useState([])
    const [testo, setTesto] = useState("")

    //USE EFFECT CHE RICHIAMA CONNESSIONE AUTOMATICAMENTE (evito di dover mettere un button per il collegamento)
    useEffect(() => {
        console.log("CONNESSIONE L JSON")
        connessione();
    }, [])
      
    //FUNZIONE CONNESSIONE --> DOWNLOAD E PARSING JSON
    const connessione =()=> {

        //FETCH (Asincrona) --> il codice sottostante alla fetch viene eseguito parallelamente
        fetch(URL)

        //1° THEN --> Ottengo testo.json
        .then((testo) => testo.json())

        //2° THEN --> Comando MAP
        .then((mioJSON) => {
            mioJSON.map((elemento) => {
                mioDatabase.push(elemento)
            })
            setMarca(mioDatabase)
        })
    }

    //FUNZIONE INSERISCI MARCA --> AGGIORNA QUANDO SCRIVO TESTO IN INPUT
    const insMarca =(event)=> {
        console.log("FUNZIONE INSERISCI MARCA")
        setTesto(event.target.value)
    }

    //FUNZIONE CERCA MARCA --> RICHIAMATA ALLA PRESSIONE DEL BUTTON
    const cercaMarca =()=> {
        console.log("FUNZIONE CERCA MARCA")

        //Controllo che l'utente non abbia lasciato la casella di ricerca vuota altrimenti --> ALERT
        if (testo.length == 0) {
            alert("ERRORE! La casella di ricerca non può essere vuota")
        }

        //Se la casella non è vuota --> filtro le marce andando a ricercare quella inserita
        else {
            setRisultato(marca.filter((elemento) => {
                return elemento.marca == testo
            }))
        }
    }

    //FUNZIONE STAMPA --> CREA LA TABELLA
    const stampa =()=> {
        console.log("FUNZIONE STAMPA")

        //Controllo che ci sia un risultato
        if (risultato.length > 0) {
            
            //MAP mi serve per stampare tutti i prodotti nel caso di più prodotti dello stesso costruttore (es. "Asus")
            return risultato.map((elemento) => {
                
                //creo la tabella
                return <div className='tabella'>

                    {/* VOCI DELLA TABELLA */}
                    <div>
                        <div className='tabMarcaHeader'>MARCA:</div>
                        <div className='tabMarcaHeader'>MODELLO:</div>
                        <div className='tabMarcaHeader'>GIACENZA:</div>
                        <div className='tabMarcaHeader'>PREZZO:</div>
                    </div>

                    {/* VALORI DELLA TABELLA */}
                    <div>
                        <div className='tabMarcaValue'>{risultato[0].marca}</div>
                        <div className='tabMarcaValue'>{risultato[0].modello}</div>
                        <div className='tabMarcaValue'>{risultato[0].giacenza}</div>
                        <div className='tabMarcaValue'>{risultato[0].prezzo}</div>
                    </div>

                </div>
                //chiudo la tabella
            })  
        }
    }

    return (
        <div>
            {/* TITOLO */}
            <div className='titoloMarca'>CERCA MARCA</div>
            
            {/* INPUT */}
            <input type="text" className='textCerca' placeholder="Inserisci una marca" onChange={insMarca}/>
            <input type="button" className='buttonCercaMarca'value="CERCA MARCA" onClick={cercaMarca}/>
            
            {/* STAMPA */}
            <div>{stampa()}</div>
        </div>
  )
}

export default Marca