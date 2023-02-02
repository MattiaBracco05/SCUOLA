import React, {useRef} from 'react'
import './App.css'

const App = () => {
  const mioDiv = useRef(null)

  //FUNZIONE CLICCAMI (pressione del div)
  const cliccami =(event) => {
    console.log("FUNZIONE CLICCAMI (pressione del div)")

    //alert con il testo del div selezionato
    alert(event.target.textContent)
  }

  //FUNZIONE CLICCAMI 2 (pressione del div)
  const cliccami2 =(event)=>{
    console.log("FUNZIONE CLICCAMI 2 (pressione del div)")

    //alert con il prezzo del prodotto
    alert(event.target.dataset.nome)
  }

  return (
    <>
      {/* Event target */}
      <h1>·Event target (clicca su un div)</h1>
      <div onClick={cliccami}>
        <p>Ciao</p>
        <div>Buona sera</div>
        <p>Buon giorno</p>
      </div>

      {/* Current target */}
      <h1>·Current target (clicca su un immagine)</h1> 
      <div class="pc" onClick={cliccami2} className="card-img">
        {/* alle immagini aggiungo un attributo personalizzato "data-nome" */}
        <img data-nome = "Beta" src="https://storage.edidomus.it/dueruote/nuovo/850/00050791.JPG" width="400vh" alt=""/>
        <img data-nome = "Derbi" src="https://storage.edidomus.it/dueruote/nuovo/850/LAT3899.jpg" width="350vh" alt=""/>
        <img data-nome = "Fantic" src="https://www.dueruote.it/content/dam/dueruote/it/foto/moto-scooter/2019/11/05/fantic-motor-enduro-e-motard-50-e-125/gallery/rbig/50%20M%20bk%20competition.jpg" width="300vh" alt=""/>
      </div>
    </>
  )
}

export default App