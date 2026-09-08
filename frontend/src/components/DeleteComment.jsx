import {useState} from "react";

function DeleteComment () {
    const [open, setOpen] = useState(false)

    const HandleDelete = async (e) => {
        e.preventDefault()
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