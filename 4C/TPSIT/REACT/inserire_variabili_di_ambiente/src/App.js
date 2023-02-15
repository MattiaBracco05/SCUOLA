import React from 'react'

const App = () => {

  //RETURN --> Stampa a video
  return (
    <div>
      <h1>Variabili d'ambiente</h1>
      Variabile d'ambiente nascosta: {process.env.REACT_APP_KEY}
    </div>
    )
}

export default App