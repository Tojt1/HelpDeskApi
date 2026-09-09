import {useState} from "react";
import {useParams} from "react-router";
import {jwtDecode} from "jwt-decode";

function DeleteTicket () {
    const [open, setOpen] = useState(false)

    return(
        <>
            <button className="deletet-btn" onClick={() => setOpen(true)}>Usuń</button>

            {open && (
                <>
                    <div className="deletet-background" onClick={() => setOpen(false)}></div>
                    <div className="deletet-container" onClick={(e) => e.stopPropagation()}>
                        <span>Czy na pewno chcesz usunąć swoje konto?Tej operacji nie można cofnąć.
                            Po usunięciu konta utracisz dostęp do swoich danych i zapisanych informacji.</span>
                        <div className="deletet-buttons">
                            <button className="delete-btn" onClick={handleDelete}>Tak</button>
                            <button className="cancel-btn" onClick={() => setOpen(false)}>Nie</button>
                        </div>
                    </div>
                </>
            )}
        </>
    )
}