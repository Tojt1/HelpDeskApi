import {useEffect} from "react";

function Settings (){
    useEffect(()=> {
        const token = localStorage.getItem("token")

        const getData = async () => {
            const respose = await fetch("http://localhost:8000/me", {
                headers:{
                    "Authorization":`Bearer ${token}`
                }
            })

            const data = respose.json()
            console.log(data)
        }
        getData();
    }
    , [])
}

export default Settings