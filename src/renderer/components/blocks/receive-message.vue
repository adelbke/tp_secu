<template>
  <div>
    <h2 class="text-xl font-mono font-bold text-center text-gray-300 py-2">
      Received Messages
    </h2>
    <!-- Add clear history functionality -->
    <div class="md:h-96 md:overflow-y-auto grid grid-flow-row grid-cols-1 gap-4 px-4">
      <received-message
        v-for="(msg, index) in $store.state.crypt.receivedMessages"
        :key="index"
        :sender="msg.sender"
        :message="msg.message"
        :decrypted-message="msg.decryptedMessage"
        :cryptKey="String(msg.key)"
        :algorithm="msg.algorithm"
      ></received-message>
    </div>
  </div>
</template>

<script>
import receivedMessage from './received-message.vue'
export default {
  components: {
    receivedMessage
  },
  data: function () {
    return {}
  }
}
</script>

<style scoped>

</style>