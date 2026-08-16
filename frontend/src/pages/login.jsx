import {useState} from "react";
import "./login.css"
import {useNavigate} from "react-router";

function Login(){
    const navigate = useNavigate();

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [loginInfo, setLoginInfo] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault()

        const response = await fetch("http://localhost:8000/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                email, password
            })
        });

        const data = await response.json();
        localStorage.setItem("token", data.token)

        alert("Pomyślnie zalogowano")
        navigate("/")
    }

    return(
        <div className="login-container">
            <h2>Logowanie</h2>
            <form onSubmit={handleSubmit} className="login-from">
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
            {loginInfo && (
                <div>
                    <p>Pomyślnie zalogowano jako: {loginInfo.email}</p>
                </div>
            )}
        </div>
    )
}

export default Login