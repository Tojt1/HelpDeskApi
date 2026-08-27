import {useState} from "react";
import "./ChangePassword.css"

function ChangePassword() {
    const [open, setOpen] = useState(false)
    const [currentPassword, setCurrentPassword] = useState("")
    const [newPassword, setNewPassword] = useState("")

    const handleChangePassword = async (e) => {
        e.preventDefault()

        const token = localStorage.getItem("token")

        const response = await fetch("http://localhost:8000/me/password", {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${token}`
            },
            body: JSON.stringify({
                new_password: newPassword,
                old_password: currentPassword
            })
        })
        const data = response.json()
        console.log("t")
    }

    return (
        <>
            <button onClick={() => setOpen(true)}>Zmień</button>


            {open && (
                <div className="model-background" onClick={() => setOpen(false)}>
                    <div className="model" onClick={(e) => e.stopPropagation()}>
                        <h2>Zmień hasło</h2>
                        <p>Obecne hasło: </p>
                        <input
                        type="text"
                        placeholder="Current password..."
                        value={currentPassword}
                        onChange={(e) => setCurrentPassword(e.target.value)}/>
                        <p>Nowe hasło: </p>
                        <input
                        type="text"
                        placeholder="New password..."
                        value={newPassword}
                        onChange={(e) => setNewPassword(e.target.value)}/>
                        <button onClick={handleChangePassword}>Zmień</button>
                    </div>
                </div>
            )}
        </>
    )
}

export default ChangePassword