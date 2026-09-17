import {Outlet} from "react-router";
import Adminmenu from "./Adminmenu.jsx";

function AdminLayout (){

    return (
        <>
            <Adminmenu />

            <Outlet />
        </>
    )
}

export default AdminLayout