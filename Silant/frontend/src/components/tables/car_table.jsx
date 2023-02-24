import "./tables.css";
import { useParams } from "react-router-dom";
import React, { useEffect, useState } from "react";

const CarTable = () => {
  const [car, setCar] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  const { id } = useParams();

  console.log(id);

  useEffect(() => {
    async function fetchData() {
      const response = await fetch(`../api/cars/${id}/`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      });

      if (!response.ok) {
        const message = `Машина не найдена`;
        setCar(message);
        setError(true);
        setLoading(false);
      } else {
        const jdata = await response.json();
        setCar(jdata);
        setLoading(false);
      }
    }
    fetchData();
  }, []);

  return loading ? (
    <div>Loading...</div>
  ) : error ? (
    car
  ) : (
    <div className="app-container">
      <div className="app-inner-container">
        <h1>Результат поиска:</h1>
        <table>
          <thead>
            <tr>
              <th scope="col">Зав. № машины</th>
              <th scope="col">Модель техники</th>
              <th scope="col">Модель двигателя</th>
              <th scope="col">Зав. № двигателя</th>
              <th scope="col">Модель транс миссии</th>
              <th scope="col">Зав. № транс миссии</th>
              <th scope="col">Модель вед. моста</th>
              <th scope="col">Зав. № вед. моста</th>
              <th scope="col">Модель упр. моста</th>
              <th scope="col">Зав. № упр. моста</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td data-label="Зав. № машины">{car.serial_number}</td>
              <td data-label="Модель техники">{car.model_name}</td>
              <td data-label="Модель двигателя">{car.engine_model_name}</td>
              <td data-label="Зав. № двигателя">{car.engine_serial_number}</td>
              <td data-label="Модель трансмиссии">
                {car.transmission_model_name}
              </td>
              <td data-label="Зав. № трансмиссии">
                {car.transmission_serial_number}
              </td>
              <td data-label="Модель вед. моста">
                {car.driving_axle_model_name}
              </td>
              <td data-label="Зав. № вед. моста">
                {car.driving_axle_serial_number}
              </td>
              <td data-label="Модель упр. моста">
                {car.steering_axle_model_name}
              </td>
              <td data-label="Зав. № упр. моста">
                {car.steering_axle_serial_number}
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default CarTable;
