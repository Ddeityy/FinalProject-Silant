import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";

const GeneralManual = () => {
  const [data, setData] = useState([]);
  const { id } = useParams();

  console.log(window.location.pathname);

  useEffect();
  return data && <div>hello</div>;
};

export default GeneralManual;
