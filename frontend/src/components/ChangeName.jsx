import {useState} from "react";

function ChangeName() {
    const [open, setOpen] = useState(false)
    const [currentName, setCurrentName] = useState("")
    const [newName, setNewName] = useState("")


    return(
        <civ>
            <button className="name-open" onClick={() => setOpen(true)}>Zmień</button>
            {open &&(
                <div className="name-background" onClick={() => setOpen(false)}>
                    <div className="name-container" onClick={(e) => e.preventDefault()}>
                        <form className="name-form">
                            <input
                                type="text"
                                placeholder="Twoje obecny nick ..."
                                value={currentName}
                                onChange={(e)=> setCurrentName(e.target.value)}
                            />
                            <input
                            type="text"
                            placeholder="Nowey nick ...."
                            value={newName}
                            onChange={(e) => setNewName(e.target.value)}/>

                            <button type="submit">Zmień</button>
                        </form>
                    </div>
                </div>
            )
            }
        </civ>
    )
}