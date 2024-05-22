<template>
    <div class="container-in">
      <div class="DetailMovie" v-if="movie">
        <img :src="movie.poster_image" alt="poster_image" class="poster-image">
        <h1 class="movie-title">{{ movie.title }}</h1>
        <span class="movie-rating">{{ movie.release_date }}</span>
        <span class="movie-rating">| &#9733; {{ movie.rating }}</span>
        <span class="movie-certification">| 관람등급 : {{ movie.certification }}</span>
        <p class="movie-overview">{{ movie.overview }}</p>
        <button class="btn-trailer" @click="openYoutube">
            <img src="@/assets/Youtube.png" alt="Trailer Icon" class="button-icon">
          예고편 보러가기
        </button>
        <button class="btn-wishlist" @click="store.addWishList(movie.id)">
            <img src="@/assets/WishList.png" alt="Trailer Icon" class="button-icon">
            위시리스트 추가
        </button>
        <button class="btn-wishlist" @click="store.goCommunityNav()">
            <img src="@/assets/Review.png" alt="Trailer Icon" class="button-icon">
            게시판 이동
        </button>
        <button class="btn-wishlist" @click="goBack">
            <img src="@/assets/Back.png" alt="Trailer Icon" class="button-icon">
            뒤로 가기
        </button>
      </div>
      <div v-else>
        <p>Loading...</p>
      </div>
    </div>
  </template>
  
  <script setup>
  import axios from 'axios'
  import { ref, onMounted } from 'vue';
  import { useRoute,useRouter } from 'vue-router';
  import { useCounterStore } from '@/stores/counter';
  
  const route = useRoute()
  const router = useRouter()
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
  const goBack = () => {
    router.go(-1)
    }
  </script>
  
  <style scoped>
  .container-in {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 0;
    width: 100%;
    height: 100vh; /* Viewport height to cover the full screen */
    background-color: black;
  }
  
  .DetailMovie {
    width: 80%;
    max-width: 800px;
    padding: 20px;
    background-color: white;
    border-radius: 15px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    text-align: center;
  }
  
  .poster-image {
    width: 100%;
    max-width: 300px;
    height: auto;
    border-radius: 10px;
    margin-bottom: 20px;
  }
  
  .movie-title {
    font-size: 2em;
    font-weight: bold;
    margin-bottom: 10px;
  }
  
  .movie-overview {
  font-size: 1em;
  color: #555;
  margin-top: 20px;
  margin-bottom: 20px;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 5; /* number of lines to show */
  overflow: hidden;
  text-overflow: ellipsis;
}
  
  .movie-rating,
  .movie-certification {
    margin-left: 0.5vw;
    font-size: 1.3em;
    margin-bottom: 10px;
  }
  
  h2 {
    font-size: 1.5em;
    margin-top: 20px;
    margin-bottom: 10px;
  }
  
  .btn-trailer,
  .btn-wishlist {
    display: inline-block;
    padding: 10px 25px;
    font-size: 1em;
    margin: 10px 5px;
    color: black;
    background-color: white;
    border: 2px solid black;
    border-radius: 15px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
.btn-trailer:hover,
.btn-wishlist:hover {
  background-color: white;
  border: 2px solid black; /* 두꺼운 검은색 선 */
  border-radius: 15px; /* 둥근 테두리 */
  color: black; /* 글씨 색을 흰색으로 */
}

.button-icon {
  width: 25px; /* 이미지 크기 조정 */
  height: 25px;
  margin-right: 4px; /* 텍스트와 아이콘 사이 간격 */
}
  </style>