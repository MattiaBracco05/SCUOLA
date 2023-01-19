/*
COMPONENTE FOTO GALLERY 2
2° Foto gallery presente nel sito, riporta 8 immagini con lo spostamento dell'ombra sul campanile
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
    src: require("assets/img/f1.jpg"),
    altText: "Slide 1",
    caption: "22/12/2022 · 10:55"
  },
  {
    src: require("assets/img/f2.jpg"),
    altText: "Slide 2",
    caption: "22/12/2022 · 10:56"
  },
  {
    src: require("assets/img/f3.jpg"),
    altText: "Slide 3",
    caption: "22/12/2022 · 10:57"
  },
  {
    src: require("assets/img/f4.jpg"),
    altText: "Slide 4",
    caption: "22/12/2022 · 10:58"
  },
  {
    src: require("assets/img/f5.jpg"),
    altText: "Slide 5",
    caption: "22/12/2022 · 10:59"
  },
  {
    src: require("assets/img/f6.jpg"),
    altText: "Slide 6",
    caption: "22/12/2022 · 10:59"
  },
  {
    src: require("assets/img/f7.jpg"),
    altText: "Slide 7",
    caption: "22/12/2022 · 11:00"
  },
  {
    src: require("assets/img/f8.jpg"),
    altText: "Slide 8",
    caption: "22/12/2022 · 11:00"
  }
];

export default function FotoGallery2() {
  return (
    <div className="section section-javascript" id="javascriptComponents">
      <div className="section">
        <Container>
          <Row className="justify-content-between align-items-center">
            <Col className="mb-5 mb-lg-0" lg="6">
              <p className="text-white mt-4">
                Questa fotogallery riporta 8 fotografie scattate da me e immortalano l'ombra sul campanile dai minuti precedenti al fenomeno fino al perfetto allineamento verificatosi alle ore 11:00.
                <br />Purtroppo causa presenza di nuvole l'ombra negli scatti al momento del perfetto allineamento è meno definita rispetto ai minuti precedenti, ma pur sempre visibile.
              </p>
            </Col>
            <Col lg="6">
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
