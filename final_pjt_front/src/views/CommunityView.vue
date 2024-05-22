<template>
  <div class="container min-vw-100 min-vh-100" >
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
    <ArticleList />
  </div>
</template>

<script setup>
import ArticleList from '@/components/ArticleList.vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'

const router = useRouter()
const store = useCounterStore()

const goidnav = ()=>{
    store.goIndexNav()
}
const gocomunav = ()=>{
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
  width: 100vw;
  padding: 0;
}

.img-logo {
  
  width: 190px;
  height: 70px;
  padding: 0;
}
</style>