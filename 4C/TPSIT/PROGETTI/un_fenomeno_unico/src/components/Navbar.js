/*
COMPONENTE NAVBAR
Navbar contenente titolo e link esterni che diventa un menu a tendina quando le dimensioni dello schemro si riducono
*/
import React from "react";
import { Link } from "react-router-dom";
import {
  Collapse,
  NavbarBrand,
  Navbar,
  NavItem,
  NavLink,
  Nav,
  Container,
  Row,
  Col
} from "reactstrap";

export default function IndexNavbar() {
  const [collapseOpen, setCollapseOpen] = React.useState(false);
  const [collapseOut, setCollapseOut] = React.useState("");
  const [color, setColor] = React.useState("navbar-transparent");

  React.useEffect(() => {
    window.addEventListener("scroll", changeColor);
    return function cleanup() {
      window.removeEventListener("scroll", changeColor);
    };
  }, []);
  const changeColor = () => {
    if (
      document.documentElement.scrollTop > 99 ||
      document.body.scrollTop > 99
    ) {
      setColor("bg-info");
    } else if (
      document.documentElement.scrollTop < 100 ||
      document.body.scrollTop < 100
    ) {
      setColor("navbar-transparent");
    }
  };
  const toggleCollapse = () => {
    document.documentElement.classList.toggle("nav-open");
    setCollapseOpen(!collapseOpen);
  };
  const onCollapseExiting = () => {
    setCollapseOut("collapsing-out");
  };
  const onCollapseExited = () => {
    setCollapseOut("");
  };
  return (
    <Navbar className={"fixed-top " + color} color-on-scroll="100" expand="lg">      
      <Container>
        <div className="navbar-translate">
          
          {/* TITOLO NAVBAR ESTESA*/}
          <NavbarBrand to="/" tag={Link} id="navbar-brand">
            <span>4C Bracco Mattia · Un fenomeno unico</span>
          </NavbarBrand>

          {/* LINEE NAVBAR A TENDINA */}
          <button aria-expanded={collapseOpen} className="navbar-toggler navbar-toggler" onClick={toggleCollapse}>
            <span className="navbar-toggler-bar bar1" />
            <span className="navbar-toggler-bar bar2" />
            <span className="navbar-toggler-bar bar3" />
          </button>
        </div>

        <Collapse className={"justify-content-end " + collapseOut} navbar isOpen={collapseOpen} onExiting={onCollapseExiting} onExited={onCollapseExited}>
          
          {/* INIZIO NAVBAR A TENDINA */}
          <div className="navbar-collapse-header">
            <Row>
              {/* TITOLO NAVBAR A TENDINA*/}
              <Col className="collapse-brand" xs="6">
                <a href="#" onClick={(e) => e.preventDefault()}>
                  4C Bracco Mattia · Un fenomeno unico
                </a>
              </Col>
              <Col className="collapse-close text-right" xs="6">
                <button aria-expanded={collapseOpen} className="navbar-toggler" onClick={toggleCollapse}>
                  <i className="tim-icons icon-simple-remove" />
                </button>
              </Col>
            </Row>
          </div>

          {/* INIZIO LOGHI COLLEGAMENTO */}
          <Nav navbar>

            {/* LOGO COLLEGAMENTO INSTAGRAM */}
            <NavItem className="p-0">
              {/* LINK */}
              <NavLink data-placement="bottom" href="https://www.instagram.com/matti_bracco/" rel="noopener noreferrer" target="_blank">
              {/* ICONA */}
              <i className="fab fa-instagram" />
              {/* NOME */}
              <p className="d-lg-none d-xl-none">Instagram</p>
              </NavLink>
            </NavItem>

            {/* LOGO COLLEGAMENTO GITHUB */}
            <NavItem className="p-0">
              {/* LINK */}
              <NavLink data-placement="bottom" href="https://github.com/MattiaBracco05" rel="noopener noreferrer" target="_blank">
              {/* ICONA */}
              <i class="fab fa-github"></i>
              {/* NOME */}
              <p className="d-lg-none d-xl-none">Github</p>
              </NavLink>
            </NavItem>

          </Nav>

        </Collapse>
      </Container>
    </Navbar>
  );
}
