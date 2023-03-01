import React, { useEffect, useState } from "react";
import { useForm } from "react-hook-form";

const ManualCreate = () => {
  const [manuals, setManuals] = useState([]);
  const [loading, setLoading] = useState(true);

  const { register, handleSubmit } = useForm();

  const onSubmit = (data) => {
    fetch("http://127.0.0.1:8002/api/maitenance/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${localStorage.getItem("token")}`,
      },
      body: JSON.stringify(data),
    }).then(window.location.replace("http://127.0.0.1:8002/"));
  };

  const handleSelect = (data, t, name) => {
    return data.filter((i) => i[t] !== name);
  };

  useEffect(() => {
    const fetchManuals = async () => {
      const response = await fetch("http://127.0.0.1:8002/api/manual/");
      const data = await response.json();
      setManuals(data);
    };
    fetchManuals();
    setLoading(false);
  }, []);

  return (
    !loading && (
      <div className="app-container">
        <form onSubmit={handleSubmit(onSubmit)} className="app-form">
          <label>Название</label>
          <input {...register("name")} />
          <br />
          <label>Описание</label>
          <input {...register("description")} />
          <br />
          <label>Зав. № машины</label>
          <select required {...register("manual_type")}>
            <option value=""></option>
            {handleSelect(manuals, "manual_type", "Компания").map((model) => (
              <option key={model.id} value={model.id}>
                {model.manual_type}
              </option>
            ))}
          </select>
          <br />
          <button type="submit">Отправить</button>
        </form>
      </div>
    )
  );
};

export default ManualCreate;
