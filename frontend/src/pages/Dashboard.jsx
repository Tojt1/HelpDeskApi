import {jwtDecode} from "jwt-decode";
import {useState} from "react";
import Tickets from "../components/Tickets.jsx";
import "./Dashboard.css"

function Dashboard(){


    return(
        <>
            <Tickets />
        </>
    )
}

export default Dashboard