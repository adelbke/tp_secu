'use strict'

import { app, BrowserWindow } from 'electron'
// import { lstat } from 'fs'
import store from '../renderer/store'

// Event Handler for starting python scripts
// const { ipcMain } = require('electron')

/**
 * Set `__static` path to static files in production
 * https://simulatedgreg.gitbooks.io/electron-vue/content/en/using-static-assets.html
 */
if (process.env.NODE_ENV !== 'development') {
  global.__static = require('path').join(__dirname, '/static').replace(/\\/g, '\\\\')
}

let mainWindow
const winURL = process.env.NODE_ENV === 'development'
  ? `http://localhost:9080`
  : `file://${__dirname}/index.html`

function createWindow () {
  /**
   * Initial window options
   */
  mainWindow = new BrowserWindow({
    height: 563,
    useContentSize: true,
    width: 1000
  })

  mainWindow.webContents.session.webRequest.onBeforeSendHeaders(
    (details, callbacks) => {
      callbacks({
        requestHeaders: {
          'origin': '*',
          'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept',
          ...details.requestHeaders
        }
      })
    }
  )

  mainWindow.webContents.session.webRequest.onHeadersReceived((details, callbacks) => {
    callbacks({
      responseHeaders: {
        'Access-Control-Allow-Origin': ['*'],
        'Access-Control-Allow-Headers': ['Origin', 'X-Requested-With', 'Content-Type', 'Accept'],
        ...details.responseHeaders
      }
    })
  })

  mainWindow.loadURL(winURL)

  // rest Server Setup
  const { fork } = require('child_process')
  const path = require('path')
  // const restServer = spawn('node', [path.join(__dirname, './server/app.js')], { detached: false })
  const restServer = fork(path.join(__dirname, './server/app.js'))

  restServer.on('message', (message) => {
    if (typeof message === 'object') {
      if ('peerMessage' in message) {
        let { peerMessage } = message
        store.dispatch('crypt/pushMessage', peerMessage)
      }
      if ('peers' in message) {
        let { peers } = message
        store.dispatch('crypt/setHosts', peers)
      }
    }
  })

  mainWindow.on('closed', () => {
    store.dispatch('crypt/resetState')
    restServer.kill(0)
    mainWindow = null
  })
}

app.on('ready', createWindow)

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', () => {
  if (mainWindow === null) {
    createWindow()
  }
})

/**
 * Auto Updater
 *
 * Uncomment the following code below and install `electron-updater` to
 * support auto updating. Code Signing with a valid certificate is required.
 * https://simulatedgreg.gitbooks.io/electron-vue/content/en/using-electron-builder.html#auto-updating
 */

/*
import { autoUpdater } from 'electron-updater'

autoUpdater.on('update-downloaded', () => {
  autoUpdater.quitAndInstall()
})

app.on('ready', () => {
  if (process.env.NODE_ENV === 'production') autoUpdater.checkForUpdates()
})
 */
