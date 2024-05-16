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
    height: 100vh;
    background-size: cover;
    background-color: black;
}
</style>