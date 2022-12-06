/*
OBELIX - BUTTON PER STAMPARE I LOCALI
Lo scopo di questo esercizio è inserire un button nella pagina web
Alla pressione (onClick) vengono mostrati i locali
*/

import React, { useState } from 'react'
import "./App.css"

//Costante con l'URL del file JSON dei locali
const URL = "https://raw.githubusercontent.com/itisrivoira/obelix/main/lista_locali.json"

const App = () => {

	/*
	Il primo elemento (locali) è il nome dello stato
	Il secondo elemento (setLocali) è la funzione
	per modificare (es. aggiungere un elemento nell'array) devo usare la funzione!
	lo stato può essere inizializzato al posti di "second" con: ·stringa vuota, ·array vuoto, ·0, ...
	*/
	const [locali, setLocali] = useState([])

	//Funzione connessione() che viene richiamata quando si verifica un click sul button
	const connessione = ()=> {
		console.log("Sono dentro la funzione!")

		
		//Funzione fetch per scaricare il contenuto dell'URL e parsarlo
		fetch(URL)
			.then((localitext) => localitext.json())
			.then((localiJSON) => {
				console.log("LOCALI NELL'ARRAY:")
				console.log(localiJSON)

				/*
				Utilizzo il comando map per stampare i nomi dei locali
				Questa funzione mi richiede 2 parametri che per comodità chiamo "element" e "index"
				*/
				localiJSON.map((element, index) => {
					setLocali((locali) => [...locali, "Nome locale: " + element.nome + " Città: " + element.citta + " "])
					return
				})

			})
		}

  return (
	//All'interno del retur, nel <div> inserisco un input button
    <div>
		{/* per chiudere devo SEMPRE utilizzare "/>" ! */}
		{/* quando richiamo la funzione NON devo mettere le parentesi () altrimenti viene richiamata in automtico senza il click */}
		<input type="button" value={"CONNETTI OBELIX"} onClick={connessione}/>
		{locali}
	</div>
  )
}

export default App