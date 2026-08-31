import {useParams} from "react-router";

function Ticket (){
    const { ticket_id } = useParams()

    console.log(ticket_id)

    return (
        <>
            <h1>Hello</h1>
        </>
    )
}

export default Ticket