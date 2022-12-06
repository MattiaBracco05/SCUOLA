//PARSING XML
let URL = "https://raw.githubusercontent.com/icobasco/sample_data_files/master/4C_catalogoFilm.xml"
const carica = () => {
    fetch(URL)
        .then((catalogo) => catalogo.text())
        .then((dati) => {

            //DOM PARSER
            let mioXML = new DOMParser();
            //PARSING DEL TESTO
            let parseXML = mioXML.parseFromString(dati, "text/xml")

            let titoli = parseXML.querySelectorAll("titolo")
            let genere = parseXML.querySelectorAll("generi genere")
            let anno = parseXML.querySelectorAll("anno")
            let insert = ""

            const tabellaDati = document.querySelector("table tbody");

            for (let i = 0; i < titoli.length; i++) {
                insert += "<tr class='effect'>";
                insert += `<td>${titoli[i].innerHTML}</td>`
                insert += `<td>${genere[i].attributes.value.textContent}</td>`
                insert += `<td>${anno[i].attributes.value.textContent}</td>`
                insert += "</tr>";
            }

            tabellaDati.innerHTML = insert;

        })
}