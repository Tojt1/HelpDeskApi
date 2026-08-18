import {useState} from "react";
import {useNavigate} from "react-router";
import {Link} from "react-router";
import "./register.css";


function RegisterUser (){
    const navigate = useNavigate()

    const [name, setName] = useState("")
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const [registerError, setRegisterError] = useState("")

    const handleRegister = async (e) => {
        e.preventDefault()

        setRegisterError("")

        try {
            const response = await fetch("http://localhost:8000/register", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    name, email, password
                })

            });
            const data = await response.json();
            if (response.ok) {
                alert("Pomyślnie utworzono konto")
                navigate("/login")
            } else{
                setRegisterError(data.detail)
            }


        }
        catch(error){
            setRegisterError(error)
        }
    }


    return(
        <div className="register-container">
            <form onSubmit={handleRegister} className="register-form">
                <p>Name:</p>
                <input
                type="text"
                placeholder="Name: "
                value={name}
                onChange={(e) => setName(e.target.value)}/>

                <p>Email:</p>
                <input
                type="email"
                placeholder=".....@djn.dnj"
                value={email}
                onChange={(e) => setEmail(e.target.value)}/>

                <p>Password:</p>
                <input
                type="password"
                placeholder="******"
                value={password}
                onChange={(e) => setPassword(e.target.value)}/>

                <button className="register-btn" type="submit"> Zarejestruj sięx</button>
            </form>
            {registerError &&(
                <div>
                    <p>Wystąpił błąd podczas rejestracji: {registerError}</p>
                </div>
            )}
            <Link to="/login" className="link-login">Zaloguj się</Link>
        </div>
    )
}

export default RegisterUser