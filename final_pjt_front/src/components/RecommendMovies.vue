<template>
    <div>
        <div class="title">
        <h1>Movies set in</h1>
        <h1>{{ name }}</h1>
        </div>
        <div>
            <div v-for="movie in store.movies" :key="movie.id" :movie="movie">
                <RouterLink :to="{ name: 'MovieDetail', params: { id: movie.id } }">
                    <img :src="movie.poster_image" alt="poster_image">
                </RouterLink>
            </div>
        </div>
        <div class="movieLists">
            <!-- <div v-for="movie in Store.movies" :key="movie.id" >
                <div v-if="movie.poster_path" class="movie-card" @click="goDetailpage(movie.id)">
                <img :src="getMoviePosterUrl(movie.poster_path)" alt="Movie Poster" class="movie-img"/>
                </div>
            </div> -->
        </div>
    </div>
</template>

<script setup>
import {ref} from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute, RouterLink } from 'vue-router'

const store = useCounterStore()
const route = useRoute()
// const getMoviePosterUrl = (posterPath) => `https://image.tmdb.org/t/p/w500${posterPath}`;
const name = route.params.country

// Detailpage로 이동
// const goDetailpage = (movieId)=> route.push(`/${movieId}`)

// 영화리스트: movies;알고리즘을 통해 영화가 들어오는 함수:getMovies()
// onMounted(()=>{
//     movieStore.getMovies()
// })

</script>

<style scoped>
/* 박스 관련 */
.title {
    position: relative;
    min-width: 800px;
    height: 200px;
}
/* 리스트 관련 */
.movie-list{
    display: flex;
    flex-wrap: wrap;
    gap: 10px;

}
.movie-card{
    flex-basis: calc(33.33% - 10px);
    border: 1px solid #ccc;
    padding: 10px;
    width: 200px;
    height: 900px;
    
}
.movie-img{
    width: 100%;
}

/* 글씨체 관련 */
h1{
    font-weight: bold;
    margin-left: 5vh;
    font-size: 128px;
    letter-spacing: -5px;
    color: white;
    top: 50%;
    transform: translateY(100%);
}
</style>