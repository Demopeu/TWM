<template>
    <div>
        <h1>Select</h1>

        <div @click="handleClick">
            <button value="US, CA, MX">N.America</button>
            <button value="BR, AR, CL, VE, CO">S.America</button>
            <button value="GB, FR, DE, IT, RU">Europe</button>
            <button value="ID">India</button>
            <button value="CN">China</button>
            <button value="KR">Korea</button>
            <button value="JP">Japan</button>
        </div>
    </div>
</template>

<script setup>

import { useRouter } from 'vue-router'

const router = useRouter()

const handleClick = function (event) {
    const button = event.target
    if (button.tagName === 'BUTTON') {
        const region = button.value
        goRecommendedMovie(region)
    }
}

const goRecommendedMovie = function (region) {
    const countryCodes = region.split(', ')
    console.log(countryCodes)
}

</script>

<style scoped>

</style>