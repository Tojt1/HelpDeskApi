import {useState} from "react";
import {jwtDecode} from "jwt-decode";
import {useParams} from "react-router";

function DeleteComment ({ commentId }) {
    const [open, setOpen] = useState(false)
    const { ticket_id } = useParams()

    const HandleDelete = async (e) => {
        e.preventDefault()

        const token = localStorage.getItem("token")
        const user = jwtDecode(token)

        const response = await fetch(`http://localhost:8000/tickets/${user["id"]}/${ticket_id}/${commentId}`,
            {
                headers: {
                    "Authorization": `Bearer ${token}`
                }
            })
        if (response.ok){
            alert("Pomyślnie usunięto komentarz")
        }
    }

    return(
        <>
            <button className="deletec-open" onClick={() => setOpen(true)}></button>

            {open && (
                <>
                    <div className="deletec-background" onClick={() => setOpen(false)}></div>
                    <div className="deletec-container" onClick={(e) => e.stopPropagation()}>
                        <p>Czy jesteś pewien, że chcesz usunąć ten komentarz?</p>
                        <button className="delete-btn" onClick={HandleDelete}>Tak</button>
                        <button className="cancel-btn" onClick={() => setOpen(false)}>Nie</button>
                    </div>
                </>
            )}
        </>
    )
}

export default DeleteComment