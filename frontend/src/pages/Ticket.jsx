import {useParams} from "react-router";
import {useState, useEffect, use} from "react";
import {jwtDecode} from "jwt-decode";

function Ticket (){
    const { ticket_id } = useParams()
    const [ticket, setTicket] = useState([])

    useEffect(() => {
        const token = localStorage.getItem("token")
        const users = jwtDecode(token)
        const getTicket = async () => {
            const respone = await fetch(`http://localhost:8000/tickets/${users["id"]}/${ticket_id}`, {
                headers: {
                    "Authorization": `Bearer ${token}`
                }
            })
            const data = await respone.json()
            console.log(data)
            setTicket(data)
        }
        getTicket();
    }, []);

    return (
        <>
            <h1>{ticket.id}</h1>
        </>
    )
}

export default Ticket