<template>
  <div
    class="
      grid grid-cols-1
      gap-4
      bg-blue-800
      rounded
      shadow-special
      border-blue-800
      text-gray-200
      p-4
    "
  >
    <label class="block-title text-xl font-bold">algorithm</label>

    <select
      v-model="selectedAlgorithm"
      class="bg-blue-900 p-2 font-mono outline-none rouneded border-indigo-900"
    >
      <option selected disabled value="" class="text-gray-600">
        Please select an Algorithm
      </option>
      <option
        v-for="cipher in ciphers"
        :key="cipher.name"
        :value="cipher.name"
        v-text="cipher.name"
      ></option>
    </select>
    <component v-bind:is="algorithmComponent" v-model="cryptKey"></component>
    <div class="flex flex-row justify-end">
      <button
        v-if="selectedAlgorithm != 'transposition'"
        class="button-main mr-2"
        @click="decrypt()"
      >
        Decrypt
      </button>
      <button class="button-main" @click="encrypt()">Encrypt</button>
    </div>
  </div>
</template>

<script>
import ceasarCipherInput from '../ciphers/ceasar-cipher-input.vue'
import vigenereCipherInput from '../ciphers/vigenere-cipher-input.vue'
import substitutionCipherInput from '../ciphers/substitution-cipher-input.vue'

export default {
  data () {
    return {
      ciphers: [
        {
          name: 'ceasar',
          component: ceasarCipherInput
        },
        {
          name: 'vigenere',
          component: vigenereCipherInput
        },
        {
          name: 'substitution',
          component: substitutionCipherInput
        },
        {
          name: 'transposition',
          component: ceasarCipherInput
        }
      ]
    }
  },
  methods: {
    encrypt () {
      this.$store.dispatch('crypt/encrypt')
    },
    decrypt () {
      this.$store.dispatch('crypt/decrypt')
    }
  },
  computed: {
    algorithmComponent () {
      if (this.selectedAlgorithm === '') {
        return ''
      }
      return this.ciphers.find((x) => x.name === this.selectedAlgorithm)
        .component
    },
    selectedAlgorithm: {
      get () {
        let algo = this.$store.getters['crypt/getAlgorithm']
        return this.ciphers.findIndex((x) => x.name === algo) === -1
          ? 'ceasar'
          : algo
      },
      set (value) {
        this.$store.dispatch('crypt/setAlgorithm', value)
      }
    },
    cryptKey: {
      get () {
        return this.$store.getters['crypt/getKey']
      },
      set (value) {
        this.$store.dispatch('crypt/setKey', value)
      }
    }
  }
}
</script>

<style>
</style>