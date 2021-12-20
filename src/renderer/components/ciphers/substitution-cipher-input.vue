<template>
  <div class="p-2 bg-blue-900 shadow-inner m-1 rounded flex flex-col">
    <div class="mb-2 flex flex-col">
      <label
        class="
          block
          font-mono font-bold
          uppercase
          text-blue-400 text-sm
          tracking-widest
        "
        >PlainText Alphabet</label
      >
      <input
        type="text"
        :value="plainAlphabet"
        v-on:input="plainAlphabetChanged"
        class="bg-gray-900 p-1 rounded font-mono outline-none m-1"
      />
      <error-display :errors="plainAlphabetErrors"></error-display>
    </div>
    <div class="flex flex-col">
      <label
        class="
          block
          font-mono font-bold
          uppercase
          text-blue-400 text-sm
          tracking-widest
        "
        >CipherText Alphabet</label
      >
      <input
        type="text"
        :value="cipherAlphabet"
        v-on:input="cipherAlphabetChanged"
        class="bg-gray-900 p-1 rounded font-mono outline-none m-1"
      />
      <error-display :errors="cipherAlphabetErrors"></error-display>
    </div>
    <error-display :errors="globalErrors"></error-display>
  </div>
</template>

<script>
import errorDisplay from './error-display.vue'
export default {
  props: ['cryptkey'],
  components: { errorDisplay },
  data () {
    return {
      plainAlphabet: 'abcdefghijklmnopqrstuvwxyz',
      cipherAlphabet: 'abcdefghijklmnopqrstuvwxyz'
    }
  },
  mounted () {
    this.$emit('input', this.outputKey)
  },
  computed: {
    outputKey () {
      return this.plainAlphabet + ' ' + this.cipherAlphabet
    },
    cipherAlphabetErrors () {
      let vm = this
      let output = []
      if (!vm.hasUniqueChars(vm.cipherAlphabet)) {
        output.push({
          message: 'The cipher Alphabet is not unique',
          type: 'warning'
        })
      }
      return output
    },
    plainAlphabetErrors () {
      let vm = this
      let output = []
      if (!vm.hasUniqueChars(vm.plainAlphabet)) {
        output.push({
          message: 'The plain Alphabet is not unique',
          type: 'warning'
        })
      }
      return output
    },
    globalErrors () {
      let vm = this
      let output = []
      if (vm.plainAlphabet.length !== vm.cipherAlphabet.length) {
        output.push({
          message: 'The alphabets have different lengths',
          type: 'error'
        })
      }
      return output
    }
  },
  methods: {
    hasUniqueChars (text) {
      return new Set(text).size === text.length
    },

    cipherAlphabetChanged (event) {
      let vm = this
      vm.cipherAlphabet = event.target.value
      this.$emit('input', vm.outputKey)
    },
    plainAlphabetChanged (event) {
      let vm = this
      vm.plainAlphabet = event.target.value
      this.$emit('input', vm.outputKey)
    }
  }
}
</script>

<style>
</style>