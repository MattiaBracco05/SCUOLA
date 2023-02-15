import React, { useState } from 'react'
import ReactDOM from 'react-dom/client';

const App = () => {

  //DICHIARO LO useState NEL QUALE SALVO IL NOME
  const [nome, setNome] = useState("");

  //FUNZIONE alertNome (RICHIAMATA ALLA PRESSIONE DEL BUTTON CONFERMA)
  const alertNome = (event) => {
    event.preventDefault();
    alert(`Il tuo nome è: ${nome}`);
  }

  //RETURN --> Stampa a video
  return (
    <div>
      {/* FORM */}
      <form onSubmit={alertNome}>
        
        {/* INPUT TEXT */}
        <label>Inserisci il tuo nome:
          <input type="text" value={nome} onChange={(e) => setNome(e.target.value)} />
        </label>
        
        {/* BUTTON PER CONFERMARE */}
        <input type="submit" value={"CONFERMA"} />

      </form>
    </div>
  )
}

export default App