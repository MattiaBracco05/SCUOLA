import React, { useState, useEffect } from 'react'
import './App.css'
import Header from "./Header.js"

const URL = "https://raw.githubusercontent.com/itisrivoira/obelix/main/lista_citta_fake.json"


const App = () => {
	
	let mieiParametri = {
		pathlogo: "data:image/png;base64,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",
		link1: {
			url: "https://www.google.it",
			anchor: "GOOGLE"
		},
		link2: {
			url: "https://www.denina.it",
			anchor: "DENINA"
		},
		link3: {
			url: "https://comune.saluzzo.cn.it/",
			anchor: "SALUZZO"
		},
		link4: {
			url: "https://www.comune.verzuolo.cn.it/",
			anchor: "VERZUOLO"
		}
	}
	
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
		{/* HEADER */}
		<Header valori={mieiParametri}/>

		{/* BUTTON PER VISUALIZZARE */}
		<div className="carica">
			<input type="button" className='buttonCarica' value="VISUALIZZA CITTÀ" onClick={connessione}/>
		</div>

		{/* CITTÀ E STEMMI */}
		{luoghi}
	</div>
	)
}

export default App


