import {jwtDecode} from "jwt-decode";
import {useState} from "react";

function CreateToken() {
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
                "Authorisation": `Bearer ${token}`
            },
            body:JSON.stringify({
                title: problemTitle,
                description: problemDescription,
                category: problemCategory
            })
        })
        if (response.ok){
            alert("Pomyślnie utworzono ticket")
        }
    }


    return(
    <div className="dasboard-container">

        <h2>Hello {users.name}</h2>

        <form onSubmit={SubmitDash} className="dashboard-form">

            <p>Jakiego rodzaju jest twój problem?</p>
            <input
                type="text"
                placeholder="....."
                value={problemTitle}
                onChange={(e) => setProblemTitle(e.target.value)}/>

            <p>Opisz swój problem</p>
            <input
                type="text"
                placeholder="....."
                value={problemDescription}
                onChange={(e) => setProblemDescription(e.target.value)}/>

            <p>Z jakiej kategori jest twój problem</p>
            <input
                type="text"
                placeholder="Category...."
                value={problemCategory}
                onChange={(e) => setProblemCategory(e.target.value)}/>

            <button type="submit" className="dashboard-btn">Wyślij ticket</button>
        </form>
    </div>
    )
}

export default CreateToken