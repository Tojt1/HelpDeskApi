import './App.css'
import ShowTickets from "./components/Tickets.jsx"
import Login from "./pages/login.jsx";
import Home from "./pages/Home.jsx";
import { Routes, Route} from "react-router";

function App() {

  return (
      <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
      </Routes>
  )
}

export default App
