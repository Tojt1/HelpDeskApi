import {useState} from "react"
import "./ChangeEmail.css"

function ChangeEmail(){
    const [open, setOpen] = useState(false)
    const [currentEmail, setCurrentEmail] = useState("")
    const [newEmail, setNewEmail] = useState("")

    const handdleChangeEmail = async (e) => {
        e.preventDefault()

        const token = localStorage.getItem("token")
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

                    <button onClick={() => setOpen(true)}>Zmień</button>

                </div>

            </div>
            )}
        </>
    )
}

export default ChangeEmail