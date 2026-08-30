import {jwtDecode} from "jwt-decode";
import {useState} from "react";
import Tickets from "../components/Tickets.jsx";
import "./Dashboard.css"

function Dashboard(){
    const token = localStorage.getItem("token");
    const users = jwtDecode(token);
    const [problemTitle, setProblemTitle] = useState("")
    const [problemDescription, setProblemDescription] = useState("")
    const [problemCategory, setProblemCategory] = useState("")


    const SubmitDash = async (e) => {
        e.preventDefault()

        const token = localStorage.getItem("token")

        const response = await fetch("http://localhost:8000/tickets", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorisation": `Bearer ${token}`
            },
            body:JSON.stringify({
                title: problemTitle,
                description: problemDescription,
                category: problemCategory
            })
        })
        const data = response.json()
    }

    return(
        <>
            <Tickets />
        </>
    )
}

export default Dashboard