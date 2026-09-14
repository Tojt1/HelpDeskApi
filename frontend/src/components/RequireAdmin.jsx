import {jwtDecode} from "jwt-decode";
import {Navigate, Outlet} from "react-router";

function RequireAdmin () {

    const token = localStorage.getItem("token")


    if (!token){
        return <Navigate to="/login" replace />
    }

    const user = jwtDecode(token)
    try {
        if (user.role !== "ADMIN") {
            return <Navigate to="/dashboard" replace/>
        }
        return <Outlet/>
    } catch {
        localStorage.removeItem("token")
        return <Navigate to="/login" replace />
    }
}

export default RequireAdmin