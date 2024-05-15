<template>
    <div class="container min-vw-100 min-vh-100">
        <login />
    </div>
</template>

<script setup>
import login from '@/components/Login.vue'
</script>

<style scoped>
.container {
    width: 100vh;
    height: 100vh;
    background-size: 100% 100%;
    background-image: url('@/assets/WorldMap.png');
}
</style>