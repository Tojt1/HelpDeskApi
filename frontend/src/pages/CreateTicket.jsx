import {jwtDecode} from "jwt-decode";
import {useState} from "react";
import {useNavigate} from "react-router";
import "./CreateTicket.css"

function CreateTicket() {
    const navigate = useNavigate()
    const token = localStorage.getItem("token");
    const users = jwtDecode(token);
    const [problemTitle, setProblemTitle] = useState("")
    const [problemDescription, setProblemDescription] = useState("")
    const [problemCategory, setProblemCategory] = useState("")


    const SubmitDash = async (e) => {
        e.preventDefault()

        const token = localStorage.getItem("token")

        const response = await fetch("http://localhost:8000/tickets", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${token}`
            },
            body:JSON.stringify({
                title: problemTitle,
                description: problemDescription,
                category: problemCategory
            })
        })
        if (response.ok){
            alert("Pomyślnie utworzono ticket")
            navigate("/dashboard")
        }
    }


    return(
    <div className="create-container">

        <h2>Hello {users.name}</h2>

        <form onSubmit={SubmitDash} className="create-form">

            <div className="form-group">
                <p>Jakiego rodzaju jest twój problem?</p>
                <input
                    type="text"
                    placeholder="Jakiego rodzaju jest twój prboelm?"
                    value={problemTitle}
                    onChange={(e) => setProblemTitle(e.target.value)}/>
            </div>

            <div className="form-group">
                <p>Opisz swój problem</p>
                <textarea
                    placeholder="Opisz dokładnie na czym poelga twój problem?"
                    value={problemDescription}
                    onChange={(e) => setProblemDescription(e.target.value)}/>
            </div>

            <div className="form-group">
                <p>Z jakiej kategori jest twój problem</p>
                <input
                    type="text"
                    placeholder="Kategoria...."
                    value={problemCategory}
                    onChange={(e) => setProblemCategory(e.target.value)}/>
            </div>

            <button type="submit" className="create-btn">Wyślij ticket</button>
        </form>
    </div>
    )
}

export default CreateTicket