import {jwtDecode} from "jwt-decode";
import {useNavigate} from "react-router";

function RequireAdmin () {
    const navigate = useNavigate()

    const token = localStorage.getItem("token")

    if (!token){
        navigate("/login")
    }

}