<template>
    <div class="container" >
        <div class="DetailMovie" v-if="movie">
            <img :src="movie.poster_image" alt="poster_image">
            <p>{{ movie.title }}</p>
            <p>{{ movie.overview }}</p>
            <p>{{ movie.rating }}</p>
            <p>{{ movie.overview }}</p>
            <p>{{ movie.certification }}</p>
            <h2>공식 예고편</h2>
            <button @click="getMovieTrailer(movie.title)">
                예고편 짜잔
            </button>
        </div>
        <div v-else>
            <p>Loading...</p>
        </div>
    </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue';
import { onMounted } from 'vue';
import { useRoute } from 'vue-router';
const route = useRoute()
const movie = ref(null)
onMounted(() => {
    axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/recommend/detail/${route.params.id}/`
    })
    .then(response => {
        movie.value = response.data
    })
    .catch(error => {
        console.log(error)
    })
})

const getMovieTrailer = function (movieTitle) {
  const apiKey = import.meta.env.VITE_TMDB_API_KEY
  axios({
    method: 'get',
    url: 'https://www.googleapis.com/youtube/v3/search',
    params: {
      key: apiKey,
      q: movieTitle + 'official trailer',
      type: 'video',
      part: 'snippet',
      maxResults: 1
    }
  })
    .then((response) => {
      console.log(response.data)
      const videoId = response.data.items[0].id.videoId
      const trailerUrl = `https://www.youtube.com/watch?v=${videoId}`
      window.open(trailerUrl, '_blank')
    })
    .catch((error) => {
      console.log(error)
    })
}

</script>

<style scoped>
.container {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
}
.DetailMovie{
    width: 90%;
    height: 90%;
    background-color: white;
}
</style>