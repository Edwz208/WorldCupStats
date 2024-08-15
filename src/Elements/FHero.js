
import React, { useEffect, useRef } from 'react';
import './FHero.css';

export const Fhero = () => {
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
    <section className="Fhero" ref={heroRef}>
      <div className="Fhero-image">
        <img src={`${process.env.PUBLIC_URL}/ALogo.png`} alt="Hero" />
      </div>
      <div className="Fhero-text">
        <h1>Argentina</h1>
        <p>Argentina statistically displays the strongest offence. Having both <br></br> the most shots off, shots on, and the 2nd most goals scored.</p>
      </div>
    </section>
  );
};
