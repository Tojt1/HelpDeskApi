import {Navigate, Outlet} from "react-router";

function CheckLogged ( {children}) {
    const token = localStorage.getItem("token")
    if (! token){
        return <Navigate to="/login"/>
    }
    return <Outlet />
}

export default CheckLogged