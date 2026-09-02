import './App.css'
import Login from "./pages/login.jsx";
import Home from "./pages/Home.jsx";
import RegisterUser from "./pages/register.jsx";
import Dashboard from "./pages/Dashboard.jsx";
import CheckLogged from "./components/CheckLogged.jsx";
import Settings from "./pages/Settings.jsx";
import { Routes, Route} from "react-router";
import Usermenu from "./components/Usermenu.jsx";
import CreateTicket from "./pages/CreateTicket.jsx";
import CreateTicketButton from "./components/CreateTicketButton.jsx";
import Ticket from "./pages/Ticket.jsx";
import Tickets from "./components/Tickets.jsx";

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
