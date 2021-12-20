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
      ],
      selectedCipher: '',
      enteredKey: ''
    }
  },
  props: {
    initAlgoKeyData: {
      type: Object,
      default: function () {
        return {}
      }
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
        return this.selectedCipher
      },
      set (value) {
        let vm = this
        vm.selectedCipher = value
        vm.$emit('input', {
          cryptKey: vm.cryptKey,
          algorithm: vm.selectedAlgorithm
        })
      }
    },
    cryptKey: {
      get () {
        return this.enteredKey
      },
      set (value) {
        let vm = this
        vm.enteredKey = value
        vm.$emit('input', {
          cryptKey: vm.cryptKey,
          algorithm: vm.selectedAlgorithm
        })
      }
    }
  }
}
</script>

<style>
</style>