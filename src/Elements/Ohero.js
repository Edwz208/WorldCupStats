
import React, { useEffect, useRef } from 'react';
import './Ohero.css';

export const Ohero = () => {
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
    <section className="Ohero" ref={heroRef}>
      <div className="Ohero-image">
        <img src={`${process.env.PUBLIC_URL}/ALogo.png`} alt="Hero" />
      </div>
      <div className="Ohero-text">
        <h1>Argentina</h1>
        <p>Argentina, the 2022 World Cup Winner, statistically displays<br></br> a strong offense, having both the most shots off target, shots <br></br>on target, and a high average goals scored per game stat. However, <br></br>their lackluster possession stats show that shooting the ball gets <br></br> more wins than passing it around.
        </p>
      </div>
    </section>
  );
};
