<template>
  <div class="bg-gray-800 text-white">
    <div>
      <h2 class="text-2xl text-center font-mono font-bold tracking-wider py-2">
        Communication System
      </h2>
    </div>
    <div class="flex flex-row flex-wrap">
      <div class="w-full md:w-1/2 border-r border-blue-400 py-2 px-4">
        <send-message></send-message>
      </div>
      <div class="w-full md:w-1/2 border-l border-blue-400">
        <receive-message></receive-message>
      </div>
    </div>
  </div>
</template>

<script>
import sendMessage from '../components/blocks/send-message.vue'
import receiveMessage from '../components/blocks/receive-message.vue'
export default {
  components: {
    sendMessage,
    receiveMessage
  }
}
</script>

<style>
</style>