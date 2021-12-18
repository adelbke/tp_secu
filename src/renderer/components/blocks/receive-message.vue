<template>
  <div class="flex flex-col items-center">
    <div v-for="(msg, index) in $store.state.crypt.receivedMessages" :key="index">
      <pre>{{ msg }}</pre>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function () {
    return {
    }
  }
}
</script>

<style>
</style>