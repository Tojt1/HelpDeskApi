import {Navigate} from "react-router";

function CheckLogged ( {children}) {
    const token = localStorage.getItem("token")
    if (! token){
        return <Navigate to="/login"/>
    }
    return children
}

export default CheckLogged