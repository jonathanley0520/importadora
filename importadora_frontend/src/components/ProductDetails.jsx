// src/components/ProductDetails.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ProductDetails = ({ match }) => {
  const [product, setProduct] = useState(null);

  useEffect(() => {
    const fetchProduct = async () => {
      try {
        const response = await axios.get(`http://localhost:8000/api/products/${match.params.id}/`);
        setProduct(response.data);
      } catch (error) {
        console.error('Error fetching product details:', error);
      }
    };

    fetchProduct();
  }, [match.params.id]);

  if (!product) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h2>{product.name}</h2>
      <p>Weight: {product.weight} kg</p>
      <p>Volume: {product.volume} m³</p>
      {/* Add more details as needed */}
    </div>
  );
};

export default ProductDetails;
