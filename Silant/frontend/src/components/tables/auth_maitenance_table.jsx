import React from "react";
import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
const AuthMaitenanceTable = () => {
  const [maitenance, setMaitenance] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    async function fetchData() {
      const response = await fetch(`../api/maitenance/`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Token ${localStorage.getItem("token")}`,
        },
      });

      if (!response.ok) {
        const message = `ТО не найдено`;
        setMaitenance(message);
        setError(true);
        setLoading(false);
      } else {
        const jdata = await response.json();
        console.log(jdata);
        if (jdata === []) {
          const message = "ТО не найдено";
          setMaitenance(message);
          setError(true);
          setLoading(false);
        } else {
          setMaitenance(jdata);
          setLoading(false);
        }
      }
    }
    fetchData();
  }, []);
  return loading ? (
    <div>Loading...</div>
  ) : error ? (
    maitenance
  ) : (
    <div className="app-inner-container">
      <table>
        <thead>
          <tr>
            <th scope="col">Зав. № машины</th>
            <th scope="col">Вид ТО</th>
            <th scope="col">Дата проведениия</th>
            <th scope="col">Наработка, м/час</th>
            <th scope="col">№ заказ-наряда</th>
            <th scope="col">Дата заказ-наряда</th>
            <th scope="col">Орг. проводившая ТО</th>
          </tr>
        </thead>
        <tbody>
          {maitenance.map((m) => (
            <tr key={m.id}>
              <td data-label="Зав. № машины">
                <Link to={`../../cars/${m.car_serial_number}`}>
                  {m.car_serial_number}
                </Link>
              </td>

              <td data-label="Вид ТО">
                <Link to={`../../manual/${m.type}`}>{m.type_name}</Link>
              </td>

              <td data-label="Дата проведения">{m.date}</td>

              <td data-label="Наработка, м/час<">{m.operating_time}</td>

              <td data-label="№ Заказ-наряда">{m.contract_serial_number}</td>

              <td data-label="Дата заказ-наряда">{m.contract_date}</td>
              <td data-label="Орг. проводившая ТО">
                <Link to={`../../company/${m.service_company}`}>
                  {m.service_company_name}
                </Link>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};
export default AuthMaitenanceTable;
