import Usermenu from "./Usermenu.jsx";
import CreateTicketButton from "./CreateTicketButton.jsx";
import {Outlet} from "react-router";

function UserLayout () {
    return(
        <>
            <Usermenu />
            <CreateTicketButton />

            <Outlet />
        </>
    )
}
export default UserLayout