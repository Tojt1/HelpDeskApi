import {useEffect} from "react";
import {useState} from "react";
import ChangeEmail from "../components/ChangeEmail.jsx";
import ChangePassword from "../components/ChangePassword.jsx";

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
            <ChangeEmail />
            <p>{informations.email}</p>
            <ChangePassword />
            <p>{informations.created}</p>
        </>
    )
}

export default Settings