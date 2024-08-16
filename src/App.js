import React from 'react'
import logo from './logo.svg';
import './App.css';
import { Header } from './Elements/Header';
import { Hero } from './Elements/Hero';
import { COffense } from './Elements/COffense';
import { Ohero } from './Elements/Ohero';
import { Defense } from './Elements/Control';
import { Chero } from './Elements/CHero';
import { FOffense } from './Elements/FOffense';
import { Fhero } from './Elements/FHero'
import { TOffense } from './Elements/TOffense';
import { Thero } from './Elements/THero';
import { Titletext } from './Elements/Titletext';
import { Ttwo } from './Elements/Ttwo';
import { TThree } from './Elements/TThree';
import { TFour } from './Elements/TFour';
import { SpiderGraph } from './Elements/SpiderGraph'
import { TFive } from './Elements/TFive';

function App() {
  return (
    <div className="App">
      <Header />
      <Hero />
      <COffense />
      <Ohero />
      <Defense />
      <Chero />
      <FOffense />
      <Fhero /> 
      <TOffense />
      <Thero /> 
      <Titletext /> 
      <Ttwo />
      <TThree />
      <TFour />
      <SpiderGraph />
      <TFive />
      <div id="Offense" className="top-offense"></div>
      <div id="Defense" className="top-defense"></div>
      <div id="Fouls" className="top-fouls"></div>
      <div id="TeamPlay" className="top-teamplay"></div>
      <div id="TeamStats" className="top-teamstats"></div>

    </div>
  );
}

export default App;
