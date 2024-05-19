<template>
    <div class="container" >
        <div class="DetailMovie" v-if="movie">
            <!-- 현재는 임시로 몇 개 요소만 띄움.
            CSS 수정할 때 원하는 필드 추가 바람. -->
            <img :src="movie.poster_image" alt="poster_image">
            <p>{{ movie.title }}</p>
            <p>{{ movie.overview }}</p>
            <p>{{ movie.rating }}</p>
            <p>{{ movie.overview }}</p>
            <p>{{ movie.certification }}</p>
            <h2>공식 예고편</h2>
            <button @click="openYoutube">
                예고편 짜잔
            </button>
            <button @click="store.addWishList(movie.id)">
                위시리스트 추가
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
import { useCounterStore } from '@/stores/counter';
const route = useRoute()
const movie = ref(null)
const MovieUrl = ref([])
const store = useCounterStore()
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
  return new Promise((resolve, reject) => {
      const apiKey = import.meta.env.VITE_YOUTUBE_API_KEY
      axios({
        method: 'get',
        url: 'https://www.googleapis.com/youtube/v3/search',
        params: {
          key: apiKey,
          q: `${movieTitle}+ official trailer`,
          part: 'snippet',
          maxResults: 1
        }
      })
      .then((response) => {
          const MovieCode = response.data.items[0].id.videoId
          MovieUrl.value=`https://www.youtube.com/watch?v=${MovieCode}`
          resolve(MovieUrl)
      })
      .catch((error) => {
          console.log(error)
          reject(error)
      })
  })
}

const openYoutube = () => {
    getMovieTrailer(movie.value.english_title)
        .then((movieUrl) => {
            window.open(movieUrl.value, '_blank');
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