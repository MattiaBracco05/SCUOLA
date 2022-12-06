import React from 'react'

const App = () => {

	//variabile globale per il componente (tutte le funzioni possono accedere)
	const URL = "https://raw.githubusercontent.com/icobasco/sample_data_files/master/pera_misure_sample.json"
	//creo una sottofunzione (funzione nella funzione) per il parser dei dati JSON
	const download =()=> {
		fetch(URL)
		.then((testo) => testo.json())
		.then((pera) => {
			let miaVar = pera[0].data.sensor1.lowRes.humidity + " " + pera[0].data.sensor1.lowRes.temperature     
			console.log(miaVar)
		})
	}

	return (
		<div>Mattia{download()}</div>
	)
}

export default App