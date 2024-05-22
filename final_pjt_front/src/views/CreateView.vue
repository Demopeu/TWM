<template>
  <div class="container min-vw-100 min-vh-100">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark ">
            <img class="img-logo" src="@/assets/Logo_white.png" alt="Logo_black.png">
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav d-flex ms-auto">
            <li class="nav-item">
                <button @click="gocomunav" class="btn btn-outline-light" style="border: black;">게시판</button>
            </li>
            <li class="nav-item">
                <button @click="gopronav()" class="btn btn-outline-light" style="border: black;">프로필</button>
            </li>
            <li class="nav-item">
                <button @click="logout" class="btn btn-outline-light" style="border: black;">로그아웃</button>
            </li>
            <li class="nav-item">
                <button @click="goback" class="btn btn-outline-light" style="border: black;">뒤로가기</button>
            </li>
            </ul>
          </div>
        </nav>
    <div class="articleList-box">
    <div class="articleList-List-box">
            <div class="articleList-List-box-in">
              <div class="left-box">
                <h1>나만의 리뷰</h1>
              <form @submit.prevent="createArticle" class="form-box">
                <input type="text" name="title" id="title" v-model.trim="title" class="title-box" placeholder="제목을 입력해주세요">
                <div class="button-box">
                  <div name="country" id="country-select">
                    <button type="button" :class="{'selected': country === 'north-america', 'country-button': true}" @click="setCountry('north-america')">North America</button>
                    <button type="button" :class="{'selected': country === 'south-america', 'country-button': true}" @click="setCountry('south-america')">South America</button>
                    <button type="button" :class="{'selected': country === 'europe', 'country-button': true}" @click="setCountry('europe')">Europe</button>
                    <button type="button" :class="{'selected': country === 'india', 'country-button': true}" @click="setCountry('india')">India</button>
                    <button type="button" :class="{'selected': country === 'korea', 'country-button': true}" @click="setCountry('korea')">Korea</button>
                    <button type="button" :class="{'selected': country === 'china', 'country-button': true}" @click="setCountry('china')">China</button>
                    <button type="button" :class="{'selected': country === 'japan', 'country-button': true}" @click="setCountry('japan')">Japan</button>
                  </div>
                </div>
                <!-- <select name="country" id="country-select" v-model.trim="country" class="title-box">
                  <option value="" selected disabled hidden>국가 혹은 대륙을 선택하세요.</option>
                  <option value="north-america">North America</option>
                  <option value="south-america">South America</option>
                  <option value="europe">Europe</option>
                  <option value="india">India</option>
                  <option value="korea">korea</option>
                  <option value="china">china</option>
                  <option value="japan">japan</option>
                </select> -->
                <textarea name="content" id="content" cols="30" rows="10" v-model.trim="content" class="textarea-box"></textarea>
                <div class="write-button-container">
                  <input type="submit" class="write-button" value="글쓰기">
                </div>
              </form>
              </div>
              <div class="right-box">
                <div class="ad-box"></div>
              </div>
            </div>
    </div>
  </div>
</div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter';
import { useRouter } from 'vue-router'
const title = ref(null)
const content = ref(null)
const country = ref(null)
const store = useCounterStore()
const router = useRouter()

const createArticle = function () {
  const payload = {
    title: title.value,
    content: content.value,
    country: country.value
  }
  store.createArticle(payload)
}

const setCountry = (value) => {
  country.value = value
}

const goidnav = ()=>{
    store.goIndexNav()
}
const gocomunav = ()=>{
    console.log('gocomunav 확인')
    store.goCommunityNav()
}
const gopronav = ()=>{
    store.goProfileNav()
}
const logout = ()=>{
  store.logout()
}
const goback =()=>{
  router.go(-1)
}
</script>

<style scoped>
.container {
  background-color: #E9FCE7;
  width: 100%;
  height: 100vh;
  overflow-y: auto;
  padding: 0;
}
.content-box{
  display: flex;
  justify-content: space-between;
}
.articleList-box{
  padding-top: 10vh;
  width: 80%;
  height: 100%-20px;
  margin-left: auto;
  margin-right: auto;
}
.articleList-List-box {
  background-color: #D9D9D9;
  width: 100%;
  min-width: 75vh;
  border-radius: 1vw;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.articleList-List-box-in{
  background-color: white;
  width: 95%;
  border-radius: 1vw;
  margin: 3% auto;
  min-height: 90%;
  display: flex;
  flex-direction: row;
}

.left-box{
  flex: 4;
}
.right-box {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
}

.ad-box {
  width: 80%;
  height: 80%;
  background-color: black;
}

.form-box{
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.title-box{
  width: 90%;
  margin-bottom: 1%;
  margin-left: 5%;
}
.button-box{
  width: 90%;
  margin-bottom: 1%;
  margin-left: 4.5%;
}

.navbar-brand {
  font-size: 1.5em;
}

.navbar-nav .nav-link {
  color: #fff !important;
  font-size: 1.2em;
  padding: 10px 20px;
}

.navbar-nav .nav-item {
  margin-left: 10px;
}

.navbar {
  width: auto;
  padding: 0;
}

.img-logo {
  
  width: 190px;
  height: 70px;
  padding: 0;
}

h1 {
  font-weight: bold;
    margin-left: 5%;
    margin-bottom: 2%;
    margin-top: 5vh;
    font-size: 50px;
    letter-spacing: -5px;
}

.country-button {
  padding: 10px 20px;
  font-size: 16px;
  margin: 5px;
  cursor: pointer;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: white;
}

.country-button.selected {
  background-color: #4e4eff;
  color: white;
}

.textarea-box {
  width: 90%;
  height: 700px;
  margin-top: 1%;
  margin-bottom: 1%;
  margin-left: 5%;
  resize: none; /* 크기 조절 불가 */
  overflow-y: auto; /* 내용이 많을 때 스크롤 */
}

.write-button-container {
  display: flex;
  justify-content: flex-start;
  width: 70%;
  margin-left: 4.7%;
  margin-bottom: 1%;
}

.write-button {
  background-color: #7979e9; /* Dark Blue */
  color: white;
  padding: 10px 20px;
  font-size: 18px;
  font-weight: bold;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  margin: 10px 0;
}
.write-button:hover {
  background-color: #4e4eff; /* Medium Blue for hover effect */
}
</style>