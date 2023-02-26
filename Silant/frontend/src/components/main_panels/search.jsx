import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";

const SearchBar = () => {
  const [query, setQuery] = useState([]);

  const onChange = (e) => {
    setQuery(e.target.value);
  };

  return (
    query && (
      <>
        <div>
          <h3>
            Проверьте комплектацию и технические характеристики техники Силант
          </h3>
          <label>Введите заводской номер</label>
          <div className="app-inner-container">
            <form className="app-form">
              <input
                type="text"
                placeholder="0001"
                value={query}
                required
                onChange={onChange}
              />
              <Link to={`car/${query}`}>
                <button type="submit">Поиск</button>
              </Link>
            </form>
          </div>
        </div>
      </>
    )
  );
};
export default SearchBar;
