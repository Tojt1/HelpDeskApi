import './App.css'
import Login from "./pages/login.jsx";
import Home from "./pages/Home.jsx";
import { Routes, Route} from "react-router";

function App() {

  return (
      <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />}/>
      </Routes>
  )
}

export default App
