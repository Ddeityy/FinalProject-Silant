import React, { useState, useEffect } from 'react';
import SearchBar from './search.jsx';

const GeneralPanel = () => {
  const [username, setUsername] = useState('');
  const [isAuth, setIsAuth] = useState(Boolean)
  const [userData, setUserData] = useState("")

  useEffect(() => {
    const fetchUserData = async () => {
      const data = await fetch(`http://127.0.0.1:8002/api/users/current/`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Token ${localStorage.getItem('token')}`
        }
      })
      const jdata = await data.json()
      setUserData(jdata)
      setUsername(jdata.name)
    }

    if (localStorage.getItem('token') === null) {
      setIsAuth(false)
    } else {
      fetch('http://127.0.0.1:8002/api/auth/user/', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Token ${localStorage.getItem('token')}`
        }
      })
        .then(res => res.json())
        .then(data => {
          console.log(data)
          setIsAuth(true)
          fetchUserData()
        })
    }
  }, []);

  return (
    <div className='app-container'>
      <div className='app-inner-container'>
      {isAuth ?
        <>
          <h2>{username}</h2>
        </>
        :
        <>
          <h1>Проверьте комплектацию и технические характеристики техники Силант</h1>
          <SearchBar />
        </>
      }
      </div>
    </div>
  );
}

export default GeneralPanel;