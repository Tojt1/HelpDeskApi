import {useNavigate} from "react-router";
import {useState} from "react";
import "./Adminmenu.css"

function Adminmenu (){
    const [open, setOpen] = useState(false)
    const navigate = useNavigate()

    const handleLogout = () => {
        localStorage.removeItem("token")
        navigate("/")
    }

    return(
        <>
            <div className="amenu-container">
                <button className="aopen-menu" onClick={()=> setOpen(!open)}>👤</button>
                {open &&(
                    <div className="amenu-options">
                        <button className="amenu-tickets" onClick={()=> navigate("/admin/dashboard")}>✉️Ticket</button>
                        <button className="amenu-settings" onClick={()=> navigate("/admin/settings")}>⚙️ Ustawienia</button>
                        <button className="amenu-logout" onClick={handleLogout}>❌ Wyloguj się</button>
                    </div>
                )}
            </div>
        </>
    )
}

export default Adminmenu