// src/pages/Home.js
import React from 'react';
import { Link } from 'react-router-dom';

const Home = () => {
  return (
    <div>
      <h1>Welcome to Importadora Tecnologia</h1>
      <p>Explore our products and start shopping!</p>
      <Link to="/products">View Products</Link>
    </div>
  );
};

export default Home;
