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
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()


const handleClick = function (event) {
    const button = event.target
    if (button.tagName === 'BUTTON') {
        const region = button.value
        goRecommendedMovie(region)
    }
}

const goRecommendedMovie = function (region) {
    const country = region

    // 임시 데이터베이스 만드는 용
    // axios({
    // method: 'get',
    // url: 'http://127.0.0.1:8000/movies/recommend/'
    // })
    // .then(response => {
    //     console.log('데이터 보내기 성공')
    //     router.push({ name: 'RecommendMovies', params: { country: country }})
    // })
    // .catch(error => {
    //     console.log(error)
    // })
    axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/recommend/${country}/`,
    })
    .then(response => {
        console.log('데이터')
        console.log(response.data)
    })
    .catch(error => {
        console.log('실패')
        console.log(error)
    })
}

</script>

<style scoped>

</style>