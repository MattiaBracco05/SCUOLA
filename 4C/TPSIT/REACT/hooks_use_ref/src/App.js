import React, { useRef } from 'react'

const App = () => {
  const mioDiv = useRef(null)
  
  //FUNZIONE CAMBIA COLORE (richiamata alla pressione del button)
  const cambiaColore =()=> {
    console.log("FUNZIONE CAMBIA COLORE (pressione button)")

    //devo sempre utilizzare .current! (non posso mai mettere direttamente mioDiv.style.color...)
    console.log(mioDiv.current)

    //N.B. alcune proprietà hanno il "-" (ad esempio background-color) --> le devo utilizzare senza (backgroundColor)

    //cambio lo stile del <div>
    mioDiv.current.style.color = "darkblue"
    mioDiv.current.style.backgroundColor = "lightblue"
    mioDiv.current.style.fontSize = "10vh"
    mioDiv.current.style.fontFamily = "Monospace"

    //cambio il contenuto del <div>
    mioDiv.current.textContent = "ciao"
  }

  //RETURN (stampa a video)
  return (
    <div>
      {/* DIV */}
      <div ref={mioDiv}>{"BENVENUTO"}</div>
      {/* BUTTON */}
      <input type="button" value="CLICCA QUI" onClick={() => cambiaColore("Mattia")}/>
    </div>
  )
}

export default App