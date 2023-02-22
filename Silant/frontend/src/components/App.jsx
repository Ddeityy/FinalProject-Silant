import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import GeneralPanel from './main_panels/general_panel.jsx';
import AppFooter from './footer/footer.jsx';
import AppHeader from './header/header.jsx';
import Login from './header/login.jsx';
import Logout from './header/logout.jsx';
import "./styles.css"




const App = () => {
  return (
    <div className='App'>
      <Router>
        <AppHeader />
        <Routes>
          <Route path='/login' element={<Login />} exact />
          <Route path='/logout' element={<Logout />} exact />
          <Route path="/" element={<GeneralPanel />} exact />
        </Routes>
        <AppFooter />
      </Router>
    </div>
  );
};

export default App;