
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
        <p>Argentina, the 2022 World Cup Winner, had no red, <br></br> cards the entire tournament, albeit many yellow cards, and<br></br> scored the most penalties of the tournament. This shows the <br></br> importance of playing clean to avoid red cards and penalties and <br></br> capitalizing on penalties when other teams don't play clean.
        </p>
      </div>
    </section>
  );
};
