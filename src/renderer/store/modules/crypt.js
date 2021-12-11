const state = {
  key: null,
  algorithm: '',
  message: '',
  crypt: '',
  hosts: [],
  p2pServer: false,
  receivedMessages: []
}

const getters = {
  getMessage: state => {
    return state.message
  },
  getKey: state => {
    return state.key
  },
  getAlgorithm: state => {
    return state.algorithm
  },
  getCrypt: state => {
    return state.crypt
  }
}

const mutations = {
  SET_KEY (state, key) {
    state.key = key
  },
  SET_MESSAGE (state, message) {
    state.message = message
  },
  SET_ALGORITHM (state, algorithm) {
    state.algorithm = algorithm
  },
  SET_CRYPT (state, crypt) {
    state.crypt = crypt
  },
  SET_P2PSERVER (state, server) {
    state.p2pServer = server
  },
  ADD_MESSAGE (state, msg) {
    state.receivedMessages.push(msg)
  }
}

const actions = {
  setMessage ({ commit }, message) {
    commit('SET_MESSAGE', message)
  },
  setKey ({ commit }, key) {
    commit('SET_KEY', key)
  },
  setAlgorithm ({ commit }, algorithm) {
    commit('SET_ALGORITHM', algorithm)
  },
  encrypt ({ state, commit }) {
    let { PythonShell } = require('python-shell')
    let path = require('path')
    let options = {
      pythonOptions: ['-u'],
      pythonPath: '/usr/bin/python3.9',
      scriptPath: path.join(__dirname, '/../../../../python-scripts'),
      args: ['encrypt',
        '-a', state.algorithm,
        '-m', state.message,
        '-k', state.key.toString()
      ]
    }
    let pyshell = new PythonShell('main.py', options)

    pyshell.on('stderr', function (stderr) {
      console.log(stderr)
    })
    pyshell.on('message', function (message) {
      // console.log('tkheltet2')
      // console.log(message)
      commit('SET_CRYPT', message)
    })
  },
  decrypt ({ state, commit }) {
    let { PythonShell } = require('python-shell')
    let path = require('path')
    let options = {
      pythonOptions: ['-u'],
      pythonPath: '/usr/bin/python3.9',
      scriptPath: path.join(__dirname, '/../../../../python-scripts'),
      args: ['decrypt',
        '-a', state.algorithm,
        '-m', state.message,
        '-k', state.key.toString()
      ]
    }
    let pyshell = new PythonShell('main.py', options)

    pyshell.on('stderr', function (stderr) {
      console.log(stderr)
    })
    pyshell.on('message', function (message) {
      // console.log('tkheltet2')
      // console.log(message)
      commit('SET_CRYPT', message)
    })
  },

  startServer ({state, commit}) {
    // rest Server Setup
    const { spawn } = require('child_process')
    const path = require('path')
    const restServer = spawn('node', [path.join(__dirname, './server/app.js')])

    restServer.stdout.on('message', (data) => {
      console.log('restServer says: ', data)
    })
  },
  pushMessage ({ commit }, message) {
    commit('ADD_MESSAGE', message)
  }
}

export default {
  state,
  getters,
  mutations,
  actions
}
