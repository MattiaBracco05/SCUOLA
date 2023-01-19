/*
COMPONENTE FOTO GALLERY 1
1° Foto gallery presente nel sito, riporta 3 foto con la torre civica, il campanile e la chiesa di San Giovanni
*/
import React from "react";

import {
  Container,
  Row,
  Col,
  UncontrolledCarousel
} from "reactstrap";

const carouselItems = [
  {
    src: require("assets/img/torre_civica.jpg"),
    altText: "Slide 1",
    caption: "Torre Civica"
  },
  {
    src: require("assets/img/campanile.jpg"),
    altText: "Slide 2",
    caption: "Campanile della Chiesa di San Giovanni"
  },
  {
    src: require("assets/img/chiesa.jpg"),
    altText: "Slide 3",
    caption: "Chiesa di San Giovanni"
  }
];

export default function FotoGallery1() {
  return (
    <div className="section section-javascript" id="javascriptComponents">
      <div className="section">
        <Container>
          <Row className="justify-content-between align-items-center">
            <Col lg="6 offset-lg-3">
              <UncontrolledCarousel
                items={carouselItems}
                indicators={true}
                autoPlay={false}
              />
            </Col>
          </Row>
        </Container>
      </div>
    </div>
  );
}
