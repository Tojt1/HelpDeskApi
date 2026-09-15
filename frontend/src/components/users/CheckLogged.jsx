import {Navigate, Outlet} from "react-router";
import {jwtDecode} from "jwt-decode";
import {useEffect} from "react";


function CheckLogged () {
    const token = localStorage.getItem("token")

    if (! token){
        return <Navigate to="/login" replace />
    }

    let users = jwtDecode(token)

    const expiretime = users.exp * 1000
    const timeleft = expiretime - Date.now()

    useEffect(() => {
        if (timeleft<=0) {
            localStorage.removeItem("token")
            return;
        }

        const timer = setTimeout(() => {
            localStorage.removeItem("token")
            return <Navigate to="/login" />
        }, timeleft)

        return () => clearTimeout(timer)

    }, [timeleft]);


    return <Outlet />
}

export default CheckLogged