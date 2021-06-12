console.log("[INFO] Starting khmer letters recognition application...")

const { exec }   = require("child_process")
const electron   = require('electron')
const { stdout } = require("process")
const path       = require('path')
const url        = require('url')

const { app, BrowserWindow, ipcMain } = electron

var interfaceWindow

// Listen to app ready event
app.on('ready', () => {
    interfaceWindow = new BrowserWindow({
        webPreferences: {
            nodeIntegration : true,
            contextIsolation: false
        }
    })
    // load html
    interfaceWindow.loadURL(url.format({
        pathname: path.join(__dirname, 'index.html'),
        protocol: 'file:',
        slashes : true
    }))
})

ipcMain.on('executeDataCollectingModule', () => {
    exec("python3 src/app.py --data True", (error, stdout, stderr) => {
        if (error) {
            console.log(error)
            return
        }
        if (stderr) {
            console.log(stderr)
            return
        }
        else console.log("[INFO] Successfully connected to data collecting module")
    })
})

ipcMain.on('executePredictModule', () => {
    exec("python3 src/app.py --predict True", (error, stdout, stderr) => {
        if (error) {
            console.log(error)
            return
        }
        if (stderr) {
            console.log(stderr)
            return
        }
        else console.log("[INFO] Successfully connected to predict module")
    })
})