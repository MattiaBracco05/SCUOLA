/*
COMPONENTE HEADER
Contiene il titolo e la descrizione del sito, inoltre inserisce 7 quadrat decorativi (quelli che si spostano)
*/
import React from "react";
import { Container } from "reactstrap";

export default function Header() {
  return (
    <div className="page-header header-filter">
      <div className="squares square1" />
      <div className="squares square2" />
      <div className="squares square3" />
      <div className="squares square4" />
      <div className="squares square5" />
      <div className="squares square6" />
      <div className="squares square7" />
      <Container>
        <div className="content-center">
          <h1 className="h1-seo">Un Fenomeno Unico</h1>
          <h3 className="d-sm-block">
            L’ombra della Torre Civica si proietta sul campanile di San Giovanni
          </h3>
        </div>
      </Container>
    </div>
  );
}
