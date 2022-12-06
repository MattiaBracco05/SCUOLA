import React, { useState, useEffect } from 'react'
import "./Giacenza.css"

//URL DELFILE JSON
const URL = "https://raw.githubusercontent.com/andgio1976/maga/main/info"

//VARIABILE IN CUI SALVO I DATI DEL JSON
let mioDatabase = []

const Giacenza =()=> {
    
    //USE STATE
    const [giacenza, setGiacenza] = useState([])
    const [risultato, setRisultato] = useState([])
    const [testo, setTesto] = useState("")

    //USE EFFECT CHE RICHIAMA CONNESSIONE AUTOMATICAMENTE (evito di dover mettere un button per il collegamento)
    useEffect(() => {
        console.log("CONNESSIONE AL JSON");
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
            setGiacenza(mioDatabase)
        })
    }

    //FUNZIONE CERCA GIACENZA --> RICHIAMATA ALLA PRESSIONE DEL BUTTON
    const cercaGiacenza =()=> {
        console.log("FUNZIONE CERCA GIACENZA")
        setRisultato(giacenza.filter((elemento) => {
            return elemento.giacenza < 3
        }))
    }

    //FUNZIONE STAMPA --> CREA LA TABELLA
    const stampa =()=> {
        console.log("FUNZIONE STAMPA")

        if (risultato.length > 0) {
            return risultato.map((elemento) => {

                //creo la tabella
                return <div className='tabella'>

                    {/* CHIAVI TABELLA */}
                    <div>
                        <div className='tabGiacenzaHeader'>MARCA:</div>
                        <div className='tabGiacenzaHeader'>MODELLO:</div>
                        <div className='tabGiacenzaHeader'>GIACENZA:</div>
                        <div className='tabGiacenzaHeader'>PREZZO:</div>
                    </div>

                    {/* VALORI TABELLA */}
                    <div>
                        <div className='tabGiacenzaValue'>{elemento.marca}</div>
                        <div className='tabGiacenzaValue'>{elemento.modello}</div>
                        <div className='tabGiacenzaValue'>{elemento.giacenza}</div>
                        <div className='tabGiacenzaValue'>{elemento.prezzo}</div>
                    </div>
                </div>
                //chiudo la tabella
            })  
        }
    }

    return (
        <div>
            {/* TITOLO */}
            <div className='titoloGiacenza'>CERCA GIACENZE MINORI DI 3</div>

            {/* input */}
            <input type="button" className='buttonCercaGiacenza' value="VISUALIZZA GIACENZA" onClick={cercaGiacenza}/>

            {/* RISULATTAO */}
            <div>{risultato.length > 0 && stampa()}</div>

        </div>
    )
}

export default Giacenza