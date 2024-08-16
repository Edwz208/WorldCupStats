import React from 'react'
import './header.css'
export const Header = () => {
  return (
   <header className="header">
      <img src={`${process.env.PUBLIC_URL}/Logo-Soccer.png`} alt="Logo" className="navbar-logo" />

      <nav className="navbar">
        <a href="#Offense">Offense</a>
        <a href="#Defense">Defense</a>
        <a href="#Fouls">Fouls</a>
        <a href="#TeamPlay">Team Play</a>
        <a href="#TeamStats"> Team Stats</a>




      </nav>
   </header>
  )

}
