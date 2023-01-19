import React from "react";
import {
  Card,
  CardBody,
  CardTitle,
  Container,
  Row,
  Col
} from "reactstrap";

export default function Riepilogo() {
  return (
    <>
      <section className="section">
        <Container>
          <Row className="row-grid justify-content-between">

            {/* inzio descrizione */}
            <Col md="6">
              <div className="pl-md-5">
                <h1>Riepilogo:</h1>
              </div>
            </Col>
            {/* fine descrizione */}

            {/* inizio card */}
            <Col className="mt-lg-0" md="5">
              
              {/* inizio prima riga di card */}
              <Row>
                <Col className="px-2 py-2" lg="6" sm="12">
                  {/* inizio card data inizio */}
                  <Card className="card-stats">
                    <CardBody>
                      <Row>
                        {/* LOGO */}
                        <Col md="4" xs="5">
                          <div className="icon-big text-center icon-warning">
                            <i className="far fa-calendar-check" />
                          </div>
                        </Col>
                        {/* TESTO */}
                        <Col md="8" xs="7">
                          <div className="numbers">
                            <CardTitle tag="p">20 / 12</CardTitle>
                            <p className="card-category">Inizio</p>
                          </div>
                        </Col>
                      </Row>
                    </CardBody>
                  </Card>
                  {/* fine card data inizio */}
                </Col>
                <Col className="px-2 py-2" lg="6" sm="12">
                  {/* inizo card data fine */}
                  <Card className="card-stats">
                    <CardBody>
                      <Row>
                        <Col md="4" xs="5">
                          <div className="icon-big text-center icon-warning">
                            <i className="far fa-calendar-times" />
                          </div>
                        </Col>
                        <Col md="8" xs="7">
                          <div className="numbers">
                            <CardTitle tag="p">07 / 01</CardTitle>
                            <p className="card-category">Fine</p>
                          </div>
                        </Col>
                      </Row>
                    </CardBody>
                  </Card>
                  {/* fine card data fine */}
                </Col>
              </Row>
              {/* fine prima riga di card */}

              {/* inizio seconda riga di card */}
              <Row>
                <Col className="px-2 py-2" lg="6" sm="12">
                  {/* inizio card luogo */}
                  <Card className="card-stats">
                    <CardBody>
                      <Row>
                        <Col md="4" xs="5">
                          <div className="icon-big text-center icon-warning">
                            <i className="far fa-map" />
                          </div>
                        </Col>
                        <Col md="8" xs="7">
                          <div className="numbers">
                            <CardTitle tag="p">Saluzzo</CardTitle>
                            <p className="card-category">Luogo</p>
                          </div>
                        </Col>
                      </Row>
                    </CardBody>
                  </Card>
                  {/* fine card luogo */}
                </Col>
                <Col className="px-2 py-2" lg="6" sm="12">
                  {/* inizio card durata */}
                  <Card className="card-stats">
                    <CardBody>
                      <Row>
                        <Col md="4" xs="5">
                          <div className="icon-big text-center icon-warning">
                            <i className="far fa-hourglass" />
                          </div>
                        </Col>
                        <Col md="8" xs="7">
                          <div className="numbers">
                            <CardTitle tag="p">1 minuto</CardTitle>
                            <p className="card-category">Durata</p>
                          </div>
                        </Col>
                      </Row>
                    </CardBody>
                  </Card>
                  {/* fine card durata*/}
                </Col>
              </Row>
              {/* fine seconda riga di card */}

              {/* inizio terza riga di card */}
              <Row>
                <Col className="px-2 py-2" lg="6" sm="12">
                  {/* inizio card scoperto nel */}
                  <Card className="card-stats">
                    <CardBody>
                      <Row>
                        <Col md="4" xs="5">
                          <div className="icon-big text-center icon-warning">
                            <i className="far fa-clock" />
                          </div>
                        </Col>
                        <Col md="8" xs="7">
                          <div className="numbers">
                            <CardTitle tag="p">2016</CardTitle>
                            <p className="card-category">Scoperto nel</p>
                          </div>
                        </Col>
                      </Row>
                    </CardBody>
                  </Card>
                  {/* fine card scoperto nel */}
                </Col>
                <Col className="px-2 py-2" lg="6" sm="12">
                  {/* inizio card scoperto da */}
                  <Card className="card-stats">
                    <CardBody>
                      <Row>
                        <Col md="4" xs="5">
                          <div className="icon-big text-center icon-warning">
                            <i className="far fa-user" />
                          </div>
                        </Col>
                        <Col md="8" xs="7">
                          <div className="numbers">
                            <CardTitle tag="p">F. Giletta</CardTitle>
                            <p className="card-category">Scoperto da</p>
                          </div>
                        </Col>
                      </Row>
                    </CardBody>
                  </Card>
                  {/* fine card scoperto da*/}
                </Col>
              </Row>
              {/* fine terza riga di card */}

            </Col>
            {/* fine card */}

          </Row>
        </Container>
      </section>
    </>
  );
}
