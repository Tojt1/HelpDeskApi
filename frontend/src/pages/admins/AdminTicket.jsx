import {useState, useEffect} from "react";
import {jwtDecode} from "jwt-decode";
import {useParams} from "react-router";
import "./AdminTicket.css"
import AdminAsign from "../../components/AdminAsign.jsx";

function AdminTicket (){
    const [showButton, setShowButton] = useState(false)
    const [ticket, setTicket] = useState([])
    const [comments, setComments] = useState([])
    const [commentMessage, setCommentMessage] = useState("")
    const token = localStorage.getItem("token")
    let user = jwtDecode(token)
    let { ticket_id } = useParams()

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

    useEffect(() => {
         const getComments = async() => {
            const response = await fetch(`http://localhost:8000/tickets/${user["id"]}/${ticket_id}/comments`, {
                headers:{
                    "Authorization":`Bearer ${token}`
                }
            })
            const data = await response.json()
             if (data.length ==0){
                 setCommentMessage("Nie ma tutaj jeszcze komentarzy")
             }
            setComments(data)
        }
        getTicket()

        getComments()
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
            <div className="acomments">
                {comments.map((comment) => (
                    <div className="acomment-card" key={comment.id}>
                        <span>{comment.author_name}</span>

                        <span>{new Date(comment.created).toLocaleDateString("pl-PL")}</span>

                        <p>{comment.content}</p>
                    </div>
                ))}
            </div>
            <p className="acomment-none">{commentMessage}</p>
            {showButton &&(
                <div className="aticket-btns">
                    <AdminAsign when_clicked={getTicket} />
                </div>
            )}
        </div>
    )
}

export default AdminTicket