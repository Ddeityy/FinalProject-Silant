import React, { useState, useEffect} from 'react';


const Logout = () => {
  const [isAuth, setIsAuth] = useState(Boolean);

  useEffect(() => {
    if (localStorage.getItem('token') == null) {
      setIsAuth(true)
      window.location.replace('http://127.0.0.1:8002/')
    } else {
      setIsAuth(false);
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
        window.location.replace('http://127.0.0.1:8002/')
      });
  };

  return (
    <div className='app-container'>
      {isAuth && (
        <form className='app-form'>
          <label>Вы уверены, что хотите выйти?</label>
          <br />
          <input type='submit' value='Выйти' onClick={handleLogout} />
        </form>
      )}
      <form className='app-form'>
          <label>Вы уверены, что хотите выйти?</label>
          <br />
          <input type='submit' value='Выйти' onClick={handleLogout} />
        </form>
    </div>
  );
};

export default Logout;