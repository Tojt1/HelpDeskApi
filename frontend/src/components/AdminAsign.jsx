import {useParams} from "react-router";

function AdminAsign ({when_clicked}){
    const token = localStorage.getItem("token")
    const { ticket_id } = useParams()
    const handleAssign = async (e) =>{
        e.preventDefault()
        const response = await fetch(`http://localhost:8000/admin/${ticket_id}/assign`, {
            headers:{
                "Authorization":`Bearer ${token}`
            }
        })
        if (response.ok){
            alert("pomyślnie przypisano agenta")
            when_clicked()
        }
    }
    return (
        <button className="assign-btn" onClick={handleAssign}>Przypisz mnie</button>
    )
}

export default AdminAsign