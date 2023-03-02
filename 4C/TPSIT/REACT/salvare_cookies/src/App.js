import React from 'react'
import {Route, BrowserRouter, Routes} from "react-router-dom"

import Home from "./Home"
import MiaNavbar from "./MiaNavbar"
import ChiSiamo from './ChiSiamo'
import DoveSiamo from './DoveSiamo'

const App = () => {

  //RETURN --> Stampa a video
  return (
    <div>
      <h1>React router dom</h1>

      <BrowserRouter>
            {/* NAVBAR PER LA NAVIGAZIONE (sono obbilgato a inserira dentro a BrowserRouter!)*/}
            <MiaNavbar />
        <Routes>
          {/* Aggiungo una route per ogni componente da inserire */}
          {/* element={}  -->   Elemento da inserire (devo prima importarlo) */}
          {/* path={}     -->   Percorso dell'URL in cui inseriro */}
          {/* es. Home sarà a http://localhost:3000, ChiSiamo si troverà a http://localhost:3000/ChiSiamo */}
          <Route element={<Home />} path={"/"}/>
          <Route element={<ChiSiamo />} path={"/ChiSiamo"}/>
          <Route element={<DoveSiamo />} path={"/DoveSiamo"}/>
        </Routes>
      </BrowserRouter>
      
    </div>
    )
}

export default App