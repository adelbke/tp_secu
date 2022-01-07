<template>
  <div class="">
    <h2 class="text-center text-xl font-mono font-bold text-gray-300 pb-2">
      Send a Message
    </h2>
    <div
      class="m-1 p-2 bg-blue-800 rounded shadow-special grid grid-cols-1 gap-4"
      method="post"
    >
      <div>
        <label class="block" for="">Select a Recipient:</label>
        <div class="flex flex-row">
          <select
            v-model="selectedHost"  
            class="
              bg-blue-900
              p-2
              font-mono
              outline-none
              rounded
              shadow
              mr-2
              border-indigo-900
            "
          >
            <option
              selected
              disabled
              class="text-gray-500 text-lg"
            >
              Please select a Recipient
            </option>
            <option
              class="text-white"
              v-for="host in hosts"
              :key="host.name"
              :value="host"
              v-text="`${host.name} - ${host.ip}`"
            ></option>
          </select>
          <button class="button-main" @click="refresh">
            <refresh-icon></refresh-icon>
          </button>
        </div>
      </div>
      <div>
        <label>Select a cipher:</label>
        <algo-input-form v-model="algoKey"></algo-input-form>
      </div>
      <div>
        <label class="block">Enter a message:</label>
        <textarea
          class="
            resize-none
            bg-blue-900
            w-full
            p-1
            font-code
            rounded
            outline-none
            mb-2
          "
          placeholder="Enter a message to send"
          v-model="message"
          rows="5"
        ></textarea>
      </div>
      <div class="flex flex-row justify-end">
        <button class="button-main" @click="sendMessage()">Send</button>
      </div>
    </div>
  </div>
</template>

<script>
import refreshIcon from '../icons/refresh.vue'
import algoInputForm from './algo-input-form.vue'
import axios from 'axios'
export default {
  components: {
    refreshIcon,
    algoInputForm
  },
  methods: {
    refresh () {
      // do something
    },
    async sendMessage () {
      let vm = this
      let { algorithm, cryptKey } = vm.algoKeyData

      // this.$store.dispatch('crypt/setKey', cryptKey)
      // this.$store.dispatch('crypt/setAlgorithm', algorithm)
      // this.$store.dispatch('crypt/setMessage', vm.message)
      // this.$store.dispatch('crypt/encrypt')

      await axios.post('http://' + this.selectedHost.ip + ':3000/encrypt', {
        sender: 'adel',
        algorithm: algorithm,
        message: this.$store.getters['crypt/getCrypt'],
        key: cryptKey,
        type: 'encrypt'
      })
    }
  },
  data () {
    return {
      // hosts: [
      //   { ip: '192.168.1.1', mac: 'AC:CF:23:31:9B:FC', name: 'localhost' }
      // ],
      selectedHost: {},
      message: '',
      algoKeyData: {}
    }
  },
  computed: {
    hosts () {
      return this.$store.getters['crypt/getHosts']
    },
    algoKey: {
      get () {
        return this.algoKeyData
      },
      set (value) {
        this.algoKeyData = value
      }
    }
  }
}
</script>

<style>
</style>