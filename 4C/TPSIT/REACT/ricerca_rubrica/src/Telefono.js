import React, { useState, useEffect } from 'react'
import "./Telefono.css"

const URL = "https://raw.githubusercontent.com/andgio1976/rubrica/main/json"
let miePersone = []

const Telefono =()=> {
    const [persone, setPersone] = useState([])
    const [ris, setRis] = useState([])
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

    //FUNZIONE INSERISCI NUMERO --> AGGIORNA QUANDO SCRIVO TESTO IN INPUT
    const insNumero =(event)=> {
        setTesto(event.target.value)
    }

    //FUNZIONE CERCA NUMERO --> RICHIAMATA ALLA PRESSIONE DEL BUTTON
    const cercaNumero =()=> {
        if (testo.length == 0 || testo.length < 10) {
            alert("Inserisci il numero di telefono valido")
        } else {
            setRis(persone.filter((elemento) => {
                return elemento.Telefono == testo
            }))
        }
    }

    //FUNZIONE STAMPA --> CREA LA TABELLA
    const stampa =()=> {
        if (ris.length > 0) {
            return <div className='tabella'>
                <div>
                    <div className='tabHeader'>NOME:</div>
                    <div className='tabHeader'>COGNOME:</div>
                    <div className='tabHeader'>TELEFONO:</div>
                </div>
                <div>
                    <div className='tabValue'>{ris[0].nome}</div>
                    <div className='tabValue'>{ris[0].cognome}</div>
                    <div className='tabValue'>{ris[0].Telefono}</div>
                </div>
            </div>
        }
    }

    return (
        <div>
            {/* TITOLO */}
            <div className='titolo'>CERCA TELEFONO</div>
            
            {/* INPUT */}
            <input type="text" className='textCerca' placeholder="Inserisci numero di telefono" onChange={insNumero}/>
            <input type="button" className='buttonCercaNumero'value="CERCA TELEFONO" onClick={cercaNumero}/>
            
            {/* STAMPA */}
            <div>{stampa()}</div>
        </div>
  )
}

export default Telefono