/*
COMPONENTE TESTO INTRODUZIONE
Testo che introduce il sito
*/
import React from "react";
import { Container, Row, Col } from "reactstrap";

export default function TestoIntroduzione() {
  return (
    <div>
      <Container>
        <h3 className="title">Introduzione</h3>
        <div id="typography">
          <Row>
            <Col md="12">
              <div className="typography-line">
                <blockquote>
                  <p className="blockquote blockquote-info">
                    Giovedì 22 dicembre 2022 ci siamo recati nel centro storico per ammirare un fenomeno unico nel suo genere che si verifica da oltre 500 anni, ma è stato scoperto solamente nel 2016 dal professore Franco Giletta.
                    <br />Si tratta di una precisa sovrapposizione dell'ombra prodotta dalla Torre Civica sul campanile della Chiesa di San Giovanni.
                  </p>
                </blockquote>
              </div>
            </Col>
          </Row>
        </div>
      </Container>
    </div>
  );
}
