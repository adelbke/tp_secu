<template>
  <div>
    <select
      v-model="selectedAlgorithm"
      class="bg-blue-900 p-2 font-mono outline-none rounded border-indigo-900"
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
        return this.$store.getters['crypt/getAlgorithm']
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