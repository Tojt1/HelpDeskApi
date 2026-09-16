
function AdminAsign (){
    const token = localStorage.getItem("token")
    const handleAssign = async (e) =>{
        e.preventDefault()
        const response = await fetch("http://localhost:8000/admin/assign", {
            headers:{
                "Authorization":`Bearer ${token}`
            }
        })
        if (response.ok){
            const data = response.json()
        }
    }
    return (
        <button className="assign-btn">Przypisz mnie</button>
    )
}

export default AdminAsign