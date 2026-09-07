import {useState} from "react";
import "./ChangeName.css"

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
        <>
            <button className="name-open" onClick={() => setOpen(true)}>Zmień</button>
            {open &&(
                <>
                    <div className="name-background" onClick={() => setOpen(false)}> </div>
                        <div className="name-container" onClick={(e) => e.stopPropagation()}>
                            <form className="name-form" onSubmit={handleChange}>
                                <h2>Zmiana imienia</h2>
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

                                <button type="submit" className="name-submit">Zmień</button>
                            </form>
                        </div>
                </>
            )
            }
        </>
    )
}

export default ChangeName