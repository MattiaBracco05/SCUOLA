import React, { useContext } from 'react'
import { mioContext } from './App'

const Home = () => {

    let messaggio = useContext(mioContext)

    //RETURN --> Stampa a video
    return (
        <div>
            <h1>Home</h1>
            Variabile globale: {messaggio}
        </div>
    )
}

export default Home