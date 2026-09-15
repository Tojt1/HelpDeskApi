import {useState, useEffect} from "react";
import {jwtDecode} from "jwt-decode";
import {useParams} from "react-router";

function AdminTicket (){
    const [showButton, setShowButton] = useState(false)
    const [ticket, setTicket] = useState([])
    const token = localStorage.getItem("token")
    let user = jwtDecode(token)
    let { ticket_id } = useParams()

    useEffect(() => {
        const getTicket = async () =>{
             const response = await fetch(`http://localhost:8000/tickets/${user["id"]}/${ticket_id}`, {
                headers:{
                    "Authorization":`Bearer ${token}`
                }
            })
            const data = await response.json()
            if (data.agent_id == null){
                setShowButton(true)
            }
            setTicket(data)
        }
        getTicket()
    }, []);

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
                <span>Ostatnia aktualizacja: <strong>{new Date(ticket.updated).toLocaleDateString("pl-PL")}</strong></span>
                <p>Status: {ticket.status}</p>
            </div>
            {showButton &&(
                <div className="aticket-btns">
                    <button>Przypisz mnie</button>
                </div>
            )}
        </div>
    )
}

export default AdminTicket