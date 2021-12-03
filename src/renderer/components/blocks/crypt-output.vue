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
    <label
      class="block mb-2 capitalize text-xl tracking-tighter font-press-start"
      >Encrypted</label
    >
    <div class="p-2 bg-blue-900 shadow-inner m-1 rounded">
      <pre class="whitespace-pre-line">{{ cryptOutput }}</pre>
    </div>
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
      return this.$store.getters['crypt/getCrypt']
    }
  },
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