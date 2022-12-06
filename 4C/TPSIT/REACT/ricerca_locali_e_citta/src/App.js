import React, { useEffect, useState } from 'react'
import './App.css'

const URL="https://raw.githubusercontent.com/itisrivoira/obelix/main/lista_locali.json"
let mieiLocali = new Array()

const App = () => {

//USE STATE
const [locali, setLocali] = useState([])
const [testoLocale, setTestoLocale] = useState([])
const [testoCitta, setTestoCitta] = useState("")
const [risultatoLocale, setRisultatoLocale] = useState([])
const [risultatoCitta, setRisultatoCitta] = useState([])

useEffect(() => {
  connessione();
  }, [])

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
const ricercaLocale =(event)=> {
  console.log("RICERCA")
  setTestoLocale(event.target.value)
}

//FUNZIONE RICERCA 2
const ricercaCitta =(event)=> {
  setTestoCitta(event.target.value)
}

//FUNZIONE CERCA LOCALE
const cercaLocale =()=> {

  //FILTER MI RITORNA UN ARRAY
  setRisultatoLocale(locali.filter((elemento) => {
      return elemento.nome == testoLocale
    }))
}

//FUNZIONE CERCA CITTÀ
const cercaCitta =()=> {
  setRisultatoCitta(locali.filter((elemento)=>{
    return elemento.citta == testoCitta
  }))
}

const stampa=()=>{
  return risultatoCitta.map((elemento,indice)=>{
    return <div key={indice}>{elemento.nome}</div>
  })
}

  return (
    <div>
      <div>
        {/* ----- CASELLA DI RICERCALOCALE ----- */}
        <input type="text" className="textCerca" placeholder='Inserisci il nome di un locale' onChange={ricercaLocale}></input>
        {/* ----- BUTTON PER CERCARE LOCALE ----- */}
        <input type="button" value={"CERCA LOCALE"} className="buttonCerca" onClick={cercaLocale}/>
        {/* ----- CASELLA DI RICERCA CITTÀ ----- */}
        <input type="text" className="textCerca" placeholder='Inserisci il nome di una città' onChange={ricercaCitta}></input>
        {/* ----- BUTTON PER CERCARE CITTÀ ----- */}
        <input type="button" value={"CERCA CITTÀ"} className="buttonCerca" onClick={cercaCitta}/>
      </div>

      {/* RISULATO - NOME*/}
      <div className='nomeLocale'>
        {risultatoLocale.length > 0 && "Nome locale: " + risultatoLocale[0].nome}
      </div>
      {/* RISULTATO - INDIRIZZO*/}
      <div className='datiLocale'>
        {risultatoLocale.length > 0 && "Indirizzo: " + risultatoLocale[0].indirizzo}
      </div>
      {/* RISULTATO -TELEFONO */}
      <div className='datiLocale'>
        {risultatoLocale.length > 0 && "Telefono: " + risultatoLocale[0].telefono}
      </div>
      {/* RISULTATO - MAIL */}
      <div className='datiLocale'>
        {risultatoLocale.length > 0 && "Mail: " + risultatoLocale[0].email}
      </div>
      <div className='elencoLocali'>
        <div className='titolo'>LOCALI NELLA CITTÀ RICERCATA:</div>
        {stampa()}
      </div>
    </div>
  )
}

export default App