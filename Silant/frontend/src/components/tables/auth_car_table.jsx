import React from "react";
import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
const AuthCarTable = () => {
  const [cars, setCars] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    async function fetchData() {
      const response = await fetch(`../api/car/`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Token ${localStorage.getItem("token")}`,
        },
      });

      if (!response.ok) {
        const message = `Машина не найдена`;
        setCars(message);
        setError(true);
        setLoading(false);
      } else {
        const jdata = await response.json();
        if (jdata === []) {
          const message = "Машин не найдено";
          setCars(message);
          setError(true);
          setLoading(false);
        } else {
          console.log(jdata);
          setCars(jdata);
          setLoading(false);
        }
      }
    }
    fetchData();
  }, []);
  return loading ? (
    <div>Loading...</div>
  ) : error ? (
    cars
  ) : (
    <div className="app-inner-container">
      <table>
        <thead>
          <tr>
            <th scope="col">Зав. № машины</th>
            <th scope="col">Модель техники</th>
            <th scope="col">Модель двигателя</th>
            <th scope="col">Зав. № двигателя</th>
            <th scope="col">Модель трансмиссии</th>
            <th scope="col">Зав. № трансмиссии</th>
            <th scope="col">Модель вед. моста</th>
            <th scope="col">Зав. № вед. моста</th>
            <th scope="col">Модель упр. моста</th>
            <th scope="col">Зав. № упр. моста</th>

            <th scope="col">Дата отгрузки</th>
            <th scope="col">Покупатель</th>
            <th scope="col">Грузополучатель</th>
            <th scope="col">Сервисная компания</th>
          </tr>
        </thead>
        <tbody>
          {cars.map((car) => (
            <tr key={car.serial_number}>
              <td data-label="Зав. № машины">
                <Link to={`../../cars/${car.serial_number}`}>
                  {car.serial_number}
                </Link>
              </td>

              <td data-label="Модель техники">
                <Link to={`../../manual/${car.model}`}>{car.model_name}</Link>
              </td>

              <td data-label="Модель двигателя">
                <Link to={`../../manual/${car.engine_model}`}>
                  {car.engine_model_name}
                </Link>
              </td>

              <td data-label="Зав. № двигателя">{car.engine_serial_number}</td>

              <td data-label="Модель трансмиссии">
                <Link to={`../../manual/${car.transmission_model}`}>
                  {car.transmission_model_name}
                </Link>
              </td>

              <td data-label="Зав. № трансмиссии">
                {car.transmission_serial_number}
              </td>
              <td data-label="Модель вед. моста">
                <Link to={`../../manual/${car.driving_axle_model}`}>
                  {car.driving_axle_model_name}
                </Link>
              </td>
              <td data-label="Зав. № вед. моста">
                {car.driving_axle_serial_number}
              </td>
              <td data-label="Модель упр. моста">
                <Link to={`../../manual/${car.steering_axle_model}`}>
                  {car.steering_axle_model_name}
                </Link>
              </td>
              <td data-label="Зав. № упр. моста">
                {car.steering_axle_serial_number}
              </td>

              <td data-label="Датаотгрузки">{car.shipment_date}</td>
              <td data-label="Покупатель">{car.buyer_name}</td>
              <td data-label="Грузополучатель">{car.consignee}</td>
              <td data-label="Сервисная компания">
                <Link to={`../../company/${car.service_company}`}>
                  {car.service_company_name}
                </Link>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};
export default AuthCarTable;
