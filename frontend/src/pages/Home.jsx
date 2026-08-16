import { useState } from "react";
import { Link } from "react-router";
import "./Home.css"

const handleSubmit = () => {
    alert("wyslanoo")
}

function Home() {
    const [problemTitle, setProblemTitle] = useState("")
    const [problemDescription, setProblemDescription] = useState("")

    return <div className="home-container">
        <h2>Witaj, jaki jest twój problem?</h2>

        <form onSubmit={handleSubmit} className="home-form">
            <p>Jakigo rodzaju jest twój problem?</p>
            <input
            type="text"
            placeholder="....."
            value={problemTitle}
            onChange={(e) => setProblemTitle((e.target.value))}/>


            <p>Opisz swój problem</p>
            <input
            type="text"
            placeholder="...."
            value={problemDescription}
            onChange={(e) => setProblemDescription(e.target.value)}/>

        </form>
        <Link to="/login" className="link-login">Zaloguj się</Link>
    </div>
}

export default Home