/*
COMPONENTE TESTO TORRI
Card contenente una breve descrizione della torre civica e del campanile della Chiesa di San Giovanni
*/
import React from "react";
import classnames from "classnames";

import {
  TabContent,
  TabPane,
  Container,
  Row,
  Col,
  Card,
  CardHeader,
  CardBody,
  Nav,
  NavItem,
  NavLink
} from "reactstrap";

export default function TestoTorri() {
  const [iconTabs, setIconsTabs] = React.useState(1);
  return (
    <div className="section section-tabs">
      <Container>
        <Row>
          <Col className="ml-auto mr-auto" md="10" xl="12">
			{/* inizio card */}
            <Card>
                {/* inizio header */}
                <CardHeader>
					<Nav className="nav-tabs-info" role="tablist" tabs>
						{/* HEADER - TORRE CIVICA */}
						<NavItem>
                    		<NavLink className={classnames({active: iconTabs === 1})} onClick={(e) => setIconsTabs(1)} href="#">
							<i className="fas fa-building" />
							Torre Civica
                    		</NavLink>
                  		</NavItem>
						{/* HEADER - CAMPANILE */}
                  		<NavItem>
							<NavLink className={classnames({active: iconTabs === 2})} onClick={(e) => setIconsTabs(2)} href="#">
							<i className="fas fa-church"></i>
							Campanile Chiesa di S. Giovanni
							</NavLink>
                  		</NavItem>
                	</Nav>
            	</CardHeader>
				{/* fine header */}
				{/* inizio body */}
              	<CardBody>
            		<TabContent className="tab-space" activeTab={"link" + iconTabs}>
                		<TabPane tabId="link1">
                    		<p>
								Situata vicino all'Antico Palazzo Comunale questa torre posta all'angolo tra la salita al Castello e la via di San Giovanni venne costruita nel 1462 durante il marchesato di Ludovico I (1416 - 1475).
								<br />Nel 1556 fu sopraelevata con l’aggiunta del cosiddetto “castello della campana” ovvero una cuspide ottagonale in cui si trovava la grossa campana che ha scandito per diversi anni le attività quotidiane dei saluzzesi.
								<br />Questa torre alta ben 48 metri è da sempre simbolo della comunità cittadina indipendente dal potere marchionale e dall'infulenza religiosa rappresentati rispettivamente dalla Castiglia e dalla Chiesa di San Giovanni.
								<br />L'ultimo restauro nel 1993 ha riportato alla luce i 130 gradini presenti all'interno necessari a raggiungere la sommità della torre, posto dal quale si può godere un panorama spettacolare.
								<br />
								<br />La pianta della Torre Civica è sfalsata di 45° rispetto a quella della torre del campanile della Chiesa di San Giovanni.
                    		</p>
                		</TabPane>
                		<TabPane tabId="link2">
							<p>
								La Chiesa di San Giovanni, costruzione iniziata nel 1281, fu l'edificio religioso più importante presente nella città di Saluzzo fino alla costruzione del Duomo (iniziata nel 1491 e portata a termine nei primi anni del 1500) per volontà del marchese Ludovico II.
								<br />Nel 1376 venne eretto il campanile, quest'ultimo è realizzato con una base rettangolare e una cuspide ottagonale a 4 pinnacoli, osservandolo è possibile notare come esso presenti 5 piani con monofore e bifore.
							</p>
                		</TabPane>
                	</TabContent>
              	</CardBody>
			  	{/* fine body */}
            </Card>
			{/* fine card */}
          </Col>
        </Row>
      </Container>
    </div>
  );
}
