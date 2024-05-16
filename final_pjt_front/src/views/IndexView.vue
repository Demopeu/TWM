<template>
    <div class="container min-vw-100 min-vh-100">
        <RouterView />
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink, RouterView } from 'vue-router'

const currentPage = ref('login')

</script>

<style scoped>
.container {
    width: 100vh;
    height: 100vh;
    background-size: 100% 100%;
    background-image: url('@/assets/WorldMap.png');
}
</style>