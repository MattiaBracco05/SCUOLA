import React from 'react'
import {Route, BrowserRouter, Routes} from "react-router-dom"
import { createContext } from 'react'

//IMPORTO LE MIE "PAGINE"
import Home from "./Home"
import MiaNavbar from "./MiaNavbar"
import ChiSiamo from './ChiSiamo'
import DoveSiamo from './DoveSiamo'

//ESPORTO LA VARIABILE "mioContext"
export let mioContext = createContext()

const App = () => {
  let miaVariabileGlobale = "PROVA-123"

  //RETURN --> Stampa a video
  return (
    <div>
      <h1>React router dom</h1>

      <BrowserRouter>
          {/* Navbar per la navigazione */}
          <MiaNavbar />

          {/* Context provider */}
          <mioContext.Provider value={miaVariabileGlobale}>
            <Routes>
              <Route element={<Home />} path={"/"}/>
              <Route element={<ChiSiamo />} path={"/ChiSiamo"}/>
              <Route element={<DoveSiamo />} path={"/DoveSiamo"}/>
            </Routes>
          </mioContext.Provider>
          
      </BrowserRouter>
      
    </div>
    )
}

export default App