<template>
  <div id="app" class="bg-gray-800 h-screen">
    <navbar></navbar>
    <router-view></router-view>
    <!-- <index></index> -->
    <!-- <python-test></python-test> -->
  </div>
</template>

<script>
import navbar from './components/nav/navbar.vue'
export default {
  name: 'tp_secu',
  components: {
    navbar
  }
}
</script>

<style>
/* CSS */
.shadow-special {
  box-shadow: rgba(0, 0, 0, 0.25) 0px 54px 55px,
    rgba(0, 0, 0, 0.12) 0px -12px 30px, rgba(0, 0, 0, 0.12) 0px 4px 6px,
    rgba(0, 0, 0, 0.17) 0px 12px 13px, rgba(0, 0, 0, 0.09) 0px -3px 5px;
}

.button-main {
  @apply bg-blue-900 shadow rounded font-mono p-2;
}
.block-title {
  @apply block mb-2 capitalize tracking-tighter font-mono;
}
.block-title{
  @apply block mb-2 capitalize tracking-tighter font-mono
}
</style>
