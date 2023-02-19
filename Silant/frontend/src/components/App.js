import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Dashboard from './dashboard';
import AppHeader from './header';
import AppFooter from './footer';
import Login from './login';
import Logout from './logout';




const App = () => {
  return (
    <div className='App'>
      <Router>
        <AppHeader />
        <Routes>
          <Route path='/login' element={<Login />} exact />
          <Route path="/" element={<Dashboard />} exact />
          <Route path='/logout' element={<Logout />} exact />
        </Routes>
        <AppFooter />
      </Router>
    </div>
  );
};

export default App;