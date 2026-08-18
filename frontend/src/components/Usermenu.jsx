import {useState} from "react";
import {useNavigate} from "react-router";

function Usermenu(){
    const navigate = useNavigate()
    const [open, setOpen] = useState(false)

    const handleLogout = () => {
        localStorage.removeItem("token")
        navigate("/")
    }

    return (
        <div className="user-container">
            <button onClick={() => setOpen(!open)}>👤</button>

            {open && (
                <div className="dropdown">
                    <button onClick={() => navigate("/tickets")}>Tickets</button>
                    <button onClick={() => navigate("/settings")}>Settings</button>
                    <button onClick={handleLogout}>wyloguj</button>
                </div>
            )}
        </div>
    )
}

export default Usermenu