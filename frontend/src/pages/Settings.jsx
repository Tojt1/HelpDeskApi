import {useEffect} from "react";
import {useState} from "react";
import ChangeEmail from "../components/ChangeEmail.jsx";
import ChangePassword from "../components/ChangePassword.jsx";
import "./Settings.css"

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
        <div className="setting-container">

            <div className="setting-row">
            <p>{informations.name}</p>
            <ChangeEmail />
            </div>

            <div className="setting-row">
            <p>{informations.email}</p>
            <ChangePassword />
            </div>

            <div className="setting-row">
            <p>{informations.created}</p>
            </div>

        </div>
    )
}

export default Settings