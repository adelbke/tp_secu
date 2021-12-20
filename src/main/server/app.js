// import process from 'process'
const express = require('express')
const cors = require('cors')
const app = express()

const port = 3000

app.use(cors())
app.use(express.json())

app.get('/', (req, res) => {
  console.log('hello world !!!')
  res.send('Hello world !!')
})

app.post('/encrypt', (req, res) => {
  console.log(JSON.stringify(req.body))
  res.json(req.body)
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})
