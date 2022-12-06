import React, { useState, useEffect } from 'react' 

import './App.css'
import Marca from './Marca.js'
import Giacenza from './Giacenza.js'

const App = () => { 
    return (
        <div>
            <Marca />
            <Giacenza />
        </div>
    )
}

export default App