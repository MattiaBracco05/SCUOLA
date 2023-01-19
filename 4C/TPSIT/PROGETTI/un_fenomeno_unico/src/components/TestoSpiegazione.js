/*
COMPONENTE TESTO SPIEGAZIONE
Testo che spiega il fenomeno
*/
import React from "react";
import { Container, Row, Col } from "reactstrap";

export default function TestoSpiegazione() {
  return (
    <div>
      <Container>
        <h3 className="title">Quando si verifica questo fenomeno?</h3>
        <div id="typography">
          <Row>
            <Col md="12">
              <div className="typography-line">
                <blockquote>
                  <p className="blockquote blockquote-info">
                    Questo particolare fenomeno, dovuto anche al sole più basso all'orizzonte, si verifica soltanto in un determinato periodo che va dai giorni precedenti al solstizio d'inverno fino all'epifania e dura all'incirca 1 minuto intorno allo scoccare delle ore 11:00, dopo il quale l'ombra sarà spostata a destra rispetto all'edificio.
                    <br />L’ombra della Torre nel periodo di novembre inizia a salire lungo il campanile fino a raggiungere la perfetta sovrapposizione per poi lentamente ridiscendere. Il 22 dicembre, giorno corrispondente al solstizio d'inverno alle ore 11:00 sembra essere l'istante in cui questo allineamento risulta perfetto.
                    <br />L'unico luogo dal quale si può assistere a questa sovrapposizione è la piazza antistante la Chiesa di San Giovanni.
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
