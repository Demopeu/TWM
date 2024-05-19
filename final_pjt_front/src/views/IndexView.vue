<template>
    <div class="container min-vw-100 min-vh-100">
        <RouterView />
    </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
.container {
    width: 100vh;
    height: 1080px;
    max-height: 800px;
    background-size: 100% 100%;
    padding: 0;
    background-image: url('@/assets/WorldMap.png');
}
</style>