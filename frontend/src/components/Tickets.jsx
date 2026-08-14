
function ShowTickets({ticket}){
    function AssignTo(){
        alert("clicked")
    }
    return (
        <div className="tickets">
            <div className="ticket-info">
                <h3>{ticket.title}</h3>
                <p>{ticket.created}</p>
            </div>
            <div className="ticket-overlay">
                <button className="assign-btn" onClick={AssignTo}>Przypisz</button>
            </div>
        </div>
    )
}

export default  ShowTickets