/*
COMPONENTE TESTO SPIEGAZIONE
Testo che spiega il fenomeno
*/
import React from "react";
import { Container, Row, Col } from "reactstrap";

export default function TestoProgettazione() {
  return (
    <div>
      <Container>
        <h3 className="title">Effetto puramente casuale o voluto?</h3>
        <div id="typography">
          <Row>
            <Col md="12">
              <div className="typography-line">
                <blockquote>
                  <p className="blockquote blockquote-info">
                    La vera domanda che ognuno di noi si può porre è chiedersi se questo fenomeno sia stato voluto o sia solo un "caso fortunatissimo".
                    <br />Dopo una lunga osservazione e un lungo studio di questo fenomeno il professore Franco Giletta ha potuto individuare diversi elementi di suggestione che fanno pensare ad un effetto voluto, tra questi il periodo dell'anno in cui si verifica questo gioco di luci, ovvero quello che precede il Sol Invictus pagano e il Natale cristiano.
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
