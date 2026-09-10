import {useState} from "react";
import {useParams} from "react-router";
import {jwtDecode} from "jwt-decode";
import "./DeleteTicket.css"

function DeleteTicket () {
    const [open, setOpen] = useState(false)

    const handleDelete = async (e) => {
        e.preventDefault()
    }

    const handleOpen = (e) => {
        e.stopPropagation()



        setOpen(true)
    }

    return(
        <>
            <button className="deletet-btn" onClick={handleOpen}>Usuń</button>

            {open && (
                    <div className="deletet-container" onClick={(e) => e.stopPropagation()}>
                        <span>Czy na pewno chcesz usunąć ten ticket?Tej operacji nie można cofnąć.
                            Po usunięciu tkcketu nie będzie można już tego cofnąć.</span>
                        <div className="deletet-buttons">
                            <button className="delete-btn" onClick={handleDelete}>Tak</button>
                            <button className="cancel-btn" onClick={() => setOpen(false)}>Nie</button>
                        </div>
                    </div>
            )}
        </>
    )
}

export default DeleteTicket