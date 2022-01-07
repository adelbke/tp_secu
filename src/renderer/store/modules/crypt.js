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
  getHosts: state => {
    return state.hosts
  },
  cryptable: state => {
    let { key, algorithm, message } = state
    return !!key && !!algorithm && !!message
  },
  getKey: state => {
    return state.key
  },
  getAlgorithm: state => {
    return state.algorithm
  },
  getCrypt: state => {
    return state.crypt
  },
  getQuickResponse: state => state.quickResponse
}

const mutations = {
  RESET_STATE (state) {
    const initial = {
      key: null,
      algorithm: '',
      message: '',
      crypt: '',
      hosts: [],
      p2pServer: false,
      receivedMessages: []
    }
    Object.keys(initial).forEach(key => { state[key] = initial[key] })
  },
  SET_KEY (state, key) {
    state.key = key
  },
  SET_MESSAGE (state, message) {
    state.message = message
  },
  SET_ALGORITHM (state, algorithm) {
    if (state.algorithm !== algorithm) {
      state.key = null
      state.algorithm = algorithm
    }
  },
  SET_CRYPT (state, crypt) {
    state.crypt = crypt
  },
  ADD_MESSAGE (state, msg) {
    state.receivedMessages.push(msg)
  },
  SET_HOSTS (state, hosts) {
    state.hosts = hosts
  },
  set_quickResponse (state, quickResponse) {
    state.quickResponse = quickResponse
  }
}

const actions = {
  setMessage ({ commit, dispatch, getters }, message) {
    commit('SET_MESSAGE', message)
  },
  setKey ({ commit }, key) {
    commit('SET_KEY', key)
  },
  setAlgorithm ({ commit }, algorithm) {
    commit('SET_ALGORITHM', algorithm)
  },
  // quickEncrypt({commit}, { key, algorithm,  }){

  // }
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

  pushMessage ({ commit }, message) {
    commit('ADD_MESSAGE', message)
  },
  setHosts ({ commit }, hosts) {
    commit('SET_HOSTS', hosts)
  },
  resetState ({ commit }) {
    commit('RESET_STATE')
  }
}

export default {
  state,
  getters,
  mutations,
  actions
}
