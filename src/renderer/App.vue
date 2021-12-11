<template>
  <div id="app" class="bg-gray-900">
    <navbar></navbar>
    <router-view></router-view>
    <!-- <index></index> -->
    <!-- <python-test></python-test> -->
  </div>
</template>

<script>
// import Index from './pages/encrypt.vue'

// import pythonTest from './components/python-test.vue'
import navbar from './components/nav/navbar.vue'
export default {
  name: 'tp_secu',
  components: {
    // Index,
    navbar
  }
  // components: {
  // pythonTest
  // }
}
</script>

<style>
/* CSS */

.button-main {
  @apply bg-blue-900 shadow rounded font-mono p-2 
}
.block-title{
  @apply block mb-2 capitalize tracking-tighter font-mono
}
</style>
