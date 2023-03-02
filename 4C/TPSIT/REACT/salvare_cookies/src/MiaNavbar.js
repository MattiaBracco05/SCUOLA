import React from 'react'
import {NavLink, useNavigate} from "react-router-dom"

const MiaNavbar = () => {

    const pippo = useNavigate()

    //FUNZIONE APRI (richiamata alla pressione del button)
    const apri =() => {
        console.log("FUNZIONE APRI (pressione del button)")
        pippo("/ChiSiamo")
        sessionStorage.setItem("variabileSessionStorage", "Mattia")
        localStorage.setItem("variabileLocalStorage", "Mattia")

        //Per vedere queste variabili: tasto DX --> ispeziona --> archiviazione --> archiviazione locale / archiviazione sessioni

        let miaVariabile = sessionStorage.getItem("nomeVariabile")
        console.log(miaVariabile)

    }

    //RETURN --> Stampa a video    
    return (
        <div>
            {/* Navbar */}
            <NavLink to={"/"}>HOME</NavLink><br/>
            <NavLink to={"/ChiSiamo"}>Chi siamo ?</NavLink><br/>
            <NavLink to={"/DoveSiamo"}>Dove siamo ?</NavLink><br/>

            {/* Equivalente del cliccare la fraccie indietro (<--) del browser, torna al componente aperto precedentemente */}
            <NavLink to={-1}>INDIETRO</NavLink><br/>

            {/* Button */}
            <input type="button" value="API" onClick={apri}/>
        </div>
    )
}

export default MiaNavbar