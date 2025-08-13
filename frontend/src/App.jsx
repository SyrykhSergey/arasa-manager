import { useEffect, useState } from 'react'

function App() {
    const [status, setStatus] = useState('проверяю бэкенд...')

    useEffect(() => {
        // благодаря прокси /api -> http://127.0.0.1:5000
        fetch('/api/')
            .then(r => r.json())
            .then(d => setStatus(d.status ?? JSON.stringify(d)))
            .catch(() => setStatus('бэкенд не отвечает'))
    }, [])

    return (
        <div style={{ padding: 24, fontFamily: 'system-ui, sans-serif' }}>
            <h1>Telegram Manager (Frontend)</h1>
            <p>Backend status: {status}</p>
        </div>
    )
}

export default App
