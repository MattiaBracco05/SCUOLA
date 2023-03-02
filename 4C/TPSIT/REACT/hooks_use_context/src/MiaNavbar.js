import React from 'react'
import {NavLink, useNavigate} from "react-router-dom"

const MiaNavbar = () => {

    const pippo = useNavigate()

    //FUNZIONE APRI (richiamata alla pressione del button)
    const apri =() => {
        console.log("FUNZIONE APRI (pressione del button)")
        pippo("/ChiSiamo")
    }

    //RETURN --> Stampa a video    
    return (
        <div>
            {/* Navbar */}
            <NavLink to={"/"}>HOME</NavLink><br/>
            <NavLink to={"/ChiSiamo"}>Chi siamo?</NavLink><br/>
            <NavLink to={"/DoveSiamo"}>Dove siamo?</NavLink><br/>

            {/* Equivalente del cliccare la fraccie indietro (<--) del browser, torna al componente aperto precedentemente */}
            <NavLink to={-1}>INDIETRO</NavLink><br/>

            {/* Button */}
            <input type="button" value="API 'CHI SIAMO?'" onClick={apri}/>
        </div>
    )
}

export default MiaNavbar