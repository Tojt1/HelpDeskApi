import {useState} from "react";

function ChangePassword() {
    const [open, setOpen] = useState(false)
    const [currentPassword, setCurrentPassword] = useState("")
    const [newPassword, setNewPassword] = useState("")

    const handleChangePassword = async (e) => {
        e.preventDefault()

        const token = localStorage.getItem("token")

        const response = await fetch("http://localhost:8000/me/password", {
            method: "Post",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${token}`
            },
            body: JSON.stringify({
                new_password: newPassword
            })
        })
    }

    return (
        <>
            <button onClick={() => setOpen(true)}>Zmień</button>
            <div className="model-background" onClick={() => setOpen(false)}></div>

            {open &&
            <div className="model" onClick={(e) => e.stopPropagation()}>
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
                <button></button>
            </div>
            }
        </>
    )
}

export default ChangePassword