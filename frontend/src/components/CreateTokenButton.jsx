import {useNavigate} from "react-router";
import "./CreateTokenButton.css"

function CreateTokenButton(){
    const navigate = useNavigate()

    return (
        <>
            <button onClick={() => navigate("/createToken")} className="ticket-button">+</button>
        </>
    )
}

export default CreateTokenButton