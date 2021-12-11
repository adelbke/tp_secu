// import process from 'process'
const express = require('express')
const app = express()
const port = 3000

app.use(express.json())

const allAlgos = ['ceasar', 'transposition', 'vigenere', 'substitution']

function isString (variable) {
  return typeof variable === 'string'
}

function isNumber (variable) {
  return typeof variable === 'number'
}

function validateKey (key, algo) {
  let outputValidation = true
  if (['ceasar', 'transposition'].includes(algo)) {
    // key should be number
    outputValidation = outputValidation && isNumber(key) && key > 0
  } else {
    if (['vigenere', 'substitution'].includes(algo)) {
      // key should be string
      outputValidation = outputValidation && isString(key)
      if (algo === 'substitution') {
        outputValidation = outputValidation &&
          key.length === 26 &&
          new Set(key).size === key.length
      }
    }
  }

  return outputValidation
}

function validateRequest ({ sender, algorithm, message, key, type }) {
  let requirements = [
    isString(sender),
    isString(algorithm),
    allAlgos.includes(algorithm),
    isString(message),
    validateKey(key, algorithm),
    isString(type),
    ['encrypt', 'decrypt'].includes(type)
  ]
  // check sender
  // let check = isString(sender)
  // check algo
  // check = check && isString(algorithm) && allAlgos.includes(algorithm)
  // check message
  // check = check && isString(message)
  // check = check && validateKey(key, algorithm)

  // check = check && isString(type) && ['encrypt', 'decrypt'].includes(type)

  return !requirements.includes(false)
}

app.get('/', (req, res) => {
  console.log('hello world !!!')
  res.send('Hello world !!')
})

app.post('/encrypt', (req, res) => {
  let msgObject = req.body
  validateRequest(req.body)
  console.log(JSON.stringify(msgObject))
  res.json(msgObject)
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})
