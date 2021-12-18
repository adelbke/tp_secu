<template>
  <div class="p-2 bg-blue-900 shadow-inner m-1 rounded">
    <label class="block mb-2">
      Key
      <small class="text-sm">(Shift Value)</small>
    </label>
      <input
        type="number"
        :value="cryptkey"
        v-on:input="shiftValueChanged"
        placeholder="Enter a numeric value"
        class="bg-gray-900 p-1 rounded font-mono outline-none m-1"
        @change="shiftValueChanged($event)"
      />
  </div>
</template>

<script>
export default {
  props: ['cryptkey'],
  data () {
    return {
      shiftValue: 0
    }
  },
  methods: {
    shiftValueChanged (event) {
      this.$emit('input', parseInt(event.target.value))
    }
  }
}
</script>

<style>
</style>