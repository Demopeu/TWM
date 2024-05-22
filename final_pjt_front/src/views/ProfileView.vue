<template>
    <div class="back-container">
      <div class="black-squre"></div>
        <div class="gray-squre">
          <div class="main-container">
            <div class="profile-image-info">
              <span v-if="profileImage"><img class="profile-image" alt="profile_image" :src=profileImage></span>
              <span class="profile-info" v-if="user && wishlist">
                <h2 class="profile-username">{{ user.username }}</h2>
                <hr>
                <div class="profile-email">
                  <div class="email-info">
                    <span class="email-label">E-mail:</span>
                    <span class="email-text">{{ user.email }}</span>
                  </div>
                  <div class="last-login-info">
                    <span class="last-login-label">최근 접속:</span>
                    <span class="last-login-text">{{ formatDate }}</span>
                  </div>
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
            
            <div class="section-container">
              <div class="section-title">
                위시리스트 영화 목록
              </div>
              <div class="tooltip-container">
                <button class="tooltip-icon" @click="openModal">
                  <span class="button-text">?</span>
                </button>
              </div>
            </div>
            <div class="modal" v-if="modalOpen" @click.self="closeModal">
              <div class="modal-content">
                <span class="close" @click="closeModal">&times;</span>
                <p style="font-weight:bold; text-align: center;">
                  담겨진 영화를 클릭해보세요!
                  <br>
                  <br>
                  본 영화 목록을 수정할 수 있어요!
                </p>
              </div>
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
import image1 from '@/assets/profile/image1.jpg';
import image2 from '@/assets/profile/image2.jpg';
import image3 from '@/assets/profile/image3.jpg';
import image4 from '@/assets/profile/image4.jpg';
import image5 from '@/assets/profile/image5.jpg';
import image6 from '@/assets/profile/image6.jpg';
import image7 from '@/assets/profile/image7.jpg';
import image8 from '@/assets/profile/image8.jpg';
import image9 from '@/assets/profile/image9.jpg';
import image10 from '@/assets/profile/image10.jpg';

const route = useRoute();
const user = ref(null)
const userTrophys = ref(null)
const wishlist = ref(null)
const store = useCounterStore();
const formatDate = ref(null)
const profileImage = ref(null)

const formattedDate = function (date) {
  formatDate.value = date.substring(0, 10);
}

const imageList = [
  image1,
  image2,
  image3,
  image4,
  image5,
  image6,
  image7,
  image8,
  image9,
  image10,

];
const setRandomProfileImage = async () => {
      const randomIndex = Math.floor(Math.random() * imageList.length);
      const randomImage = imageList[randomIndex];
      profileImage.value = randomImage;
    };
onMounted(() => {
  setRandomProfileImage()
})

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

const modalOpen = ref(false);

const openModal = () => {
  modalOpen.value = true;
}

const closeModal = () => {
  modalOpen.value = false;
}

</script>

<style scoped>
.section-container {
  display: flex;
  align-items: center;
}

.tooltip-container {
  margin-left: 10px; /* 버튼과 목록 사이의 간격 조절 */
}

.tooltip-icon {
  background-color: #4CAF50; /* 버튼 배경색 */
  border: none;
  color: white; /* 버튼 텍스트 색상 */
  padding: 4px 9px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 10px; /* 버튼 텍스트 크기 */
  border-radius: 100%; /* 버튼 모서리 둥글게 */
  cursor: pointer;
}

.button-text {
  font-size: 11px; /* 버튼 내 텍스트 크기 */
}

.tooltip-icon:hover {
  background-color: #45a049; /* 마우스를 올렸을 때 배경색 변경 */
}

.modal {
  display: flex;
  align-items: center;
  justify-content: center;
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.4);
}

.modal-content {
  background-color: #fefefe;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
  width: 80%; /* 모달의 너비를 조절합니다. */
  max-width: 400px; /* 모달의 최대 너비를 설정합니다. */
}

.close {
  position: absolute;
  top: 10px;
  right: 10px;
  color: #aaa;
  font-size: 24px;
  cursor: pointer;
}

.close:hover {
  color: black;
}

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
  width: 100%;
  height: 100%; /* 상하단 여백을 위해 전체 높이에서 10%를 뺌 */
  background: linear-gradient(135deg, #ff9999, #66ccff); /* 그라데이션 색상 설정 */
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 2;
  box-sizing: border-box;
}

.main-container {
  position: relative;
  width: 80%;
  padding: 5%;
  background-color: rgba(255, 255, 255, 0.836);
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
  margin-bottom: 3vh;
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

.profile-email {
  display: flex;
  flex-direction: column;
  margin-top: 10px;
}

.email-info, .last-login-info {
  display: flex;
  align-items: center;
  margin-bottom: 5px;
}

.email-label, .last-login-label {
  font-weight: bold;
  margin-right: 5px;
}

.email-text, .last-login-text {
  color: #555;
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
  border: 2px solid #ddd; /* 테두리 두께와 색상 설정 */
  border-radius: 15px; /* 테두리의 모서리를 둥글게 만듭니다. */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 그림자 효과 추가 */
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