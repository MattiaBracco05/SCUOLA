let temperatureOrdered = []
let humidityOrdered = []

const caricaDati = () => {

    fetch(url)
        .then((dati) => dati.json())
        .then((data) => {

            const dateTable = document.querySelector("table tbody");

            let i = 0;
            let insert = ""
            data.forEach(function({ lora_device_id, data, measured_at }) {

                temperatureOrdered[i] = data.sensor1.lowRes.temperature
                humidityOrdered[i] = data.sensor1.lowRes.humidity

                insert += "<tr class='effect'>";
                insert += `<td>${lora_device_id}</td>`
                insert += `<td class="um">${cleanTimestamp(measured_at)}</td>`
                insert += `<td>${cleanTemperature(temperatureOrdered[i])}°</td>`
                insert += `<td>${humidityOrdered[i]}%</td>`
                insert += "</tr>";

                i++;

            })

            dateTable.innerHTML = insert;

        })
}

//ORDINA PER TEMPERATURA CRESCENTE
const temperatureUp = () => {
    temperatureOrdered.sort()
    fetch(url)
        .then((dati) => dati.json())
        .then((data) => replace(data))
}

//ORDINA PER TEMPERATURA DECRESCENTE
const temperatureDown = () => {
    temperatureOrdered.sort(function(x, y) {
        return y - x;
    });
    fetch(url)
        .then((dati) => dati.json())
        .then((data) => replace(data))
}

//ORDINA PER UMIDITÀ CRESCENTE
const humidityUp = () => {
    humidityOrdered.sort()
    fetch(url)
        .then((dati) => dati.json())
        .then((data) => replace(data))
}

//ORDINA PER UMIDITÀ DECRESCENTE
const humidityDown = () => {
    humidityOrdered.sort(function(x, y) {
        return y - x;
    });
    fetch(url)
        .then((dati) => dati.json())
        .then((data) => replace(data))
}

//FORMATTAZIONE DATA CAMPIONAMENTO
const cleanTimestamp = (timestamp) =>
    timestamp.substring(8, 10) + "/" + timestamp.substring(5, 7) + "/" + timestamp.substring(0, 4) + " - " + timestamp.substring(11, 19)

//FORMATTAZIONE DATA TEMPERATURA
const cleanTemperature = (temperature) =>
    temperature /= 10

//INSERIMENTO DEI DATI NELLA TABELLA
const replace = (data) => {
    const dateTable = document.querySelector("table tbody");

    let i = 0;
    let insert = ""
    data.forEach(function({ lora_device_id, measured_at }) {

        insert += "<tr class='effect'>";
        insert += `<td>${lora_device_id}</td>`
        insert += `<td class="um">${cleanTimestamp(measured_at)}</td>`
        insert += `<td>${cleanTemperature(temperatureOrdered[i])}°</td>`
        insert += `<td>${humidityOrdered[i]}%</td>`
        insert += "</tr>";

        i++;

    })

    dateTable.innerHTML = insert;
}