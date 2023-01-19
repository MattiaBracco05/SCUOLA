/*
COMPONENTE VIDEO PLAYER
Mini Player MP4 utilizzato per la riproduzione del video time-lapse
*/
import React from "react";
import {DefaultPlayer as Video} from 'react-html5video';
import 'react-html5video/dist/styles.css'
import MioVideo from '../assets/video/time_lapse.mp4';
import Copertina from '../assets/img/copertina_time_lapse.jpg';

import {
    Container,
    Row,
    Col,
} from "reactstrap";

const ReactVideoPlayer = () => {
    return (
        <Container>
            <Row className="justify-content-between align-items-center">
                <Col lg="6">
                    <Video autoPlay loop poster={Copertina}>
                        <source src={MioVideo} type="video/mp4" />
                    </Video>
                </Col>
                <Col className="mb-5 mb-lg-0" lg="6">
                    <p className="text-white mt-4">
                        Grazie anche al video time-lapse è possibile vedere in pochi secondi lo spostamento compiuto dall'ombra in circa 5 minuti, la quale scorre a destra fino a combaciare con i lati della torre del camapnile mentre l'ombra della cupola si allinea a sua volta con la cuspide del campanile.
                        <br />Nella parte finale del video è possibile vedere l'ombra che inizia lo spostamento a destra e non risulta più allineata al campanile
                    </p>
                </Col>
            </Row>
        </Container>
    );
};

export default ReactVideoPlayer;