import {useState} from "react";
import {jwtDecode} from "jwt-decode";
import {useParams} from "react-router";
import "./AddComment.css"

function AddComment (){
    const [open, setOpen] = useState(false)
    const [content, setContent] = useState(false)

    const handleComment = async (e) => {
        e.preventDefault()

        const token = localStorage.getItem("token")
        const user = jwtDecode(token)
        const {ticket_id} = useParams()

        const response = await fetch(`http://localhost8000/tickets/${user["id"]}/${ticket_id}/comments`, {
            method: "POST",
            headers:{
                "Content-type": "application/json",
                "Authorization": `Bearer ${token}`
            },
            body: JSON.stringify(
                content
            )
        })
        if (response.ok){
            alert("Pomyślnie dodano komentarz")
            setOpen(false)
        }
        else{
            const data = response.json()
            console.log(data)
        }
    }

    return (
        <>
            <button className="comment-open" onClick={() => setOpen(true)}>Dodaj komentarz</button>

            {open &&
            <div className="comment-background" onClick={() => setOpen(false)}>
                <div className="comment-container" onClick={(e) => e.stopPropagation()}>
                    <form className="comment-form">
                        <h2>Dodaj komentarz: </h2>
                        <textarea
                            placeholder="Napisz tu coś: ...."
                            value={content}
                            onChange={(e) => setContent(e.target.value)}
                        />
                        <button className="comment-btn" onClick={handleComment}>Dodaj</button>
                    </form>
                </div>
            </div>
            }
        </>
    )
}

export default AddComment