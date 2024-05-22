<template>
    <div class="container min-vw-100">
        <RouterView />
    </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
body, .wrapper {
    background-color: black;
    margin: 0;
    padding: 0;
    min-height: 100vh;
    height: 100%;
    width: 100%;
    /* overflow: hidden; */
}

.container {
    background-color: black;
    max-height: 1080px;
    height: 100vh;
    overflow: auto;
    position: relative;
    background-image:url('@/assets/MovieBack.jpg');
    background-repeat: no-repeat;
    background-position: 80% 10%;
    background-size: 40%;
}

</style>