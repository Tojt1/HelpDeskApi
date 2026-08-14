import {useState} from "react";

function Login(){
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault()
        alert(email)
    }

    return(
        <div className="login-container">
            <form onSubmit={handleSubmit} className="login-from">
                <h2>Logowanie</h2>
                <input
                type="email"
                placeholder="Email:"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                />
                <input
                type="password"
                placeholder="Password: "
                value={password}
                onChange={(e) => setPassword(e.target.value)}/>
                <button type="submit" className="signin-button">Zaloguj się</button>
            </form>
        </div>
    )
}

export default Login