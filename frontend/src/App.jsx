import './App.css'
import Login from "./pages/commons/login.jsx";
import Home from "./pages/users/Home.jsx";
import RegisterUser from "./pages/users/register.jsx";
import Dashboard from "./pages/users/Dashboard.jsx";
import CheckLogged from "./components/users/CheckLogged.jsx";
import Settings from "./pages/commons/Settings.jsx";
import { Routes, Route} from "react-router";
import Usermenu from "./components/users/Usermenu.jsx";
import CreateTicket from "./pages/users/CreateTicket.jsx";
import CreateTicketButton from "./components/users/CreateTicketButton.jsx";
import Ticket from "./pages/users/Ticket.jsx";
import Tickets from "./pages/users/Tickets.jsx";

function App() {

  return (
      <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />}/>
          <Route path="/register" element={<RegisterUser />}/>

          <Route element={<>
              <CheckLogged />
              <Usermenu />
              <CreateTicketButton />
          </>
          }>

              <Route path="/dashboard" element={<Dashboard />} />
              <Route path="/me" element={<Settings />}/>
              <Route path="/createTicket" element={<CreateTicket />}/>
              <Route path="/tickets/:ticket_id" element={<Ticket />}/>
          </Route>

      </Routes>
  )
}

export default App
