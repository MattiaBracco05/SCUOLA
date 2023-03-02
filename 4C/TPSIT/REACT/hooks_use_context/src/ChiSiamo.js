import React, { useContext } from 'react'
import { mioContext } from './App'

const ChiSiamo = () => {
    
    let messaggio = useContext(mioContext)

    //RETURN --> Stampa a video
    return (
        <div>
            <h1>Chi siamo?</h1>
            Variabile globale: {messaggio}
        </div>
    )
}

export default ChiSiamo