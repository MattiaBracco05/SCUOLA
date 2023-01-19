import React from "react";

//IMPORTO I VARI COMPONENTI
import Navbar from "./Navbar.js";
import Header from "./Header.js";
import Footer from "./Footer.js";
import TestoIntroduzione from "./TestoIntroduzione.js";
import ButtonMaps from "./ButtonMaps.js";
import FotoGallery1 from "./FotoGallery1";
import TestoTorri from "./TestoTorri.js";
import TestoSpiegazione from "./TestoSpiegazione.js";
import FotoGallery2 from "./FotoGallery2.js";
import VideoPlayer from "./VideoPlayer";
import TestoProgettazione from "./TestoProgettazione.js";
import Riepilogo from "./Riepilogo.js";

export default function Index() {
  React.useEffect(() => {
    document.body.classList.toggle("index-page");

    return function cleanup() {
      document.body.classList.toggle("index-page");
    };
  }, []);
  return (
    <>
      {/* NAVBAR (fissa) */}
      <Navbar />
      {/* inizio pagina scorrevole */}
      <div className="wrapper">
        {/* INTESTAZIONE */}
        <Header />
        {/* TESTO INTRODUZIONE */}
        <TestoIntroduzione />
        {/* BUTTON MAPS */}
        <ButtonMaps />
        {/* FOTO GALLERY 1 */}
        <FotoGallery1 />
        {/* TESTO TORRI */}
        <TestoTorri />
        {/* TESTO SPIEGAZIONE */}
        <TestoSpiegazione />
        {/* FOTO GALLERY 2 */}
        <FotoGallery2 />
        {/* VIDEO PLAYER */}
        <VideoPlayer />
        {/* TESTO PROGETTAZIONE */}
        <TestoProgettazione />
        {/* RIEPILOGO */}
        <Riepilogo />                
        {/* FOOTER */}
        <Footer />
      </div>
      {/* fine pagina scorrevole */}
    </>
  );
}
