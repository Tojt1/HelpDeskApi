import {useState} from "react";
import {useNavigate} from "react-router";
import "./DeleteAccount.css"

function DeleteAccount (){
    const [open, setOpen] = useState(false)
    const navigate = useNavigate()

    const handleDelete = async (e) => {
        e.preventDefault()

        const token = localStorage.getItem("token")

        const response = await fetch("http://localhost:8000/me/delete", {
            method: "DELETE",
            headers:{
                "Authorization": `Bearer ${token}`
            }
        })
        if (response.ok){
            alert("Pomyślnie usunięto konto")
            localStorage.removeItem("token")
            navigate("/")
        }
    }

    return(
        <>
            <button className="deletea-open" onClick={() => setOpen(true)}>Usuń konto</button>
            {open && (
                <>
                    <div className="deletea-bacground" onClick={()=> setOpen(false)}></div>
                    <div className="deletea-container" onClick={(e) => e.stopPropagation()}>
                        <span>Czy na pewno chcesz usunąć swoje konto?Tej operacji nie można cofnąć.
                            Po usunięciu konta utracisz dostęp do swoich danych i zapisanych informacji.</span>
                        <div className="deletea-buttons">
                            <button className="delete-btn" onClick={handleDelete}>Tak</button>
                            <button className="cancel-btn" onClick={() => setOpen(false)}>Nie</button>
                        </div>
                    </div>
                </>
            )}
        </>
    )
}

export default DeleteAccount