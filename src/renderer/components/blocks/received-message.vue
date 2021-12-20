<template>
  <div class="bg-blue-700 rounded shadow-special p-2">
    <div class="block">
      <small class="text-sm"
        >Received Message from: <strong> {{ sender }}</strong></small
      >
    </div>
    <div class="block p-2 bg-blue-900 shadow-inner m-1 rounded">
      <pre class="whitespace-pre-line">{{ message }}</pre>
    </div>
    <div class="flex flex-row justify-between">
      <div>
        <small class="text-sm"
          >Algorithm: <strong>{{ algorithm }}</strong></small
        >
      </div>
      <div>
        <small class="text-sm"
          >Key: <strong>{{ cryptKey }}</strong></small
        >
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    sender: {
      type: String,
      default: 'myself'
    },
    message: String,
    cryptKey: String,
    algorithm: String
  }
}
</script>

<style>
</style>