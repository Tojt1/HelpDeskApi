import {useEffect, useState} from "react";

function AdminDashboard (){
    const [tickets, setTickets] = useState([])

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
                setTickets(data)
            }
        }
        getData();
    }, []);


    return (
        <div className="adashboard-container">
            {tickets.map((ticket)=>(
                <div className="aticket-card" key={ticket.id}>
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