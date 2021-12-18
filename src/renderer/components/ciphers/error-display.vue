<template >
  <div>
    <small
    v-for="error in errors"
    :key="error.message"
    class="text-sm"
    :class="{
      'text-red-400': error.type == 'error',
      'text-yellow-400': error.type == 'warning',
    }"
    >{{ error.type.toUpperCase() }}: {{ error.message }}
  </small>
  </div>
</template>

<script>
export default {
  props: ['errors']
}
</script>

<style>
</style>