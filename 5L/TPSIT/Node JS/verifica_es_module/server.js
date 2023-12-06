import http from "http"
import url from "url"
import {ottieniData, calcolaTemperaturaMediaLocalita} from "./modulo.js"

/*
Nel file "package.json" alla riga 5 dichiaro come "type" "module"
Questo non deve esseredichiarato nello script! ma prima (per esempio dopo la descrizione (description))
*/

//Creo un array per ogni località dove andro a salvare le misurazioni
var MisurazioniVerzuolo = []
var MisurazioniMilano = []
var MisurazioniTorino = []
var MisurazioniFirenze = []
var MisurazioniBologna = []
var MisurazioniRoma = []
var MisurazioniNapoli = []
var MisurazioniBari = []
var MisurazioniMessina = []


http.createServer((req, res) => {
    //ricavo i parametri
    let parametri = url.parse(req.url, true)
    let temperaturaMinima = parseInt(parametri.query.tempMin)
    let temperaturaMassima = parseInt(parametri.query.tempMax)
    let localita = parametri.query.localitaSelezionata
    
    //console log dei dati inseriti dall'utente
    console.log(temperaturaMinima)
    console.log(temperaturaMassima)
    console.log("Località selezionata: " + parametri.query.localitaSelezionata)

    //ricavo la data con una funzione nel modulo
    let dataMisurazione = ottieniData()
    //creo l'array della mia nuova misurazione appena effettuata
    let nuovaMisurazione = [temperaturaMinima, temperaturaMassima, dataMisurazione]
    
    //switch delle località
    switch(localita) {
        case "verzuolo":
            MisurazioniVerzuolo.push(nuovaMisurazione)
            console.log(MisurazioniVerzuolo)
            break;

        case "milano":
            MisurazioniMilano.push(nuovaMisurazione)
            console.log(MisurazioniMilano)
            break;

        case "torino":
            MisurazioniTorino.push(nuovaMisurazione)
            console.log(MisurazioniTorino)
            break;

        case "firenze":
            MisurazioniFirenze.push(nuovaMisurazione)
            console.log(MisurazioniFirenze)
            break;

        case "bologna":
            MisurazioniBologna.push(nuovaMisurazione)
            console.log(MisurazioniBologna)
            break;

        case "roma":
            MisurazioniRoma.push(nuovaMisurazione)
            console.log(MisurazioniRoma)
            break;

        case "napoli":
            MisurazioniNapoli.push(nuovaMisurazione)
            console.log(MisurazioniNapoli)
            break;

        case "bari":
            MisurazioniBari.push(nuovaMisurazione)
            console.log(MisurazioniBari)
            break;

        case "messina":
            MisurazioniMessina.push(nuovaMisurazione)
            console.log(MisurazioniMessina)
            break;

        default:
            res.write("Errore!\n")
            break;
    }

    //CALCOLO LA MEDIA DELLE LOCALITA'

    res.write("\nMEDIA DELLE TEMPERATURE NELLE SINGOLE LOCALITA'\n\n")


    //ricavo i valori del giorno corrente
    let dataAttuale = ottieniData()
    let totTemp = 0
    let numeroMisurazioni = 0

    //----- VERZUOLO -----
    totTemp = 0
    numeroMisurazioni = 0
    //ciclo per le misurazioni presenti nell'array
    for (let i=0; i < MisurazioniVerzuolo.length; i++) {
        //Controllo se il giorno corrisponde -->
        if (MisurazioniVerzuolo[i][2] = dataAttuale) {
            // console.log("misurazione effettuata oggi")
            totTemp += MisurazioniVerzuolo[i][0]
            console.log("--" + MisurazioniVerzuolo[i][0])
            totTemp += MisurazioniVerzuolo[i][1]
            console.log("--" + MisurazioniVerzuolo[i][1])
            numeroMisurazioni += 2
        }
    }
    let mediaMisurazioniVerzuolo = calcolaTemperaturaMediaLocalita(totTemp, numeroMisurazioni)
    res.write("Media delle misurazioni odierene di oggi a Verzuolo: " + mediaMisurazioniVerzuolo + "\n")

    //----- MILANO -----
    totTemp = 0
    numeroMisurazioni = 0
    //ciclo per le misurazioni presenti nell'array
    for (let i=0; i < MisurazioniMilano.length; i++) {
        //Controllo se il giorno corrisponde -->
        if (MisurazioniMilano[i][2] = dataAttuale) {
            // console.log("misurazione effettuata oggi")
            totTemp += MisurazioniMilano[i][0]
            totTemp += MisurazioniMilano[i][1]
            numeroMisurazioni += 2
        }
    }
    let mediaMisurazioniMilano = calcolaTemperaturaMediaLocalita(totTemp, numeroMisurazioni)
    res.write("Media delle misurazioni odierene di oggi a Milano: " + mediaMisurazioniMilano + "\n")

    //----- TORINO -----
    totTemp = 0
    numeroMisurazioni = 0
    //ciclo per le misurazioni presenti nell'array
    for (let i=0; i < MisurazioniTorino.length; i++) {
        //Controllo se il giorno corrisponde -->
        if (MisurazioniTorino[i][2] = dataAttuale) {
            // console.log("misurazione effettuata oggi")
            totTemp += MisurazioniTorino[i][0]
            totTemp += MisurazioniTorino[i][1]
            numeroMisurazioni += 2
        }
    }
    let mediaMisurazioniTorino = calcolaTemperaturaMediaLocalita(totTemp, numeroMisurazioni)
    res.write("Media delle misurazioni odierene di oggi a Torino: " + mediaMisurazioniTorino + "\n")

    //----- FIRENZE -----
    totTemp = 0
    numeroMisurazioni = 0
    //ciclo per le misurazioni presenti nell'array
    for (let i=0; i < MisurazioniFirenze.length; i++) {
        //Controllo se il giorno corrisponde -->
        if (MisurazioniFirenze[i][2] = dataAttuale) {
            // console.log("misurazione effettuata oggi")
            totTemp += MisurazioniFirenze[i][0]
            totTemp += MisurazioniFirenze[i][1]
            numeroMisurazioni += 2
        }
    }
    let mediaMisurazioniFirenze = calcolaTemperaturaMediaLocalita(totTemp, numeroMisurazioni)
    res.write("Media delle misurazioni odierene di oggi a Firenze: " + mediaMisurazioniFirenze + "\n")

    //----- BOLOGNA -----
    totTemp = 0
    numeroMisurazioni = 0
    //ciclo per le misurazioni presenti nell'array
    for (let i=0; i < MisurazioniBologna.length; i++) {
        //Controllo se il giorno corrisponde -->
        if (MisurazioniBologna[i][2] = dataAttuale) {
            // console.log("misurazione effettuata oggi")
            totTemp += MisurazioniBologna[i][0]
            totTemp += MisurazioniBologna[i][1]
            numeroMisurazioni += 2
        }
    }
    let mediaMisurazioniBologna = calcolaTemperaturaMediaLocalita(totTemp, numeroMisurazioni)
    res.write("Media delle misurazioni odierene di oggi a Bologna: " + mediaMisurazioniBologna + "\n")

    //----- ROMA -----
    totTemp = 0
    numeroMisurazioni = 0
    //ciclo per le misurazioni presenti nell'array
    for (let i=0; i < MisurazioniRoma.length; i++) {
        //Controllo se il giorno corrisponde -->
        if (MisurazioniRoma[i][2] = dataAttuale) {
            // console.log("misurazione effettuata oggi")
            totTemp += MisurazioniRoma[i][0]
            totTemp += MisurazioniRoma[i][1]
            numeroMisurazioni += 2
        }
    }
    let mediaMisurazioniRoma = calcolaTemperaturaMediaLocalita(totTemp, numeroMisurazioni)
    res.write("Media delle misurazioni odierene di oggi a Roma: " + mediaMisurazioniRoma + "\n")

    //----- NAPOLI -----
    totTemp = 0
    numeroMisurazioni = 0
    //ciclo per le misurazioni presenti nell'array
    for (let i=0; i < MisurazioniNapoli.length; i++) {
        //Controllo se il giorno corrisponde -->
        if (MisurazioniNapoli[i][2] = dataAttuale) {
            // console.log("misurazione effettuata oggi")
            totTemp += MisurazioniNapoli[i][0]
            totTemp += MisurazioniNapoli[i][1]
            numeroMisurazioni += 2
        }
    }
    let mediaMisurazioniNapoli = calcolaTemperaturaMediaLocalita(totTemp, numeroMisurazioni)
    res.write("Media delle misurazioni odierene di oggi a Napoli: " + mediaMisurazioniNapoli + "\n")

    //----- BARI -----
    totTemp = 0
    numeroMisurazioni = 0
    //ciclo per le misurazioni presenti nell'array
    for (let i=0; i < MisurazioniBari.length; i++) {
        //Controllo se il giorno corrisponde -->
        if (MisurazioniBari[i][2] = dataAttuale) {
            // console.log("misurazione effettuata oggi")
            totTemp += MisurazioniBari[i][0]
            totTemp += Misurazionibari[i][1]
            numeroMisurazioni += 2
        }
    }
    let mediaMisurazioniBari = calcolaTemperaturaMediaLocalita(totTemp, numeroMisurazioni)
    res.write("Media delle misurazioni odierene di oggi a Firenze: " + mediaMisurazioniBari + "\n")

    //----- MESSINA -----
    totTemp = 0
    numeroMisurazioni = 0
    //ciclo per le misurazioni presenti nell'array
    for (let i=0; i < MisurazioniMessina.length; i++) {
        //Controllo se il giorno corrisponde -->
        if (MisurazioniMessina[i][2] = dataAttuale) {
            // console.log("misurazione effettuata oggi")
            totTemp += MisurazioniMessina[i][0]
            totTemp += MisurazioniMessina[i][1]
            numeroMisurazioni += 2
        }
    }
    let mediaMisurazioniMessina = calcolaTemperaturaMediaLocalita(totTemp, numeroMisurazioni)
    res.write("Media delle misurazioni odierene di oggi a Messina: " + mediaMisurazioniMessina + "\n")


    res.write("\nMEDIA DELLE TEMPERATURE DIVISE PER ZONA\n\n")

    //CALCOLO LA MEDIA DELLE ZONE
    let totaletemperaturaZona = 0

    //Zona NORD (Verzuolo - Milano - Torino)
    //Sommo le medie delle singole città
    totaletemperaturaZona = mediaMisurazioniVerzuolo + mediaMisurazioniMilano + mediaMisurazioniTorino
    //calcolo la media
    let mediaMisurazioni_NORD = calcolaTemperaturaMediaLocalita(totaletemperaturaZona, 3)
    res.write("Media delle misurazioni odierene di oggi al NORD: " + mediaMisurazioni_NORD + "\n")

    //Zona CENTRO (Firenze - Bologna - Roma)
    //Sommo le medie delle singole città
    totaletemperaturaZona = mediaMisurazioniFirenze + mediaMisurazioniBologna + mediaMisurazioniRoma
    //calcolo la media
    let mediaMisurazioni_CENTRO = calcolaTemperaturaMediaLocalita(totaletemperaturaZona, 3)
    res.write("Media delle misurazioni odierene di oggi al CENTRO: " + mediaMisurazioni_CENTRO + "\n")

    //Zona SUD (Napoli - Bari - Messina)
    //Sommo le medie delle singole città
    totaletemperaturaZona = mediaMisurazioniNapoli + mediaMisurazioniBari + mediaMisurazioniMessina
    //calcolo la media
    let mediaMisurazioni_SUD = calcolaTemperaturaMediaLocalita(totaletemperaturaZona, 3)
    res.write("Media delle misurazioni odierene di oggi al SUD: " + mediaMisurazioni_SUD + "\n")


    //Implementare con arrotondamento dei float a 2 cifre decimali
    //La media per zona viene mostratat solamente se ci sono valori registrati per tutte e 3 le città appartenenti a quella zona (da correggere)

    res.end("\nFine del messaggio di risposta del server!")
}).listen(3000)