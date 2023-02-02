import React, { useState, useEffect } from 'react'
import './App.css'

const URL = "https://raw.githubusercontent.com/itisrivoira/obelix/main/lista_citta_fake.json"

const App = () => {	
	//USESTATE nel quale salvo le città
	const [citta, setCitta] = useState([])

	//FUNZIONE CONNESSIONE
	const connessione =()=>{
		//FETCH
		fetch(URL)
		.then((luoghiText) => luoghiText.json())
		.then((luoghiJSON) => {
			
			//COMANDO MAP
			luoghiJSON.map((element, index) => {
				
				//FUNZIONE FRECCIA CON "...luoghi" per mantenere quelli precedenti ed evitare che stampi solo l'ultimo
				setCitta((citta) => [...citta, <div class="row justify-content-center mt-3"><div class="col-3">{element.citta}</div><div class="col-3"><img src={element.stemma} alt="" width="30%"></img></div></div>])
				return
			})
		})
	}

	//RETURN --> Stampa a video
	return (
		<div>
			<h1>Città e stemma V1</h1>

			{/* BUTTON PER VISUALIZZARE */}
			<div className="carica">
				<input type="button" value="VISUALIZZA CITTÀ" onClick={connessione}/>
			</div>

			{/* CITTÀ DA VISUALIZZARE */}
			{citta}
		</div>
	)
}

export default App


