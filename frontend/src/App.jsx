import { useEffect, useState } from 'react'

function App() {
  const [services, setServices] = useState([])

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/services/')
      .then((response) => response.json())
      .then((data) => {
        setServices(data)
      })
      .catch(() => {
        setServices([])
      })
  }, [])

  return (
    <div>
      <h1>CloudNexus</h1>

      <h2>Services</h2>

      {services.map((service) => (
        <div key={service.id}>
          <p>
            <strong>{service.name}</strong> — {service.status}
          </p>
        </div>
      ))}
    </div>
  )
}

export default App