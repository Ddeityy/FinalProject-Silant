import React, { useState, useEffect } from "react";
import SearchBar from "./search.jsx";
import AuthPanel from "./auth_panel.jsx";

const GeneralPanel = () => {
  const [userData, setUserData] = useState([]);
  const [Auth, setAuth] = useState([]);

  useEffect(() => {
    const fetchUserData = async () => {
      const data = await fetch(`http://127.0.0.1:8002/api/user/current/`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Token ${localStorage.getItem("token")}`,
        },
      });

      const jdata = await data.json();
      console.log(jdata);
      setUserData(jdata);
      setAuth(true);
    };
    if (localStorage.getItem("token") === null) {
      setAuth(false);
    } else {
      fetch("http://127.0.0.1:8002/api/auth/user/", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Token ${localStorage.getItem("token")}`,
        },
      })
        .then((res) => res.json())
        .then(() => {
          fetchUserData();
        });
    }
  }, []);

  return (
    <div className="app-container">
      {Auth ? (
        <>
          <h2 className="app-inner-container">{userData.name}</h2>
          <div className="app-inner-container">
            <AuthPanel />
          </div>
        </>
      ) : (
        <>
          <div className="app-inner-container">
            <SearchBar />
          </div>
        </>
      )}
    </div>
  );
};

export default GeneralPanel;
