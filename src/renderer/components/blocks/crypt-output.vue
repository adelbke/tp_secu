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
      transition-transform
      duration-100
      ease-in
      transform
      hover:scale-105
      p-4
    "
  >
    <label class="block-title text-xl font-bold">Encrypted</label>
    <pre
      class="
        p-2
        bg-blue-900
        shadow-inner
        m-1
        rounded
        whitespace-pre-wrap
        break-words
      "
      v-text="!!cryptOutput ? cryptOutput : '\n'"
    ></pre>
    <div class="flex justify-end">
      <button @click="copyToClipboard" class="button-main">
        Copy to Clipboard
      </button>
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    cryptOutput () {
      return this.output ? this.output : this.$store.getters['crypt/getCrypt']
    }
  },
  props: ['output'],
  methods: {
    copyToClipboard () {
      let vm = this
      const { clipboard } = require('electron')
      clipboard.writeText(vm.cryptOutput)
      vm.$toast.open('Text successfully copied to clipboard !')
    }
  }
}
</script>

<style>
</style>