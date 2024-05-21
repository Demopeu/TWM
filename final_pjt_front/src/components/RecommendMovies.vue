<template>
    <div>
        <div class="logo-container">
          <img src="@/assets/Logo_white.png" alt="logo" class="logo">
        </div>
      <div class="box-box">
        <div class="title">
            <h1 class="title-text">Movies set in</h1>
            <h1 class="title-text">{{ name }}</h1>
        </div>
      </div>
      <div class="movie-list-container">
        <div class="movie-list">
          <div class="movie-item" v-for="movie in store.movies" :key="movie.id">
            <RouterLink :to="{ name: 'MovieDetail', params: { id: movie.id } }">
              <img :src="movie.poster_image" alt="poster_image">
            </RouterLink>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { useCounterStore } from '@/stores/counter'
  import { useRoute, RouterLink } from 'vue-router'
  import { ref,onMounted } from 'vue'
  
  const store = useCounterStore()
  const route = useRoute()
  const name = route.params.country
  const htmlName = ref()

  onMounted(() => {
    htmlName.value = name
    console.log(route)
  })
  </script>
  
  <style scoped>
  .box-box {
    display: flex;
    flex-direction: column;
    margin: 0 5vh 5vh 5vh;
  }
  
  .title {
    position: relative;
    min-width: 800px;
    height: 200px;
    margin-top: 10vh;
    margin-bottom: 10vh;
  }

  .title-text {
  font-size: 90px;
  font-weight: bold;
  color: white;
}
  
  .logo-container {
    position: absolute;
    top: 0;
    right: 0;
  }
  
  .logo {
    width: 190px;
    height: auto;
  }
  
  .movie-list-container {
    position: relative; /* 상대 위치 설정 */
  }
  
  .movie-list {
    display: flex;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
  }
  
  .movie-item {
    margin-right: 10px;
  }
  
  .movie-item img {
    width: 200px;
  }
  </style>