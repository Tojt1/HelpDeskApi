import {useState} from "react";

function AdminDashboard (){
    const [tickets, setTickets] = useState([])

    return (
        <div className="adashboard-container">
            {tickets.map((ticket)=>(
                <div classname="aticket-card" key={ticket.id}>
                    <div className="aticket-items">
                        <h2>{ticket.title}</h2>

                        <p>{ticket.description}</p>
                        <span>Utworzono: {new Date(ticket.created).toLocaleDateString("pl-PL")}</span>
                        <span>Agent: {ticket.agent}</span>
                    </div>
                </div>
            ))}
        </div>
    )
}

export default AdminDashboard