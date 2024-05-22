<template>
    <div class="back-container">
      <div class="black-squre"></div>
        <div class="gray-squre">
          <div class="main-container">
            <div class="profile-image-info">
              <span><img src="@/assets/Profile_image.jpg" class="profile-image" alt="profile_image"></span>
              <span class="profile-info" v-if="user && wishlist">
                <h1 class="profile-username">{{ user.username }}</h1>
                <div class="profile-email">
                  <div>E-mail : {{ user.email }}</div>
                  <div>최근접속 : {{ formatDate }}</div>
                </div>
              </span>
              <span><img src="@/assets/Logo_black.png" alt="logo_image" class="logo-image"></span>
            </div>
            <div class="page-container">
              <div class="trophy-display" v-if="userTrophys && user">
                <div class="trophy-card"  v-for="userTrophy in userTrophys">
                  <div class="trophy-info">
                    <div class="trophy-icon">
                      <img src="@/assets/Star_image.png" alt="star_icon" class="star-icon">
                    </div>
                    <div class="trophy-description"><span class="trophy-name">{{ user.username }}</span>님은</div>
                    <div class="trophy-title">{{ userTrophy }}</div>
                    <div class="trophy-description">의 리뷰왕으로 선정되셨습니다!</div>
                  </div>
                </div>
              </div>
              <div class="trophy-display" v-if="userTrophys === null && user">
                <div class="trophy-card"  v-for="_ in 1">
                  <div class="trophy-info">
                    <div class="trophy-description"><span class="trophy-name">{{ user.username }}</span>님은</div>
                    <div class="trophy-title">받은 상이 없어요</div>
                    <div class="trophy-description" style="color:blue">8ㅅ8</div>
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
  position: relative;
  width: 100%;
  height: 100%;
}

.black-squre {
  position: fixed;
  top: 0;
  left: 0;
  width: 30%;
  height: 100%;
  background-color: #494949;
  z-index: 1;
}

.gray-squre {
  position: relative;
  width: 90%;
  height: calc(100% - 10%); /* 상하단 여백을 위해 전체 높이에서 10%를 뺌 */
  margin: 5% auto; /* 상하단 여백 5%씩, 좌우 중앙 정렬 */
  background-color: #D9D9D9;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 2;
  box-sizing: border-box;
}

.main-container {
  position: relative;
  width: 70%;
  padding: 5%;
  background-color: white;
  border-radius: 10px;
  z-index: 3;
  margin-top: 20px; /* 위쪽 여백 */
  margin-bottom: 20px; /* 아래쪽 여백 */
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
  .profile-email {
    margin-left: 50px
  }
  .profile-username {
    margin-left: 50px
  }
}


.logo-image {
  width: auto;
  height: 5vh;
}

@media (max-width: 1200px) {
  .logo-image {
    display: none;
  }
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

.trophy-icon {
  position: absolute;
  top: 0;
  left: 0;
  width: 20px;
  height: 20px;
}

.star-icon {
  width: 100%;
  height: 100%;
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
  font-weight: bold;
  margin: 10px 0;
  color: #333;
}

.trophy-description {
  font-size: 1em;
  color: #777;
}

.trophy-name {
  font-size: 1em;
  color: black;
  font-weight: bold;
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