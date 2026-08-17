import {jwtDecode} from "jwt-decode";

function Dashboard(){
    const token = localStorage.getItem("token");
    const users = jwtDecode(token);

    return(
        <div>
            <h2>Hello {users.name}</h2>
        </div>
    )
}

export default Dashboard