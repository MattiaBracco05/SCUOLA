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

            //STAMPO IN CONSOLE IL TITOLO
            console.log(parseXML.querySelector("titolo"))
        })
}