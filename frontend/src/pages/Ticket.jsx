import {useParams} from "react-router";
import {useState, useEffect} from "react";
import {jwtDecode} from "jwt-decode";
import "./Ticket.css"
import AddComment from "../components/AddComment.jsx";

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
            setTicket(data)
        }
        getTicket();
    }, []);

    return (

        <div className="ticket-container">
            <div className="ticket-header">
                <div>
                    <span className="ticket-label">Ticket #{ticket.id}</span>
                    <h1>{ticket.title}</h1>
                </div>
            </div>
            <div className="ticket-description">
                <h3>Opis zgłoszenia</h3>
                <p>{ticket.description}</p>
            </div>
            <div className="ticket-info">
                <span>Ostatnia aktualizacja
                    <strong>{new Date(ticket.updated). toLocaleDateString("pl-PL")}</strong>
                </span>
            </div>
            <div className="info-item">
                <span>Status
                <strong>{ticket.status}</strong> </span>
            </div>
            < AddComment />
        </div>
    )
}

export default Ticket