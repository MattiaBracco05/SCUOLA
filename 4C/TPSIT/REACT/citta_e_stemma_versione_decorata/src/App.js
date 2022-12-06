import React, { useState, useEffect } from 'react'
import './App.css'

const URL = "https://raw.githubusercontent.com/itisrivoira/obelix/main/lista_citta_fake.json"


const App = () => {	
	//USESTATE
	const [luoghi, setluoghi] = useState([])

	//FUNZIONE CONNESSIONE
	const connessione =()=>{
		//FETCH
		fetch(URL)
		.then((luoghiText) => luoghiText.json())
		.then((luoghiJSON) => {
			
			//utilizzo per azzerare ad ogni click del button (in modo da non far ripetere le stesse città più volte)
			setluoghi([])

			//COMANDO MAP
			luoghiJSON.map((element, index) => {
				
				//FUNZIONE FRECCIA CON "...luoghi" per mantenere quelli precedenti ed evitare che stampi solo l'ultimo
				setluoghi((luoghi) => [...luoghi, <div class="row justify-content-center mt-3"><div class="col-3 citta">{element.citta}</div><div class="col-3 stemma"><img src={element.stemma} alt="" width="15%"></img></div></div>])
			})
		})
	}

	return (
	<div>
		{/* BUTTON PER VISUALIZZARE */}
		<div className="carica">
			<input type="button" className='buttonCarica' value="VISUALIZZA CITTÀ" onClick={connessione}/>
		</div>
		{luoghi}
	</div>
	)
}

export default App


