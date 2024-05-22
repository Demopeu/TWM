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
      <div class="movie-list-container swiper-container" ref="scrollContainer">
      <div class="movie-list swiper-wrapper">
        <div v-for="movie in store.movies" :key="movie.id" class="movie-item swiper-slide">
          <div class="movie-item-inner" @click="goToMovieDetail(movie.id)">
            <img :src="movie.poster_image" alt="poster_image">
          </div>
        </div>
      </div>
    </div>
    <div class="btn-box">
      <button class="btn-else" @click="goSelectCountry">나라 선택</button>
      <button class="btn-else" @click="gocomunav">게시판 이동</button>
    </div>
    </div>
  </template>
  
  <script setup>
  import { useCounterStore } from '@/stores/counter'
  import { useRoute, RouterLink,useRouter } from 'vue-router'
  import { ref,onMounted } from 'vue'
  import Swiper from 'swiper/bundle'
  
  const store = useCounterStore()
  const route = useRoute()
  const name = route.params.country
  const router = useRouter()

  onMounted(() => {
  new Swiper('.movie-list-container', {
    slidesPerView: 'auto',
    spaceBetween: 10,
    freeMode: true,
    grabCursor: true,
    scrollbar: {
      el: '.swiper-scrollbar',
      hide: false,
    },
  });
})

const goToMovieDetail = (movieId) => {
  router.push({ name: 'MovieDetail', params: { id: movieId } })
}

const goSelectCountry = () => {
  router.push({ name: 'selectcountry' })
}
const gocomunav = ()=>{
    store.goCommunityNav()
}
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
    position: relative;
  }
  
  .movie-list {
    display: flex;
    /* overflow-x: auto; */
    /* -webkit-overflow-scrolling: touch; */
  }
  
  .movie-item {
    margin-right: 10px;
  }
  
  .movie-item img {
    width: 200px;
  }

  .btn-box{
    display: flex;
    flex-direction: row;
    justify-content: center;
    margin-top: 5vh;
    margin-bottom: 5h;
  }


.btn-else {
  display: inline-block;
  padding: 10px 25px;
  font-size: 1.2em;
  margin: 10px 5px;
  color: white;
  background: rgba(255, 255, 255, 0.1);
  border: 3px solid rgba(255, 255, 255, 0.2);
  border-radius: 15px;
  backdrop-filter: blur(10px);
  cursor: pointer;
  transition: background 0.3s, transform 0.3s;
}

.btn-else:hover {
  background: rgba(255, 255, 255, 0.2);
  transform: scale(1.05);
}
  </style>