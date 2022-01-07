<template>
  <div class="bg-gray-800">
    <h2 class="py-2 text-xl font-bold font-mono text-white text-center">
      Crack vigenere
    </h2>

    <div
      class="
        container
        mx-auto
        my-2
        md:my-4
        py-4
        text-white
        justify-center
        flex flex-row flex-wrap
      "
    >
      <div class="w-full lg:w-2/3">
        <message-input class="m-2"></message-input>
      </div>
      <div class="w-full lg:w-1/3">
        <div
          class="
            m-2
            flex flex-row flex-wrap
            bg-blue-800
            rounded
            shadow-special
            border-blue-800
            text-gray-200
            p-4
          "
        >
          <div class="w-1/2 md:w-full">
            <label class="block"> Key length </label>
            <input
              type="number"
              v-model="keyLength"
              placeholder="Enter a numeric value"
              class="bg-gray-900 p-1 rounded font-mono outline-none m-1"
            />
          </div>
          <div class="w-1/2 md:w-full">
            <label class="block"> Results Limit </label>
            <input
              type="number"
              v-model="resultsLimit"
              placeholder="Enter a numeric value"
              class="bg-gray-900 p-1 rounded font-mono outline-none m-1"
            />
          </div>
          <div class="flex w-full justify-end">
            <button class="button-main" @click="start_crack">Crack</button>
          </div>
        </div>
      </div>
      <div class="w-full lg:justify-self-center">
        <div
          class="
            grid grid-cols-1
            gap-4
            bg-blue-800
            rounded
            shadow-special
            border-blue-800
            text-gray-200
            transition-transform
            duration-100
            ease-in
            transform
            hover:scale-105
            p-4
          "
        >
          <label class="block-title text-xl font-bold">Messages possibles</label>
          <div
            v-for="possible in formattedOutput"
            :key="possible.key"
            class="p-2 bg-blue-900 shadow-inner m-1 rounded flex flex-row justify-between"
          >
            <div>
              <span>Message: </span> 
              <span class="font-bold text-white" v-text="possible.msg"></span>
            </div>
            <div class="flex-initial">
              <span>Key: </span> 
              <span class="font-bold text-white" v-text="possible.key"></span>
            </div>
          </div>
        </div>
        <!-- <crypt-output :output="formattedOutput" class="m-2"></crypt-output> -->
      </div>
    </div>
  </div>
</template>

<script>
import messageInput from '../components/blocks/message-input.vue'
import cryptOutput from '../components/blocks/crypt-output.vue'
export default {
  components: {
    messageInput,
    cryptOutput
  },
  methods: {
    start_crack () {
      // this.$store.dispatch(
      //   'crypt/crack_vigenere',
      //   this.keyLength + ' ' + this.resultsLimit
      // )
      this.$store.dispatch('vigenere_crack/decrypt', {
        key: this.keyLength + ' ' + this.resultsLimit,
        algorithm: 'crack_vigenere',
        message: 'hello world'
      })
    }
  },
  computed: {
    formattedOutput () {
      let crypt = this.$store.getters['vigenere_crack/getCrypt']
      try {
        let jsonObject = JSON.parse(crypt)
        // let result = jsonObject.map((x) => `${x.msg}, ${x.key}`).join('\n')
        return jsonObject
      } catch (error) {
        return crypt
      }
    }
  },
  data () {
    return {
      keyLength: 0,
      resultsLimit: 0
    }
  }
}
</script>

<style>
</style>