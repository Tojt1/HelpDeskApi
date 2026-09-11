import {useNavigate, Outlet} from "react-router";
import {jwtDecode} from "jwt-decode";
import {useEffect} from "react";

function CheckLogged ( {children}) {
    const navigate = useNavigate()
    const token = localStorage.getItem("token")

    if (! token){
        navigate("/login")
    }
    const users = jwtDecode(token)

    const expiretime = users.exp * 1000
    const timeleft = expiretime - Date.now()

    useEffect(() => {
        if (timeleft<=0) {
            localStorage.removeItem("token")
            navigate("/login")
        }

        const timer = setTimeout(() => {
            localStorage.removeItem("token")
            navigate("/login")
        }, timeleft)

        return () => clearTimeout(timer)

    }, [timeleft, navigate]);


    return <Outlet />
}

export default CheckLogged