
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
        <img src={`${process.env.PUBLIC_URL}/fLogo.png`} alt="Hero" />
      </div>
      <div className="Thero-text">
        <h1>France</h1>
        <p>France, the 2022 World Cup Silver Medalist, had the <br></br> highest number of assists of the entire tournament, albeit <br></br> a normal number of average passes per game, showing the <br></br>value of quality over quantity in passing.</p>
      </div>
    </section>
  );
};
