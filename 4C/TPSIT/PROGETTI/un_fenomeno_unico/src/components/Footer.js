/*
COMPONENTE FOOTER
Footer con titolo e 2 link esterni a Instagram e Github
*/
import React from "react";
import {
  Button,
  Container,
  Row,
  Col
} from "reactstrap";

export default function Footer() {
  return (
    <footer className="footer">
      {/* inizio container */}
      <Container>
        {/* inizio riga */}
        <Row>
          {/* TITOLO */}
          <Col md="6">
            <h1 className="title">Un fenomeno unico</h1>
          </Col>
          {/* LOGHI COLLEGAMENTI */}
          <Col md="6">
            <h3 className="title">Follow me</h3>
            <div className="btn-wrapper profile">
              {/* INSTAGRAM */}
              <Button className="btn-icon btn-neutral btn-round btn-simple" color="default" href="https://www.instagram.com/matti_bracco/" id="tooltip230450801" target="_blank">
                <i className="fab fa-instagram" />
              </Button>
              {/* GITHUB */}
              <Button className="btn-icon btn-neutral btn-round btn-simple" color="default" href="https://github.com/MattiaBracco05" id="tooltip622135962" target="_blank">
                <i className="fab fa-github" />
              </Button>
            </div>
          </Col>
        </Row>
        {/* fine riga */}
      </Container>
      {/* fine container */}
    </footer>
  );
}
