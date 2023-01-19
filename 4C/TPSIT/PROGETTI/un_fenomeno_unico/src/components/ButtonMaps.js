/*
COMPONENTE BUTTON MAPS
Button utilizzato per inserire un collegamento a Google Maps (apre la posizione della torre civica sulla mappa)
*/
import React from "react";

import {
  Button,
  Container,
  Row,
  Col
} from "reactstrap";

export default function ButtonMaps() {
  return (
    <div>
      <Container>
        <Row>
          <Col md="5 offset-4">
            <Button className="btn-round" color="success" href="https://www.google.it/maps/place/Torre+Civica/@44.6434943,7.4881974,19z/data=!4m5!3m4!1s0x12cd4904ece1bbe3:0x35d18889b7f634a9!8m2!3d44.6433696!4d7.4882368" type="button" size="lg" target="new">
              Visualizza posizione su Google Maps
            </Button>
          </Col>
        </Row>
      </Container>
    </div>
  );
}
