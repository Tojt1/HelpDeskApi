import {useState, useEffect} from "react";
import ChangeEmail from "../../components/commons/ChangeEmail.jsx";
import ChangeName from "../../components/commons/ChangeName.jsx";
import ChangePassword from "../../components/commons/ChangePassword.jsx";
import "./AdminSettings.css"

function AdminSettings (){
    const [admin, setAdmin] = useState([])
    const token = localStorage.getItem("token")

    useEffect(() => {
        const getUser = async () => {
            const response = await fetch("http://localhost:8000/me",{
                headers:{
                    "Authorization":`Bearer ${token}`
                }
            })
            const data = await response.json()
            console.log(data)
            setAdmin(data)
        }
        getUser();
    }, []);
    return(
        <div className="asettings-container">
            <h1>Cześć {admin.name}</h1>
            <div className="asettings-row">
                <h3>Id: {admin.id}</h3>
            </div>
            <div className="asettings-row">
                <h3>Name: {admin.name}</h3>
                <ChangeName />
            </div>
            <div className="asettings-row">
                <h3>Email: {admin.email}</h3>
                <ChangeEmail />
            </div>
            <div className="asettings-row">
                <h3>Password: ******</h3>
                <ChangePassword />
            </div>
            <div className="asettings-row">
                <h3>Role: {admin.role}</h3>
            </div>
            <div className="asettings-row">
                <h3>created: {new Date(admin.created).toLocaleDateString("pl-PL")}</h3>
            </div>
        </div>
    )
}

export default AdminSettings