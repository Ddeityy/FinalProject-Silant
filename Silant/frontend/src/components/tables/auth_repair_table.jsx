import React from "react";
import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
const AuthRepairTable = () => {
  const [repair, setRepair] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    async function fetchData() {
      const response = await fetch(`../api/repair/`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Token ${localStorage.getItem("token")}`,
        },
      });

      if (!response.ok) {
        const message = `ТО не найдено`;
        setRepair(message);
        setError(true);
        setLoading(false);
      } else {
        const jdata = await response.json();
        console.log(jdata);
        if (jdata === []) {
          const message = "ТО не найдено";
          setRepair(message);
          setError(true);
          setLoading(false);
        } else {
          setRepair(jdata);
          setLoading(false);
        }
      }
    }
    fetchData();
  }, []);
  return loading ? (
    <div>Loading...</div>
  ) : error ? (
    repair
  ) : (
    <div className="app-inner-container">
      <table>
        <thead>
          <tr>
            <th scope="col">Зав. № машины</th>
            <th scope="col">Дата отказа</th>
            <th scope="col">Наработка, м/час</th>
            <th scope="col">Узел отказа</th>
            <th scope="col">Описание отказа</th>
            <th scope="col">Способ восстановления</th>
            <th scope="col">Исп. запчасти</th>
            <th scope="col">Дата восстановления</th>
            <th scope="col">Время простоя</th>
          </tr>
        </thead>
        <tbody>
          {repair.map((m) => (
            <tr key={m.id}>
              <td data-label="Зав. № машины">
                <Link to={`../../cars/${m.car_serial_number}`}>
                  {m.car_serial_number}
                </Link>
              </td>
              <td data-label="Дата отказа">{m.issue_date}</td>
              <td data-label="Наработка, м/час">{m.operating_time}</td>
              <td data-label="Узел отказа">{m.unit_name}</td>
              <td data-label="Описание отказа">{m.description}</td>
              <td data-label="Способ восстановления">{m.method_name}</td>
              <td data-label="Исп. запчасти">{m.repair_parts}</td>
              <td data-label="Дата восстановления">{m.completion_date}</td>
              <td data-label="Время простоя">{m.repair_time} д.</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};
export default AuthRepairTable;
