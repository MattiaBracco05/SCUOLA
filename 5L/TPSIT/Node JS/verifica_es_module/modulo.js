//Funzione ottieni data
export const ottieniData=() => {
    //data attuale
    let dataAttuale = new Date()
    
    //ricavo giorno, mese e anno
    let giorno = dataAttuale.getDay()
    let mese = dataAttuale.getMonth()
    let anno = dataAttuale.getFullYear()

    //Costruisco la mia data
    let miaData = giorno + "/" + mese + "/" + anno 
    return (miaData)
}

export const calcolaTemperaturaMediaLocalita=(tot, N) => {
    let media = tot / N
    return (media)
}

/*
Per esportare le mie funzioni inserisco "export" prima di "const" dove dichiaro le funzioni
*/