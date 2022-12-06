const visualizza =()=> {
	/*
	La funzione "fetch()":
		-permette di scaricare i contenuti di un file dal web.
		-ha bisongo di 2 parametri:
			-URL
			-literal eobject (simile agli oggetti json, non è obbligatorio, viene usato per inviare informazioni al server)
		-è una funzione ASINCRONA (scarico i file, quando ho finito prendo le informazioni e le visualizzo nella apgina HTML, tutto il codice che c'è sotto viene eseguito in parallelo)
		-in caso di errore "Cross-Origin Request Blocked" non si hanno i permessi per scaricare i file
	*/
	url = "https://raw.githubusercontent.com/icobasco/sample_data_files/master/pera_misure_sample.json"
	fetch(url)
	//trasformo il contenuto scaricato (testo) in un file .json
	.then((dati) => dati.json())
	//visualizzo il contenuto del file .json in una pagina web
	.then((datiJSON)=>{
		let nuovoElemento = document.createElement("div")
		nuovoElemento.innerHTML = datiJSON[0].id
		document.querySelector("body").appendChild(nuovoElemento)
	})
}