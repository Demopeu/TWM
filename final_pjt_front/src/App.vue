<script setup>
import { RouterLink, RouterView } from 'vue-router'
import  router  from './router/index.js'
</script>

<template>
  <div class="container-main">
  </div>
  <RouterView v-slot="{ Component }">
      <Transition name="fade">
          <component :is="Component"></component>
      </Transition>
  </RouterView>
</template>

<style>
@import './assets/styles.css';
.container-main {
  max-width: 500px;
  /* max-height: 1080px; */
}
</style>