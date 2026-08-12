
import './App.css'

function App() {

  return (
      <dkv>
        <p>Hello world</p>
        <Text display="hello" />
        <Text display="wojtek"/>
      </dkv>
  )
}

function Text({display}) {
  return (
      <div>
        <p>{display}</p>
      </div>
  )
}

export default App
