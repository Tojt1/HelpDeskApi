import {useEffect, useState} from "react";
import {useNavigate} from "react-router";
import "./AdminDashboard.css"

function AdminDashboard (){
    const [tickets, setTickets] = useState([])
    const navigate = useNavigate()

    useEffect( () => {
        const token = localStorage.getItem("token")

        const getData = async () => {
            const response = await fetch("http://localhost:8000/admin/tickets", {
                headers: {
                    "Authorization":`Bearer ${token}`
                }
            })
            if (response.ok){
                const data = await response.json()
                console.log(data)
                setTickets(data)
            }
        }
        getData();
    }, []);


    return (
        <div className="adashboard-container">
            {tickets.map((ticket)=>(
                <div className="aticket-card" key={ticket.id} onClick={()=> navigate(`/admin/${ticket.id}`)}>
                    <div className="aticket-items">
                        <h2>{ticket.title}</h2>

                        <p>{ticket.description}</p>
                        <div className="aticket-date">
                            <span>Utworzono: {new Date(ticket.created).toLocaleDateString("pl-PL")}</span>
                        </div>
                        <div className="aticket-info">
                            <span>Agent: {ticket.agent_id}</span>
                             <span className={`aticket-status ${ticket.status.toLowerCase()}`}>
                                 {ticket.status}
                             </span>
                         </div>
                    </div>
                </div>
            ))}
        </div>
    )
}

export default AdminDashboard