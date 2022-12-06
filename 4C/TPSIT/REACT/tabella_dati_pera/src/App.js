import React, { useEffect, useState } from 'react'
import "./App.css"
const App = () => {

	const [arrayPera, setarrayPera] = useState([]);
	
	//USE EFFECT
	useEffect(() => {
		download()
	}, [])
	
	const URL = "https://raw.githubusercontent.com/icobasco/sample_data_files/master/pera_misure_sample.json"

	//FUNZIONE DOWNLOAD (per il parser dei dati JSON)
	const download =()=> {
		fetch(URL)
		.then((testo) => testo.json())
		.then((pera) => {
			pera.map((elemento, indice) => {
				setarrayPera((arrayPera) => [...arrayPera, <div className='bordi'>UMIDITÀ: {elemento.data.sensor1.lowRes.humidity}% TEMPERATURA (*10): {elemento.data.sensor1.lowRes.temperature}°C</div>])
			})
		})
	}

	return (
		<div>{arrayPera}</div>
	)
}

export default App