import React, { useState } from 'react'
import "./App.css"

const URL = "https://raw.githubusercontent.com/itisrivoira/obelix/main/lista_citta_fake.json"

const App = () => {  
  const [luoghi, setLuoghi] = useState([])    //secondo elemento è una funzione  

  const Sel=()=>{
    let ID = document.querySelector("#selectCitta")
    let cit = 0
    console.log("Hai scelto l'opzione: " + ID.options.selectedIndex)

	//SELECT - OPZIONE 1 - SALUZZO
    if (ID.options.selectedIndex === 1) {
		
		//parsing del JSON
    	fetch(URL)
    	.then((luoghiText) => luoghiText.json())
    	.then((luoghiJSON) => {
		
			//utilizzo per azzerare ad ogni click del button (in modo da non far ripetere le stesse città più volte)
			setLuoghi([])

			//stampo nome luogo e setemma
			luoghiJSON.map((elemento, indice) => {
				if (elemento.citta == "Saluzzo") {
					cit = setLuoghi((luoghi) => [...luoghi, <div className="container"><div className="citta">{elemento.citta}</div><div className="stemma"><img className="images-stemma" src={elemento.stemma} title={"Stemma " + elemento.citta}></img></div></div>])
				}
			})
      	})
    }

	//SELECT - OPZIONE 2 - VERZUOLO
    if (ID.options.selectedIndex === 2) {
		
		//parsing del JSON
      	fetch(URL)
      	.then((luoghiText) => luoghiText.json())
      	.then((luoghiJSON) => {

			//utilizzo per azzerare ad ogni click del button (in modo da non far ripetere le stesse città più volte)
			setLuoghi([])

			//stampo nome luogo e setemma
			luoghiJSON.map((elemento, indice) => {
				if (elemento.citta == "Verzuolo") {
					cit = setLuoghi((luoghi) => [...luoghi, <div className="container"><div className="citta">{elemento.citta}</div><div className="stemma"><img className="images-stemma" src={elemento.stemma} title={"Stemma " + elemento.citta}></img></div></div>])
				}
			})
      	})
    }

  }
  return (
	//SELECT
    <div class="selectStile">
      <select name="citta" id="selectCitta" onChange={Sel}>
        <option value="" ></option>
        <option value="Saluzzo">Saluzzo</option>
        <option value="Verzuolo">Verzuolo</option>
      </select>
      {luoghi}
    </div>
  )
}

export default App