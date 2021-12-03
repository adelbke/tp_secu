const state = {
  key: null,
  algorithm: '',
  message: '',
  crypt: ''
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
    // if (
    //   (state.key !== null || state.key.toString() !== '') &&
    //   (state.algorithm !== null || state.algorithm !== '') &&
    //   (state.message !== null || state.message !== '')
    // ) {
    //   return state.crypt
    // }
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
  }
}

export default {
  state,
  getters,
  mutations,
  actions
}
