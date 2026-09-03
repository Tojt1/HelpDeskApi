import {useState} from "react"
import "./ChangeEmail.css"

function ChangeEmail(){
    const [open, setOpen] = useState(false)
    const [currentEmail, setCurrentEmail] = useState("")
    const [newEmail, setNewEmail] = useState("")
    const [error, setError] = useState(null)

    const handdleChangeEmail = async (e) => {
        e.preventDefault()

        if (!currentEmail.trim() || !newEmail.trim()){
            alert("Wszystkie pola muszą być wypełnione")
            return;
        }

        setError(null)

        const token = localStorage.getItem("token")

        const response = await fetch("http://localhost:8000/me/email", {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json",
                "Authorization":`Bearer ${token}`
            },
            body: JSON.stringify({
                old_email: currentEmail,
                new_email: newEmail
            })
        })
        const data = response.json()
        console.log(data)
        if (response.ok){
            alert("Pomyślnie zmieniono email")
        }
        else{
            setError(data.detail)
        }
    }


    return (
        <>
            <button onClick={() => setOpen(true)}>Zmień</button>

            {open && (
            <div className="modal-background "
                 onClick={() => setOpen(false)}
            >
                <div className="modal"
                     onClick={(e) => e.stopPropagation()}
                >
                    <h2>Zmień email:</h2>

                    <p>Obecny email::</p>
                    <input
                    type="text"
                    placeholder="Current email.... "
                    value={currentEmail}
                    onChange={(e) => setCurrentEmail(e.target.value)}/>

                    <p>nowy email:</p>
                    <input
                    type="text"
                    placeholder="new email.... "
                    value={newEmail}
                    onChange={(e) => setNewEmail(e.target.value)}/>

                    <button onClick={handdleChangeEmail}>Zmień</button>

                    {error &&(
                        <div className="show-error">
                            <p>Wystąpił błąd podczas zmieniania emailu: {error} </p>
                        </div>
                    )}
                </div>

            </div>
            )}
        </>
    )
}

export default ChangeEmail