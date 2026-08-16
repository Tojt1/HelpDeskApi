import {useState} from "react";
import {useNavigate} from "react-router";


function RegisterUser (){
    const navigate = useNavigate()

    const [name, setName] = useState("")
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")

    const handleRegister = async (e) => {
        e.preventDefault()

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
            alert("Pomyślnie utworzono konto")

            navigate("/login")
        } catch(error){
            console.log(error)
        }
    }


    return(
        <div>
            <form onSubmit={handleRegister} className="register-container">
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
        </div>
    )
}

export default RegisterUser