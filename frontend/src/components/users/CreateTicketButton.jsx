import {useNavigate} from "react-router";
import "./CreateTicketButton.css"

function CreateTicketButton(){
    const navigate = useNavigate()

    return (
        <>
            <button onClick={() => navigate("/createTicket")} className="ticket-button">+</button>
        </>
    )
}

export default CreateTicketButton