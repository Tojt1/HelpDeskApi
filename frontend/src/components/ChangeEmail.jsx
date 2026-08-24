import {useState} from "react"
import "./ChangeEmail.css"

function ChangeEmail(){
    const [open, setOpen] = useState(false)


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
                    <button onClick={() => setOpen(true)}>Zmień</button>

                    <h2>Hello</h2>
                </div>

            </div>
            )}
        </>
    )
}

export default ChangeEmail