import {useEffect, useState} from "react";
import {useNavigate, Link} from "react-router";
import {jwtDecode} from "jwt-decode";
import "./login.css"

function Login(){
    const navigate = useNavigate();

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [loginError, setLoginError] = useState("")

    useEffect(() => {
        if (localStorage.getItem("token")){
            let user = jwtDecode(localStorage.getItem("token"))
            if (user.role == "ADMIN"){
                navigate("/admin/dashboard")
            } else{
                navigate("/dashboard")
            }
        }
    }, []);

    const handleSubmit = async (e) => {
        e.preventDefault()

        setLoginError("")

        try{
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

            if (!response.ok){
                setLoginError(data.detail || "Niepoprawny email lub hasło")
            }
            else {
                localStorage.setItem("token", data.token)
                let user = jwtDecode(data.token)
                if (user.role == "ADMIN"){
                    navigate("/admin/dashboard")
                }
                else{
                    navigate("/dashboard")
                }
                }
        }
        catch (error){
            setLoginError("Nieudało się połączyć z serwerem")
        }
    }

    return(
        <div className="login-container">
            <h2>Logowanie</h2>
            <form onSubmit={handleSubmit} className="login-form">
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

            <Link to="/register" className="link-register">Zarejestruj się</Link>

            {loginError && (
                <div className="login-error">
                    <p>Wystąpił błąd podczas logowania: {loginError}</p>
                </div>
            )}
        </div>
    )
}

export default Login