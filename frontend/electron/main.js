import { app, BrowserWindow } from 'electron'
import { spawn } from 'child_process'
import path from 'path'
import { fileURLToPath } from 'url'

const __filename = fileURLToPath(import.meta.url)
const __dirname  = path.dirname(__filename)

let pyProc = null

function startPythonBackend() {
  const pythonPath  = path.join(__dirname, '../../backend/venv/Scripts/python.exe')
  const backendCwd  = path.join(__dirname, '../../backend')

  // запускаем uvicorn как модуль, рабочая директория — backend
  pyProc = spawn(
      pythonPath,
      ['-m', 'uvicorn', 'main:app', '--host', '127.0.0.1', '--port', '5000'],
      { cwd: backendCwd, stdio: 'pipe' }
  )

  pyProc.stdout.on('data', d => console.log('[Backend]', d.toString().trim()))
  pyProc.stderr.on('data', d => console.error('[Backend ERR]', d.toString().trim()))
  pyProc.on('close', code => console.log('[Backend] exit', code))
}

function createWindow() {
  const win = new BrowserWindow({
    width: 1200, height: 800,
    webPreferences: { nodeIntegration: false, contextIsolation: true }
  })
  win.loadURL('http://localhost:5173') // dev
  // prod: win.loadFile(path.join(__dirname, '../dist/index.html'))
}

app.whenReady().then(() => {
  startPythonBackend()
  setTimeout(createWindow, 3000) // позже сделаем ожидание порта
})

app.on('will-quit', () => { if (pyProc) pyProc.kill() })
