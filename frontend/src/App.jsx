import './App.css'
import Login from "./pages/login.jsx";
import Home from "./pages/Home.jsx";
import RegisterUser from "./pages/register.jsx";
import Dashboard from "./pages/Dashboard.jsx";
import CheckLogged from "./components/CheckLogged.jsx";
import { Routes, Route} from "react-router";

function App() {

  return (
      <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />}/>
          <Route path="/register" element={<RegisterUser />}/>
          <Route path="/dashboard" element={
              <CheckLogged>
                  <Dashboard />
              </ CheckLogged>
              } />
      </Routes>
  )
}

export default App
