import React from "react";
import { useParams, useNavigate } from "react-router-dom";

const Delete = () => {
  const { id } = useParams();
  console.log(location.pathname);

  const handleYes = () => {
    fetch(`http://127.0.0.1:8002/api/car/${id}/`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${localStorage.getItem("token")}`,
      },
    })
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        window.location.replace("http://127.0.0.1:8002/");
      });
  };

  const handleNo = () => {
    window.location.replace("http://127.0.0.1:8002/");
  };

  return (
    <>
      <h1>Вы уверены?</h1>
      <button onClick={handleYes}>Да</button>
      <button onClick={handleNo}>Нет</button>
    </>
  );
};

export default Delete;
