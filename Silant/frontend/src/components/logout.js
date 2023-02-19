import React, { useState, useEffect, Fragment } from 'react';

const Logout = () => {
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (localStorage.getItem('token') == null) {
      window.location.replace('http://localhost:8002');
    } else {
      setLoading(false);
    }
  }, []);

  const handleLogout = e => {
    e.preventDefault();

    fetch('http://127.0.0.1:8002/api/auth/logout/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Token ${localStorage.getItem('token')}`
      }
    })
      .then(res => res.json())
      .then(data => {
        console.log(data);
        localStorage.clear();
        window.location.replace('http://localhost:8002/');
      });
  };

  return (
    <div className='app-header'>
      {loading === false && (
        <>
          <h1>Вы уверены, что хотите выйти?</h1>
          <input type='button' value='Выйти' onClick={handleLogout} />
        </>
      )}
    </div>
  );
};

export default Logout;