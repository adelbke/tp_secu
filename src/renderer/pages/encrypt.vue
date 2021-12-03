<template>
  <div class="bg-gray-800 h-screen overflow-y-scroll">
    <div
      class="container mx-auto my-4 md:my-8 text-white flex flex-row flex-wrap"
    >
      <!-- <div class="w-full md:w-1/3" v-for="item in ['message input', 'algorithm', 'output']" :key="item">
        <span>{{item}}</span>
      </div> -->
      <div class="w-full lg:w-1/3">
        <message-input class="m-2"></message-input>
      </div>
      <div class="w-full lg:w-1/3">
        <algorithm-input class="m-2"></algorithm-input>
      </div>
      <div class="w-full lg:w-1/3">
        <crypt-output class="m-2"></crypt-output>
      </div>
    </div>
  </div>
</template>

<script>
import messageInput from '../components/blocks/message-input.vue'
import algorithmInput from '../components/blocks/algorithm-input.vue'
import cryptOutput from '../components/blocks/crypt-output.vue'
export default {
  components: {
    messageInput,
    algorithmInput,
    cryptOutput
  }
}
</script>

<style scoped>
.image-bg {
  background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
    url("~@/assets/images/app_bg.jpg");
  background-repeat: no-repeat;
  background-position: bottom;
  background-size: cover;
}

.shadow-special {
  box-shadow: rgba(0, 0, 0, 0.25) 0px 54px 55px,
    rgba(0, 0, 0, 0.12) 0px -12px 30px, rgba(0, 0, 0, 0.12) 0px 4px 6px,
    rgba(0, 0, 0, 0.17) 0px 12px 13px, rgba(0, 0, 0, 0.09) 0px -3px 5px;
}
</style>