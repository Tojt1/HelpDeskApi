import {useState, useEffect, use} from "react";
import {jwtDecode} from "jwt-decode";


function Tickets(){

    useEffect(() => {
        const token = localStorage.getItem("token")
        const users = jwtDecode(token)
        const [tickets, setTickets] = useState([])

        const getData = async () => {
            const response = await fetch(`http://localhost:8000/tickets/${users["id"]}}`, {
                headers: {
                    "Authorization": `Bearer ${token}`
                }
            })
            const data = response.json()
            setTickets(data)
        }
        getData();
    }, []);

    return (
        <div className="ticket-container">
            <h1>Moje tickety</h1>
            <div className="tickets-list">
                {tickets.map((ticket) => (
                    <div className="ticket-card"
                    key={ticket.id}
                    onClick={() => console.log("Kliknięto", ticket.id)}>
                        <div className="ticket-items">
                            <h2>{ticket.title}</h2>

                            <p>{ticket.description}</p>
                            <spn>Utworzono: {" "} {new Date(ticket.created).toLocaleDateString("pl-PL")}</spn>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default Tickets