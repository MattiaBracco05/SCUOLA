import React, { useState, useEffect } from 'react' 

import './App.css'
import Prefisso from './Prefisso'
import Telefono from './Telefono'

const App = () => { 
    return (
        <div>
            <Telefono />
            <Prefisso />
        </div>
    )
}

export default App