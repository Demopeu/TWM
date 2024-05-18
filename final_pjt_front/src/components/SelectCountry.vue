<template>
    <div>
        <h1>Select</h1>

        <div @click="handleClick">
            <button value="north_america">N.America</button>
            <button value="south_america">S.America</button>
            <button value="europe">Europe</button>
            <button value="india">India</button>
            <button value="china">China</button>
            <button value="korea">Korea</button>
            <button value="japan">Japan</button>
        </div>
    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore()


const handleClick = function (event) {
    const button = event.target
    if (button.tagName === 'BUTTON') {
        const region = button.value
        store.goRecommendedMovie(region)
    }
}

</script>

<style scoped>

</style>