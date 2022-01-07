const { fork } = require('child_process')
const path = require('path')
const server = fork(path.join(__dirname, './app.js'))

server.on('message', (msg) => {
  console.log('Incoming console log from parent: ', msg, typeof msg)
})
