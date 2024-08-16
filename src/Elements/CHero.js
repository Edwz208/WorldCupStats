
import React, { useEffect, useRef } from 'react';
import './CHero.css';

export const Chero = () => {
  const heroRef = useRef(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          heroRef.current.classList.add('fade-in');
          heroRef.current.classList.remove('fade-out');
        } else {
          heroRef.current.classList.add('fade-out');
          heroRef.current.classList.remove('fade-in');
        }
      },
      {
        threshold: 0.3, 
      }
    );

    if (heroRef.current) {
      observer.observe(heroRef.current);
    }

    return () => {
      if (heroRef.current) {
        observer.unobserve(heroRef.current);
      }
    };
  }, []);

  return (
    <section className="Chero" ref={heroRef}>
      <div className="Chero-image">
        <img src={`${process.env.PUBLIC_URL}/NLogo.svg`} alt="Hero" />
      </div>
      <div className="Chero-text">
        <h1>Netherlands</h1>
        <p>The Netherlands had a mediocre average defensive pressures<br></br> applied per game stat, but they had a very high average forced<br></br> turnovers stat and a very low average goals conceded per game. This <br></br>demonstrates how attacking opposing defenders at the right time <br></br>opposed to all the time is the best way to play defense.</p>
      </div>
    </section>
  );
};
