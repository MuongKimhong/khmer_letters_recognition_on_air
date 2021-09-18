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

ipcMain.on('executeDataCollectingModule', (event) => {
    var dialog = electron.dialog
    dialog.showOpenDialog(interfaceWindow, {properties: ['openDirectory']})
    .then((result) => {
        var folderPath = result.filePaths
        console.log(folderPath[0])

        event.reply('startingDataCollectingModule')

        setTimeout(() => {
            event.reply('successRunningDataCollectingModule')
        }, 7000)

        exec(`python3 src/app.py --data True --savepath ${folderPath[0] + '/'}`, (error, stdout, stderr) => {
            if (error) {
                console.log(error)
                return
            }
            if (stderr) {
                console.log(stderr)
                return
            }
            else {
                event.reply('stopDataCollectingModule')
            } 
        })
    })
})

ipcMain.on('executePredictModule', (event) => {
    var dialog = electron.dialog
    dialog.showOpenDialog(interfaceWindow, { properties: ['openFile'] }).then((result) => {
      if (result.canceled == false) {
        var folderPath = result.filePaths[0]
        console.log(folderPath)
        event.reply('startingPredictModule')
        setTimeout(() => {
          event.reply('successRunningPredictModule')
        }, 7000)
        exec(`python3 src/app.py --predict True --modelpath ${folderPath}`, (error, stdout, stderr) => {
          if (error) {
            console.log(error)
            return
          }
          if (stderr) {
            console.log(stderr)
            return
          } else {
            event.reply('stopPredictModule')
          }
        })
      }
      
    })
})