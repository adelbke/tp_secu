const state = {
  crypt: '',
  message: ''
}
const getters = {
  getCrypt: state => state.crypt
}
const mutations = {
  SET_CRYPT (state, crypt) {
    state.crypt = crypt
  }
}

const actions = {
  decrypt ({ commit, state } = null, { algorithm, key, msg }) {
    commit('SET_CRYPT', '')
    let { PythonShell } = require('python-shell')
    let path = require('path')
    let options = {
      pythonOptions: ['-u'],
      pythonPath: '/usr/bin/python3.9',
      scriptPath: path.join(__dirname, '/../../../../python-scripts'),
      args: ['decrypt',
        '-a', algorithm,
        '-m', msg,
        '-k', key.toString()
      ]
    }
    let pyshell = new PythonShell('main.py', options)

    pyshell.on('message', function (message) {
      commit('SET_CRYPT', message)
    })
    pyshell.on('stderr', function (stderr) {
      console.log(stderr)
    })
  },
  reset_state ({ commit }) {
    commit('SET_CRYPT', '')
  }
}

export default {
  state,
  getters,
  mutations,
  actions
}
