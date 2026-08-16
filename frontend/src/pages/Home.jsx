import { useState } from "react";
import { Link } from "react-router";
import "./Home.css"
import {useNavigate} from "react-router";



function Home() {

    const navigate = useNavigate();

    const [problemTitle, setProblemTitle] = useState("");
    const [problemDescription, setProblemDescription] = useState("");


    const handleSubmit = async (e) => {
        e.preventDefault()
        const items = localStorage.getItem("token")

        if(!items){
            alert("nie ma tokenu")
            navigate("/login");
            return;
        }
        alert("utworzono token")
        /// tutaj wyślij token
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

            <button className="home-btn" type="submit">Wyślij token</button>
        </form>
        <Link to="/login" className="link-login">Zaloguj się</Link>
        <Link to="/register" className="link-register">zarejestruj się</Link>
    </div>
}

export default Home