<template>
    <div>
        <h1>Movies set in</h1>
        <h1>{{ country }}</h1>
    </div>
</template>

<script setup>
import {ref} from 'vue'
const country = ref(null)
</script>

<style scoped>

</style>