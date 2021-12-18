<template>
  <div
    class="
      flex flex-row
      items-center
      justify-between
      z-10
      bg-gray-900
      shadow-xl
      text-gray-200
      px-4
    "
  >
    <h2 class="py-2 text-2xl font-press-start">DecryptorEncryptor</h2>
    <div class="flex flex-row">
      <router-link
        class="
          button-main
          text-lg
          mr-2
          focus:outline-none
        "
        to="/encrypt"
      >
        Cryptage
      </router-link>
      <router-link
        class="
          button-main
          text-lg
          focus:outline-none
        "
        to="/comms"
      >
        Communications
      </router-link>
    </div>
  </div>
</template>

<script>
export default {}
</script>

<style>
</style>