import React, { useState } from 'react'

const App = () => {

  //useState per memorizzare gli sport selezionati dalle chechbox
  const [sport, setSport] = useState([])

  //FUNZIONE AGGIORNA (richiamata al cambiamento della selezione delle chechbox)
  const aggiorna = (event) => {
    console.log("FUNZIONE AGGIORNA (onChange checkbox)")
    console.log("Selezionato: " + event.target.value)
    /*
    ***** SPORT INCLUDES *****
    Controllo che lo sport selezionato non sia già presente all'interno dell'array
    "!" serve a negare la condizione (sport.includes(event.target.value) controlla se è presente la condzione
    Con "!" l'if verifica che non sia presente (NOT) --> se è così --> aggiunge lo sport all'array

    ***** FILTER *****
    È una funzione che può essere usata solo con gli array
    Ho creato una funzione anonima (si chiama così perchè non ha un nome), questa funzione deve SEMPRE avere un return di tipo boolean True / False
    Questa funzione ritorna un'array (salvato nello useState sport tramite setSport)
    */
    if (!sport.includes(event.target.value)) {
      setSport([...sport, event.target.value])
    } else {
      setSport(sport.filter((element) => element != event.target.value))
    }
  }

  //RETURN --> Stampa a video
  return (
    <div>
      {/* CHECKBOX */}
      <h1>Checkbox</h1>
      <input type="checkbox" name="sport" value="Calcio" onChange={aggiorna} />Calcio
      <input type="checkbox" name="sport" value="Basket" onChange={aggiorna} />Basket
      <input type="checkbox" name="sport" value="Tennis" onChange={aggiorna} />Tennis
      <br/>

      {/* Stampo gli sport selezionati (salvati nello useState) */}
      {sport}
    </div>
  )
}

export default App