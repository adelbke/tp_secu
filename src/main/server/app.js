// import process from 'process'
const express = require('express')
const cors = require('cors')
const requestIp = require('request-ip')
const app = express()

const port = 3000

function getIpV4 (req) {
  let clientIp = requestIp.getClientIp(req)
  let tableSplit = clientIp.split(':')
  return tableSplit[tableSplit.length - 1]
}

app.use(cors())
app.use(express.json())

let peers = [
  { name: 'adel', ip: '10.42.0.1', active: true }
]

app.get('/', (req, res) => {
  console.log('hello world !!!')
  res.send('Hello world !!')
})

app.post('/get-peers', (req, res) => {
  let ip = getIpV4(req)
  let info = req.body
  let peer = { ip }
  if ('name' in info) {
    peer.name = info.name
  }
  if ('active' in info) {
    peer.active = info.active
  }
  let peerIndex = peers.findIndex(x => x.name === peer.name || x.ip === peer.ip)
  if (peerIndex === -1) {
    peers.push(peer)
  } else {
    peers[peerIndex] = peer
  }
  process.send({ peers })
  // console.log('/get-peers::' + JSON.stringify(peers))
  res.json(peers)
})

app.post('/encrypt', (req, res) => {
  // console.log('/encrypt::' + JSON.stringify(req.body))
  let ip = getIpV4(req)
  let index = peers.findIndex(x => x.ip === ip)
  if (index === -1 && 'sender' in req.body) {
    peers.push({
      ip,
      name: peers[index],
      active: true
    })
  }
  process.send({ peerMessage: req.body })
  res.json(req.body)
})

app.listen(port, () => {
  console.log(`HTTP Server Listening at http://0.0.0.0:${port}`)
})
