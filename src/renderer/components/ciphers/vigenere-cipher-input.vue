<template>
  <div class="p-2 bg-blue-900 shadow-inner m-1 rounded">
    <label class="block mb-2"> Key </label>
    <input
      type="text"
      :value="cryptkey"
      @keypress="restrictChars($event)"
      v-on:input="shiftValueChanged"
      class="bg-gray-900 p-1 rounded font-mono outline-none m-1"
      @change="shiftValueChanged($event)"
      placeholder="Enter a word"
    />
  </div>
</template>

<script>
export default {
  props: ['cryptkey'],
  methods: {
    shiftValueChanged (event) {
      let result = event.target.value.toLowerCase()
      this.$emit('input', result)
    },
    restrictChars: function ($event) {
      if (
        $event.charCode === 0 ||
        /[a-z]|[A-Z]/.test(String.fromCharCode($event.charCode))
      ) {
        return true
      } else {
        $event.preventDefault()
      }
    }
  }
}
</script>

<style>
</style>