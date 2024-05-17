<template>
  <div class="container min-vw-100 min-vh-100" >
    <RouterView />
  </div>
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'

</script>

<style scoped>
.container {
  background-color: #E9FCE7;
  width: 100%;
  height: 100vh;
  overflow-y: auto;
}
</style>