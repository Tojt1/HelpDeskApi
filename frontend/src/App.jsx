import './App.css'
import Login from "./pages/commons/login.jsx";
import Home from "./pages/users/Home.jsx";
import RegisterUser from "./pages/users/register.jsx";
import Dashboard from "./pages/users/Dashboard.jsx";
import CheckLogged from "./components/users/CheckLogged.jsx";
import Settings from "./pages/commons/Settings.jsx";
import { Routes, Route} from "react-router";
import CreateTicket from "./pages/users/CreateTicket.jsx";
import Ticket from "./pages/users/Ticket.jsx";
import RequireAdmin from "./components/RequireAdmin.jsx";
import AdminDashboard from "./pages/admins/AdminDashboard.jsx";
import UserLayout from "./components/users/UserLayout.jsx";
import AdminTicket from "./pages/admins/AdminTicket.jsx";
import AdminLayout from "./components/AdminLayout.jsx";

function App() {

  return (
      <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />}/>
          <Route path="/register" element={<RegisterUser />}/>

          <Route element={<CheckLogged />} >

              <Route element={<UserLayout />}>

                  <Route path="/dashboard" element={<Dashboard />} />
                  <Route path="/me" element={<Settings />}/>
                  <Route path="/createTicket" element={<CreateTicket />}/>
                  <Route path="/tickets/:ticket_id" element={<Ticket />}/>
              </Route>

              <Route element={<RequireAdmin />}>
                  <Route element={<AdminLayout/>}>
                    <Route path="/admin/dashboard" element={<AdminDashboard />}></Route>
                    <Route path="/admin/:ticket_id" element={<AdminTicket />}></Route>
                  </Route>
              </Route>

          </Route>

      </Routes>
  )
}

export default App
