import React from 'react'
import "./Header.css"

const Header = (props) => {
  return (
    <div class="row header">
        <div class="col-1 bordi logo"><img src={props.valori.pathlogo} alt="" width="100%"></img></div>
        <div class="col-2 bordi link"><a target={"new"} href={props.valori.link1.url}>{props.valori.link1.anchor}</a></div>
        <div class="col-2 bordi link"><a target={"new"} href={props.valori.link2.url}>{props.valori.link2.anchor}</a></div>
        <div class="col-2 bordi link"><a target={"new"} href={props.valori.link3.url}>{props.valori.link3.anchor}</a></div>
        <div class="col-2 bordi link"><a target={"new"} href={props.valori.link4.url}>{props.valori.link4.anchor}</a></div>
    </div>
  )
}

export default Header