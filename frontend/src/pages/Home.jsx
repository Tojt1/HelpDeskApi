import { useState } from "react";
import { Link } from "react-router";
import "./Home.css"
import {useNavigate} from "react-router";



function Home() {

    const navigate = useNavigate();

    const [problemTitle, setProblemTitle] = useState("");
    const [problemDescription, setProblemDescription] = useState("");
    const [problemCategory, setProblemCategory] = useState("")


    const handleSubmit = async (e) => {
        e.preventDefault()
        const items = localStorage.getItem("token")

        if(!items){
            alert("nie ma tokenu")
            navigate("/login");
            return;
        }
        const token = localStorage.getItem("token")

        const response = await fetch("http://localhost:8000/tickets", {
            method: "POST",
            headers: {
                "Content-Type":"application/json",
                "Authorization": `Bearer ${token}`
            },
            body:JSON.stringify({
                title: problemTitle,
                description: problemDescription,
                category: problemCategory
            })
        })
        const data = await  response.json()

        console.log("status", response.status)
        console.log("data", data)
}

    return <div className="home-container">
        <h2>Witaj, jaki jest twój problem?</h2>

        <form onSubmit={handleSubmit} className="home-form">
            <p>Jakigo rodzaju jest twój problem?</p>
            <input
            type="text"
            placeholder="....."
            value={problemTitle}
            onChange={(e) => setProblemTitle((e.target.value))}/>


            <p className="paragraph-description">Opisz swój problem</p>
            <input
            type="text"
            placeholder="...."
            value={problemDescription}
            onChange={(e) => setProblemDescription(e.target.value)}/>

            <p>Z jakiej kategori jest twój błą∂: </p>
            <input
            type="text"
            placeholder="Category...."
            value={problemCategory}
            onChange={(e) => setProblemCategory(e.target.value)}/>

            <button className="home-btn" type="submit">Wyślij token</button>
        </form>
        <Link to="/login" className="link-login">Zaloguj się</Link>
        <Link to="/register" className="link-register">zarejestruj się</Link>
    </div>
}

export default Home