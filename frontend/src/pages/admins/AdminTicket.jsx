import {useState} from "react";

function AdminTicket (){
    const [ticket, setTicket] = useState([])

    return(
        <div className="aticket-container">
            <div className="aticket-header">
                <h2>{ticket.title}</h2>
                <span className="aticket-id">Ticket #{ticket.id}</span>
            </div>
            <div className="aticket-description">
                <h3>Opis sgłoszenia</h3>
                <p>{ticket.description}</p>
            </div>
            <div className="aticket-information">
                <span>Ostatnia aktualizacja: <stron>{new Date(ticket.updated).toLocaleDateString("pl-PL")}</stron></span>
                <p>Status: {ticket.status}</p>
            </div>
        </div>
    )
}

export default AdminTicket