<template>
  <div>
    <input type="text" v-model="textInput" @change="encrypt(textInput)" />
    Encrypted:
    <span v-text="encryptedText"></span>
  </div>
</template>

<script>
export default {
  data () {
    return {
      textInput: '',
      encryptedText: ''
    }
  },
  methods: {
    encrypt (inp) {
      // let { PythonShell } = require('python-shell')
      // let path = require('path')
      // let options = {
      //   scriptPath: path.join(__dirname, '../../../python-scripts'),
      //   args: [inp]
      // }
      // let pyshell = new PythonShell('main.py', options)

      // let vm = this

      // pyshell.on('message', function (message) {
      //   console.log(`${this.encryptedText} => ${message}`)
      //   vm.encryptedText = message
      // })
      const { ipcRenderer } = require('electron')
      ipcRenderer.send('python-call', 'ping')
    }
  }
}
</script>

<style>
</style>