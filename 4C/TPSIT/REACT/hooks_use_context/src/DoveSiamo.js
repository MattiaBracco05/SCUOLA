import React, { useContext } from 'react'
import { mioContext } from './App'

const DoveSiamo = () => {
    
    let messaggio = useContext(mioContext)

    //RETURN --> Stampa a video
    return (
        <div>
            <h1>Dove siamo?</h1>
            Variabile globale: {messaggio}
        </div>
    )
}

export default DoveSiamo