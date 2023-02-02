import React from 'react'
import './App.css'

const URL = "https://37.60.34.42:8080/getProdotti"

const App = () => {
  let data = { citta: "001", idLocali: "P001"}

  fetch(URL, {
    method: "POST",
    headers:{
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
  .then((pippo) => pippo.json)
  .then(mioJSON => {

  })

  return (
    <div>
      Costruisco il componente
    </div>
  )
}

export default App