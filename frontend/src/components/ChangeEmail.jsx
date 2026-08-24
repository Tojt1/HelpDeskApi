import {useState} from "react"
import "./ChangeEmail.css"

function ChangeEmail(){
    const [open, setOpen] = useState(false)


    return (
        <div className="model-bacground"
             onClick={() => setOpen(false)}
        >
            <div className="model"
                 onClick={(e) => e.stopPropagation()}
            >
                <button onClick={() => setOpen(true)}>Zmień</button>

                {open && (
                    <div>
                        <h2>change email</h2>
                    </div>
                )}
            </div>
        </div>
    )
}

export default ChangeEmail