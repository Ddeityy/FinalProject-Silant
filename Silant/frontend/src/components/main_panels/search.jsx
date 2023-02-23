import React, { useEffect, useState } from "react"
import CarTable from "../tables/car_table.jsx"
//import useState from "react-usestateref"

const SearchBar = () => {

    const [query, setQuery] = useState("")
    const [loading, setLoading] = useState(true)

    const onChange = (e) => {
        setQuery(e.target.value)
    };

    const onSubmit = async (e) => {
        e.preventDefault();
        setLoading(false)
    };
    return (loading ?
        <>
            <form className='app-form' onSubmit={onSubmit}>
                <input type="text" placeholder="0001" value={query} required onChange={onChange} />
                <input type="button" value="Поиск" />
            </form>
        </>
        :
        <>
            <form className='app-form' onSubmit={onSubmit}>
                <input type="text" placeholder="0001" value={query} required onChange={onChange} />
                <input type="button" value="Поиск" />
            </form>
            <CarTable serial={query} />
        </>
    )
}
export default SearchBar;