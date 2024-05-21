<template>
    <div class="back-container">
      <div class="flex-container">
        <div class="black-squre"></div>
        <div class="gray-squre">
          <div class="main-container">
            <div class="profile-image-info">
              <span><img src="@/assets/Profile_image.jpg" class="profile-image" alt="profile_image"></span>
              <span class="profile-info" v-if="user && wishlist">
                <h1 class="profile-username">{{ user.username }}</h1>
                <hr>
                <div class="profile-email">
                  <div>E-mail : {{ user.email }}</div>
                  <div>최근접속 : {{ formatDate }}</div>
                </div>
              </span>
              <span><img src="@/assets/Logo_black.png" alt="logo_image" class="logo-image"></span>
            </div>
            <hr>
            <div class="page-container">
              <div class="trophy-display" v-if="userTrophys">
                <div class="trophy-card"  v-for="userTrophy in userTrophys">
                  <div class="trophy-info">
                    <div class="trophy-title">{{ userTrophy }}</div>
                  </div>
                </div>
              </div>
            </div>
            <div class="section-title">
              위시리스트 영화 목록
            </div>
            <div v-if="wishlist" class="wishlist">
              <div v-for="movie in wishlist" :key="movie.id">
                <div v-if="!movie.is_watched">
                  <img :src="movie.movie_poster" alt="movie_poster" class="movie-poster" @click="addWatchedMovie(movie.movie_id)">
                </div>
              </div>
            </div>
            <div class="section-title">
              본 영화 목록
            </div>
            <div v-if="wishlist" class="wishlist">
              <div v-for="movie in wishlist" :key="movie.id">
                <div v-if="movie.is_watched">
                  <img :src="movie.movie_poster" alt="movie_poster" class="movie-poster" @click="addWatchedMovie(movie.movie_id)">
                </div>
              </div>
            </div>
            <div v-else>
              Loading ...
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { useCounterStore } from '@/stores/counter';

const route = useRoute();
const user = ref(null)
const userTrophys = ref(null)
const wishlist = ref(null)
const store = useCounterStore();
const formatDate = ref(null)

const formattedDate = function (date) {
  formatDate.value = date.substring(0, 10);
}

onMounted(() => {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/accounts/profile/${route.params.userId}`
  })
   .then(response => {
      user.value = response.data;
      console.log(user.value);
      if (response.data.trophys) {
        userTrophys.value = response.data.trophys.split(',').map(trophy => trophy.trim().replace(/^'|'$/g, ""));
      }
      formattedDate(user.value.date_joined)
    })
    .catch(error => {
      console.log(error);
    })
})

onMounted(() => {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/movies/${route.params.userId}/get_wishlist/`
  })
  .then((response) => {
      wishlist.value = response.data;
      console.log(wishlist.value)
  })
  .catch((error) => {
    console.log(error);
  })
})

const addWatchedMovie = (movieId) => {
  store.addWatchedMovie(movieId)
    .then((response) => {
      fetchWishlist()
    })
    .catch((error) => {
      console.log(error);
    })
}

const fetchWishlist = () => {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/movies/${route.params.userId}/get_wishlist/`
  })
  .then(response => {
      wishlist.value = response.data;
  })
  .catch(error => {
    console.log(error);
  })
}

</script>

<style scoped>
.back-container {
  width: 100%;
  height: 100%;
  position: fixed;
  top: 0;
  left: 0;
  overflow: auto;
}

.flex-container {
  display:flex;
  height: 100%;
  justify-content: center;
  align-items: center;
}

.black-squre {
  width: 30%;
  background-color: #494949;
}

.gray-squre {
  width: 70%;
  background-color: #D9D9D9;
  overflow-y: auto;
}
.main-container {
  width: 60%;
  padding: 5%;
  background-color: white;
  border-radius: 10px;
}

.profile-image-info {
  position: relative;
  display: flex;
  justify-content: space-between;
  width: 93%;
  height: 20vh;
  margin-top: 3vh;
  border-radius: 100%;
}

.profile-image {
  width: auto;
  height: 100%;
  border-radius: 100%;
  aspect-ratio: 1/1;
}

.profile-info {
  display:inline-block;
  width: auto;
  height: 40%;
  align-self: center;
}

@media (min-width: 1300px) {
  .profile-info {
    display: flex;
  }
}
@media (min-width: 1300px) {
  .profile-email {
    margin-left: 50px
  }
}


.logo-image {
  width: auto;
  height: 5vh;
}

.profile-username {
  font-weight: bold;
}

.page-container {
  width: 100%;
  padding: 20px;
  box-sizing: border-box;
  margin-bottom: 30px;
}

.trophy-display {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  width: 100%;
  background-color: #ffffff;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.trophy-card {
  background-color: #ffffff;
  border: 2px solid #e0e0e0;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  text-align: center;
  transition: transform 0.3s;
}

.trophy-card:hover {
  transform: translateY(-10px);
}

.trophy-info {
  padding: 15px;
}

.trophy-title {
  font-size: 1.5em;
  margin: 10px 0;
  color: #333;
}

.trophy-description {
  font-size: 1em;
  color: #777;
}

.movie-poster {
  width: auto;
  height: 13vh;
  margin: 1vh;
  border-radius: 10px;
}

.wishlist {
  display: flex;
  width: 90%;
  background-color: #f0f0f0;
  justify-content: center;
  border-radius: 10px;
  min-height: 13vh;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin: 20px 0;
  overflow: auto;
}

.section-title {
  font-size: 1.2rem;
  font-weight: bold;
  color: #333;
}

</style>