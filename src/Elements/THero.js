
import React, { useEffect, useRef } from 'react';
import './THero.css';

export const Thero = () => {
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
    <section className="Thero" ref={heroRef}>
      <div className="Thero-image">
        <img src={`${process.env.PUBLIC_URL}/ALogo.png`} alt="Hero" />
      </div>
      <div className="Thero-text">
        <h1>Argentina</h1>
        <p>Argentina statistically displays the strongest offence. Having both <br></br> the most shots off, shots on, and the 2nd most goals scored.</p>
      </div>
    </section>
  );
};
