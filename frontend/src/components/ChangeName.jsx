import {useState} from "react";

function ChangeName() {
    const [open, setOpen] = useState(false)
    const [currentName, setCurrentName] = useState("")
    const [newName, setNewName] = useState("")

    const handleChange = async (e) => {
        e.preventDefault()

        if (!currentName.trim() || !newName.trim()){
            alert("Wszystkie pola muszą być zapełnione")
            return;
        }

        const token = localStorage.getItem("token")

        const response = await fetch("https://localhost:8000/me/name", {
            method: "PATCH",
            headers:{
                "Content-Type": "applcation/json",
                "Authorization": `Bearer ${token}`,
                body: JSON.stringify({
                    new_name: newName,
                    old_name: currentName
                })
            }
        })
    }

    return(
        <civ>
            <button className="name-open" onClick={() => setOpen(true)}>Zmień</button>
            {open &&(
                <div className="name-background" onClick={() => setOpen(false)}>
                    <div className="name-container" onClick={(e) => e.preventDefault()}>
                        <form className="name-form">
                            <h2>ZMiana imienia</h2>
                            <p>Obecny nick:</p>
                            <input
                                type="text"
                                placeholder="Twoje obecny nick ..."
                                value={currentName}
                                onChange={(e)=> setCurrentName(e.target.value)}
                            />
                            <p>nowy nick:</p>
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

export default ChangeName