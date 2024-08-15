import React, { useEffect, useState, useRef } from "react";
import { motion, useMotionValue } from "framer-motion";
import crosses from './crosses.png';
import assists from './passes_assists.png';
import './TOffense.css'


const imgs = [
  assists,
  crosses
];


const ONE_SECOND = 1000;
const AUTO_DELAY = ONE_SECOND * 10;
const DRAG_BUFFER = 50;

const SPRING_OPTIONS = {
  type: "spring",
  mass: 3,
  stiffness: 400,
  damping: 50,
};

export const TOffense = () => {

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
            threshold: 0.2, 
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

  const [imgIndex, setImgIndex] = useState(0);

  const dragX = useMotionValue(0);

  useEffect(() => {
    const intervalRef = setInterval(() => {
      const x = dragX.get();

      if (x === 0) {
        setImgIndex((pv) => {
          if (pv === imgs.length - 1) {
            return 0;
          }
          return pv + 1;
        });
      }
    }, AUTO_DELAY);

    return () => clearInterval(intervalRef);
  }, []);

  const onDragEnd = () => {
    const x = dragX.get();

    if (x <= -DRAG_BUFFER && imgIndex < imgs.length - 1) {
      setImgIndex((pv) => pv + 1);
    } else if (x >= DRAG_BUFFER && imgIndex > 0) {
      setImgIndex((pv) => pv - 1);
    }
  };

  return (
    <div className="Tcarousel-container">
      <motion.div
        drag="x"
        dragConstraints={{
          left: 0,
          right: 0,
        }}
        style={{
          x: dragX,
        }}
        animate={{
          translateX: `-${imgIndex * 100}%`,
        }}
        transition={SPRING_OPTIONS}
        onDragEnd={onDragEnd}
        className="Tcarousel-inner"
      >
        <Images imgIndex={imgIndex} />
      </motion.div>

      <dots imgIndex={imgIndex} setImgIndex={setImgIndex} />
      <GradientEdges />
    </div>
  
  );
};

const Images = ({ imgIndex }) => {
  return (
    <>
      {imgs.map((imgSrc, idx) => (
        <motion.div
          key={idx}
          style={{
            backgroundImage: `url(${imgSrc})`,
          }}
          animate={{
            scale: imgIndex === idx ? 0.95 : 0.85,
          }}
          transition={SPRING_OPTIONS}
          className="image-container"
        >

        </motion.div>
      ))}
    </>
  );
};

const dots = ({ imgIndex, setImgIndex }) => {
  return (
    <div className="Tdots-container">
      {imgs.map((_, idx) => (
        <button
          key={idx}
          onClick={() => setImgIndex(idx)}
          className={`Tdot ${idx === imgIndex ? "Tdot-active" : "Tdot-inactive"}`}
        />
      ))}
    </div>
  );
};

const GradientEdges = () => {
  return (
    <>
      <div className="gradient-edge gradient-edge-left" />
      <div className="gradient-edge gradient-edge-right" />
    </>
  );
};

