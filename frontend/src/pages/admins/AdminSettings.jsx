import {useState, useEffect} from "react";

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
            <h3>Id: {admin.id}</h3>
            <h3>Name: {admin.name}</h3>
            <h3>Email: {admin.email}</h3>
            <h3>Password: ******</h3>
            <h3>Role: {admin.role}</h3>
            <h3>created: {new Date(admin.created).toLocaleDateString("pl-PL")}</h3>
        </div>
    )
}

export default AdminSettings