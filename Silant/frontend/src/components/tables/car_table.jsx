import {
    Table, TableBody,
    TableCell,
    TableHead,
    TableRow
} from '@mui/material';

import { dividerClasses } from '@mui/material';
import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

const CarTable = (props) => {
    const [carData, setCarData] = useState([])
    const [loading, setLoading] = useState(true)
    const query = props.serial

    useEffect(() => {
        async function fetchData() {
            const response = await fetch(`http://127.0.0.1:8002/api/cars/${query}/`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            const jdata = await response.json()
            setCarData(jdata)
            setLoading(false)
        };
        fetchData();
    }
        , [])


    return (loading ?
        <div>
            Loading...
        </div>
        :
        <div>
            <h1>Результат поиска:</h1>
            {carData.model}
        </div>
    )
}

export default CarTable