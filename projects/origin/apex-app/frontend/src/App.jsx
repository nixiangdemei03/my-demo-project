import { useState, useEffect } from 'react'

function App() {
  const [msg, setMsg] = useState('Loading...')

  useEffect(() => {
    fetch('/api/hello')
      .then(res => res.json())
      .then(data => setMsg(data.msg))
      .catch(() => setMsg('Error: Backend not reachable'))
  }, [])

  return (
    <div className="app">
      <h1>APEX — Auto Parts EXport</h1>
      <p>Backend says: <strong>{msg}</strong></p>
    </div>
  )
}

export default App
