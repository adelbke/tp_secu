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
            bg-blue-800
            shadow-inner
            rounded
            shadow-special
            border-blue-800
            text-gray-200
            p-4
          "
        >
          <div class="flex flex-row justify-between">
            <label class="block-title text-xl font-bold"
              >Messages possibles</label
            >
            <div>
              <label for="" class="text-md font-normal text-gray-300">
                {{ formattedOutput.length }} Results Generated
              </label>

              <button class="text-blue-500 underline" @click="clearList">
                Clear list
              </button>
            </div>
          </div>
          <!-- <div class="flex flex-row"></div>
          <div
            v-for="possible in formattedOutput"
            :key="possible.key"
            class="
              py-2
              bg-blue-800
              rounded
              flex flex-row
              justify-between
            "
          >
            <div>
              <span>Message: </span>
              <span class="font-bold text-white" v-text="possible.msg"></span>
            </div>
            <div class="flex-initial">
              <span>Key: </span>
              <span class="font-bold text-white" v-text="possible.key"></span>
            </div>
          </div> -->

          <table class="table-auto mx-auto">
            <thead>
              <tr>
                <th class="px-4 py-2">Rank</th>
                <th class="px-4 py-2">Message</th>
                <th class="px-4 py-2">Key</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(output, index) in formattedOutput" :key="index">
                <td class="border px-4 py-2">{{ index + 1 }}</td>
                <td class="border px-4 py-2">{{ output.msg }}</td>
                <td class="border px-4 py-2">{{ output.key }}</td>
              </tr>
            </tbody>
          </table>
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
    clearList () {
      this.$store.dispatch('vigenere_crack/reset_state')
    },
    start_crack () {
      // this.$store.dispatch(
      //   'crypt/crack_vigenere',P
      //   this.keyLength + ' ' + this.resultsLimit
      // )
      this.$store.dispatch('vigenere_crack/decrypt', {
        key: this.keyLength + ' ' + this.resultsLimit,
        algorithm: 'crack_vigenere',
        msg: this.$store.getters['crypt/getMessage']
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