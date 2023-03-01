import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import GeneralPanel from "./main_panels/general_panel.jsx";
import AppFooter from "./footer/footer.jsx";
import AppHeader from "./header/header.jsx";
import Login from "./header/login.jsx";
import Logout from "./header/logout.jsx";
import CarTable from "./tables/unauth_car_table.jsx";
import GeneralManual from "./tables/manual.jsx";
import AuthCarDetail from "./tables/auth_car_detail.jsx";
import Company from "./tables/company.jsx";
import "./styles.css";
import Delete from "./user_forms/generic_delete.jsx";

const App = () => {
  return (
    <div className="App">
      <Router>
        <AppHeader />
        <Routes>
          <Route path="/login" element={<Login />} exact />
          <Route path="/logout" element={<Logout />} exact />
          <Route path="/" element={<GeneralPanel />} exact />
          <Route path="/company/:id" element={<Company />} exact />
          <Route path="/car/:id" element={<CarTable />} exact />
          <Route path="/car/details/:id/delete" element={<Delete />} />
          <Route path="/car/details/:id" element={<AuthCarDetail />} />
          <Route path="/manual/:id" element={<GeneralManual />} />
        </Routes>
        <AppFooter />
      </Router>
    </div>
  );
};

export default App;
