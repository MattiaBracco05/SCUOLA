import React, { useEffect, useState } from 'react'
import './App.css'

const URL="https://raw.githubusercontent.com/itisrivoira/obelix/main/lista_locali.json"
let mieiLocali = new Array()

const App = () => {

//USE STATE dove salvo i locali, il testo (chiave di ricerca) e il risultato della ricerca
const [locali, setLocali] = useState([])
const [testo, setTesto] = useState([])
const [risultato, setRisultato] = useState([])

//FUNZIONE CONNESSIONE PER CONNETTERE IL JSON
const connessione =()=> {
  console.log("CONNESSIONE FILE JSON")
  //FETCH
  fetch(URL)

  //1 THEN --> TESTO IN JSON
  .then((testo) => testo.json())

  //2 THEN
  .then((mioJSON) => {
    //MAP (for each)
    mioJSON.map((elemento) => {
      mieiLocali.push(elemento)
    })

    //SALVO I LOCALI NELL'ARRAY
    setLocali(mieiLocali)
  })
}

//FUNZIONE RICERCA
const ricerca =(event)=> {
  console.log("RICERCA")
  setTesto(event.target.value)
}

//FUNZIONE CERCA
const cerca =()=> {

  //FILTER MI RITORNA UN ARRAY
  setRisultato(locali.filter((elemento) => {
      return elemento.nome == testo
    }))
}
  //RETURN --> Stampa a video
  return (
    <div>
      <h1>Ricerca locali</h1>
      
      {/* BUTTON PER CONNETTERE IL JSON */}
      <div>
        <input type="button" value={"CONNETTI"} className="buttonConnetti" onClick={connessione}/>
      </div>

      {/* RICERCA */}
      <div>
        {/* CASELLA DI RICERCA */}
        <input type="text" className="textCerca" placeholder='Inserisci il nome di un locale' onChange={ricerca}></input>
        {/* BUTTON CERCA */}
        <input type="button" value={"CERCA"} className="buttonCerca" onClick={cerca}/>
      </div>

      {/* Risultato */}
      {/* RISULATO - NOME*/}
      <div className='nomeLocale'>
        Nome locale: {risultato.length > 0 && risultato[0].nome}
      </div>
      {/* RISULTATO - INDIRIZZO*/}
      <div className='datiLocale'>
        Indirizzo: {risultato.length > 0 && risultato[0].indirizzo}
      </div>
      {/* RISULTATO -TELEFONO */}
      <div className='datiLocale'>
        Telefono: {risultato.length > 0 && risultato[0].telefono}
      </div>
      {/* RISULTATO - MAIL */}
      <div className='datiLocale'>
        Mail: {risultato.length > 0 && risultato[0].email}
      </div>

    </div>
  )
}

export default App