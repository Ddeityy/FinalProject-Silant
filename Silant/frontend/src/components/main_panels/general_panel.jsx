import React, { useState, useEffect } from 'react';

const GeneralPanel = () => {
  const [userUsername, setUsername] = useState('');
  const [isAuth, setIsAuth] = useState(Boolean)
  const [userData, setUserData] = useState("")

  useEffect(() => {
    const fetchUserData = async (pk) => {
      const data = await fetch(`http://127.0.0.1:8002/api/users/${pk}`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Token ${localStorage.getItem('token')}`
        }
      })
      const jdata = await data.json()
      console.log(jdata)
      setUserData(jdata)
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
          console.log(data.pk)
          setIsAuth(true)
          fetchUserData(data.pk)
        })
      setUsername(userData.name)
    }
  }, []);

  return (
    <div className='app-container'>
      {isAuth ?
        <>
          <h2>{userUsername}</h2>
        </>
        :
        <>
          <h1>Проверьте комплектацию и технические характеристики техники Силант</h1>
        </>
      }
    </div>
  );
}

export default GeneralPanel;