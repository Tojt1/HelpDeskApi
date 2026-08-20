import {useEffect} from "react";
import {useState} from "react";

function Settings (){
    const [informations, setInformations] = useState([])
    useEffect(()=> {
        const token = localStorage.getItem("token")

        const getData = async () => {
            const respose = await fetch("http://localhost:8000/me", {
                headers:{
                    "Authorization":`Bearer ${token}`
                }
            })

            const data = await respose.json()
            setInformations(data)
        }
        getData();
    }
    , [])

    return(
        <>
            <p>{informations.name}</p>
            <button className="change-name">Change</button>
            <p>{informations.email}</p>
            <button className="change-email">change</button>
            <p>{informations.created}</p>
        </>
    )
}

export default Settings