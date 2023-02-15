import { useState } from "react";
import ReactDOM from "react-dom/client";

function App() {
  const [car, setCar] = useState({
    brand: "Beta",
    model: "RR",
    year: "2019",
    color: "rosso"
  });

  //FUNZIONE CAMBIA COLORE
  const cambiaColore = () => {
    setCar(previousState => {
      return { ...previousState, color: "blu" }
    });
  }

  //RETURN --> Stampa a video
  return (
    <div>
      <h1>Il mio {car.brand}</h1>
      <p>È un {car.model} di colore {car.color} del {car.year}.</p>
      <button type="button" onClick={cambiaColore}>Cambia colore</button>
    </div>
  )
}
export default App