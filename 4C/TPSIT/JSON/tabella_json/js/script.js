const visualizza = ()=> {

    fetch(json_measures_url)
    .then((dati)=>dati.json())
    .then((misure)=> {
        // Ho i dati e li carico nella pagina html

        let div_header = document.createElement("div");
        let div_misure = document.getElementById("misure");
        div_misure.className = "col-sm-12";
        console.log("Trovate " + misure.length + " misure");

        console.log("Prova: 241 is " + cleanTemperature("241"));

        div_header.innerHTML = "<div class=\"row\">" + 
            // "<div class=\"col-sm-3\">ID</div>" + 
            "<div class=\"col-sm-3 bg-info border d-flex justify-content-center\">DEVICE</div>" +
            "<div class=\"col-sm-3 bg-info border d-flex justify-content-center\">TIMESTAMP</div>" +
            "<div class=\"col-sm-3 bg-secondary border d-flex justify-content-center\">TEMPERATURA<br />[°Cx10]</div>" +
            "<div class=\"col-sm-3 bg-info border d-flex justify-content-center\">UMIDITA'<br />[%RH]</div>" +
            "</div>";
        div_misure.appendChild(div_header);

        // TODO: array non è ordinato per timestap!
        
        for (var misura of misure)  {
            let div_row = document.createElement("div");
            div_row.innerHTML = "<div class=\"row\">" + 
                // "<div class=\"col-sm-3\">" + misura.id + "</div>" + 
                "<div class=\"col-sm-3 bg-info border d-flex justify-content-center\">" + misura.lora_device_id + "</div>" +
                "<div class=\"col-sm-3 bg-info border d-flex justify-content-center\">" + cleanTimestamp(misura.measured_at) + "</div>" +
                "<div class=\"col-sm-3 bg-secondary border d-flex justify-content-center\">" + cleanTemperature(misura.data.sensor1.lowRes.temperature) + "</div>" +
                "<div class=\"col-sm-3 bg-info border d-flex justify-content-center\">" + misura.data.sensor1.lowRes.humidity + "</div>" +
                "</div>";
            div_misure.appendChild(div_row);
        }

    })
}

// NB: trattato come string
const cleanTimestamp = (timestamp)=> 
    timestamp.substring(8, 10) + "/" + timestamp.substring(5, 7) + "/" + timestamp.substring(0, 4) + 
    " @ " + timestamp.substring(11, 19)
    ;

// NB: trattato come numeric
const cleanTemperature = (temperature)=>
    temperature /= 10
;


