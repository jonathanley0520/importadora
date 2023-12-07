// src/pages/ProductPage.js
import React from 'react';
import {Switch, Route} from 'react-router-dom';
import ProductList from '../components/ProductList';
import ProductDetails from '../components/ProductDetails';

const ProductPage = ({ match }) => {
  return (
    <div>
      <Switch>
        <Route exact path={match.path} component={ProductList} />
        <Route path={`${match.path}/:id`} component={ProductDetails} />
      </Switch>
    </div>
  );
};

export default ProductPage;
