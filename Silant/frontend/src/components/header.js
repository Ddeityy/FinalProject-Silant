import React, { useState, useEffect, Fragment } from 'react';
import { Link } from 'react-router-dom';

const AppHeader = () => {
  const [isAuth, setIsAuth] = useState(false);

  useEffect(() => {
    if (localStorage.getItem('token') !== null) {
      setIsAuth(true);
    }
  }, []);

  return (
    <div className='app-header'>
      <h1>Django React Auth</h1>
      <ul>
        {isAuth === true ? (
          <Fragment>
            {' '}
            <li>
              <Link to='/logout'>Выйти</Link>
            </li>
          </Fragment>
        ) : (
          <Fragment>
            {' '}
            <li>
              <Link to='/login'>Войти</Link>
            </li>
          </Fragment>
        )}
      </ul>
    </div>
  );
};

export default AppHeader;