import React from 'react'
import logo from './logo.svg';
import './App.css';
import { Header } from './Elements/Header';
import { Hero } from './Elements/Hero';
import { COffense } from './Elements/COffense';

function App() {
  return (
    <div className="App">
      <Header />
      <Hero />
      <COffense />
    </div>
  );
}

export default App;
