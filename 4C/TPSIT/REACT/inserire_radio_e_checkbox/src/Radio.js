import React from 'react'

const App = () => {
  //FUNZIONE AGGIORNA (richiamata al cambiamento della selezione dei radio button)
  const aggiorna = (event) => {
    console.log("FUNZIONE AGGIORNA (onChange radio button)")
    console.log("Selezionato: " + event.target.value)
  }

  //RETURN --> Stampa a video
  return (
    <div>
      {/* RADIO BUTTON */}
      <h1>Radio button</h1>
      <input type="radio" name="sesso" value="Maschio" onChange={aggiorna} />Maschio
      <input type="radio" name="sesso" value="Femmina" onChange={aggiorna} />Femmina
    </div>
  )
}

export default App