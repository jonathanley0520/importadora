import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from '../pages/Home';
import ProductPage from '../pages/ProductPage';
import ShoppingCartPage from '../pages/ShoppingCartPage';

function App() {
  return (
    <Router>
      <div>
        <Switch>
          <Route path="/products" component={ProductPage} />
          <Route path="/shopping-cart" component={ShoppingCartPage} />
          <Route path="/" component={Home} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;

