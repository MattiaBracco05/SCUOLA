import React, { useState, useEffect } from 'react'
import "./Prefisso.css"

const URL = "https://raw.githubusercontent.com/andgio1976/rubrica/main/json"

let miePersone = []

const Prefisso =()=> {
    const [persone, setPersone] = useState([])
    const [risultato, setRisultato] = useState([])
    const [testo, setTesto] = useState("")

    //USE EFFECT CHE RICHIAMA CONNESSIONE
    useEffect(() => {
        connessione();
    }, [])
      
    //FUNZIONE CONNESSIONE --> DOWNLOAD E PARSING JSON
    const connessione =()=> {
        fetch(URL)
        .then((testo) => testo.json())
        .then((mioJSON) => {
            mioJSON.map((elemento) => {
                miePersone.push(elemento)
            })
            setPersone(miePersone)
        })
    }

    //FUNZIONE INSERISCI PREFISSO --> AGGIORNA QUANDO SCRIVO TESTO IN INPUT
    const insPrefisso=(event) => {
        setTesto(event.target.value)
    }

    //FUNZIONE CERCA PREFISSO --> RICHIAMATA ALLA PRESSIONE DEL BUTTON
    const cercaPrefisso =()=> {
        setRisultato(persone.filter((elemento) => {
            return (elemento.Telefono[0] + elemento.Telefono[1] + elemento.Telefono[2] + elemento.Telefono[3]) == testo
        }))
    }

    //FUNZIONE STAMPA --> CREA LA TABELLA
    const stampa=()=> {
        if (risultato.length > 0) {
            return risultato.map((elemento) => {
                return <div className='tabella'>
                    {/* CHIAVI TABELLA */}
                    <div>
                        <div className='tabHeader'>NOME:</div>
                        <div className='tabHeader'>COGNOME:</div>
                        <div className='tabHeader'>TELEFONO:</div>
                        <div className='tabHeader'>CITTÀ:</div>
                    </div>
                    {/* VALORI TABELLA */}
                    <div>
                        <div className='tabValue'>{elemento.nome}</div>
                        <div className='tabValue'>{elemento.cognome}</div>
                        <div className='tabValue'>{elemento.Telefono}</div>
                        <div className='tabValue'>{elemento.citta}</div>
                    </div>
                </div>
            })  
        }
    }

    return (
        <div>
            {/* TITOLO */}
            <div className='titolo'>CERCA PREFISSO</div>

            {/* input */}
            <input type="text" className='textCerca' placeholder="Inserisci prefisso" onChange={insPrefisso}/>
            <input type="button" className='buttonCercaPrefisso' value="CERCA PREFISSO" onClick={cercaPrefisso}/>

            {/* RISULATTAO */}
            <div>{risultato.length > 0 && stampa()}</div>

        </div>
    )
}

export default Prefisso