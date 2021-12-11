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
    <label class="block-title text-xl font-bold">Message</label>
    <div class="p-2">
      <textarea
        class="
          resize-none
          bg-blue-900
          border-blue-800
          w-full
          p-1
          font-code
          rounded
          shadow-outline
          outline-none
          mb-2
        "
        :class="customClasses"
        placeholder="Enter the message to encrypt"
        v-model="message"
        rows="5"
      ></textarea>
      <a
        class="
          text-blue-500
          hover:underline
          font-light
          text-sm text-right
          cursor-pointer
          block
        "
        @click="toggleOptions()"
        >more options</a
      >
    </div>

    <transition name="fade">
      <div
        class="
          bg-blue-900
          shadow-inner
          border-blue-800
          rounded
          p-2
          flex flex-row flex-wrap
          justify-around
          transition-opacity
          duration-500
          ease-in-out
        "
        v-show="displayOptions"
      >
        <div class="px-2 py-1">
          <label>Allow lowercase letters</label>
          <input
            type="checkbox"
            :disabled="lowercaseLetters && !uppercaseLetters"
            v-model="lowercaseLetters"
          />
        </div>
        <div class="px-2 py-1">
          <label>Allow uppercase letters</label>
          <input
            type="checkbox"
            :disabled="uppercaseLetters && !lowercaseLetters"
            v-model="uppercaseLetters"
          />
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  data () {
    return {
      displayOptions: false,
      lowercaseLetters: true,
      uppercaseLetters: false,
      numbers: false
    }
  },
  computed: {
    customClasses () {
      return {
        uppercase: !this.lowercaseLetters,
        lowercase: !this.uppercaseLetters
      }
    },
    message: {
      get () {
        return this.$store.getters['crypt/getMessage']
      },
      set (value) {
        if (!this.uppercaseLetters) {
          value = value.toLowerCase()
        }
        if (!this.lowercaseLetters) {
          value = value.toUpperCase()
        }
        this.$store.dispatch('crypt/setMessage', value)
      }
    }
  },
  methods: {
    toggleOptions () {
      this.displayOptions = !this.displayOptions
    }
  }
}
</script>

<style  scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
.font-code {
  font-family: Menlo, Monaco, Consolas, "Liberation Mono", "Courier New",
    monospace;
}
</style>