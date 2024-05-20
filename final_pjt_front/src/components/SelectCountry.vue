<template>
    <div class="container-inner">
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark ">
            <img class="img-logo" src="@/assets/Logo_white.png" alt="Logo_black.png" @click="goidnav">
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav d-flex ms-auto">
            <li class="nav-item">
                <button @click="gocomunav" class="btn btn-outline-light" style="border: black;">게시판</button>
            </li>
            <li class="nav-item">
                <button @click="gopronav" class="btn btn-outline-light" style="border: black;">프로필</button>
            </li>
            <li class="nav-item">
                <button @click="" class="btn btn-outline-light" style="border: black;">로그아웃</button>
            </li>
            </ul>
          </div>
        </nav>
        <div @click="handleClick" ref="centeredElement " class="centered-element-north">
            <button value="north_america">N.America</button>
        </div>
        <div @click="handleClick" ref="centeredElement " class="centered-element-sorth">
            <button value="south_america">S.America</button>
        </div>
        <div @click="handleClick" ref="centeredElement " class="centered-element-europe">
            <button value="europe">Europe</button>
        </div>
        <div @click="handleClick" ref="centeredElement " class="centered-element-india">
            <button value="india">India</button>
        </div>
        <div @click="handleClick" ref="centeredElement " class="centered-element-China">
            <button value="china">China</button>
        </div>
        <div @click="handleClick" ref="centeredElement " class="centered-element-Korea">
            <button value="korea">Korea</button>
        </div>
        <div @click="handleClick" ref="centeredElement " class="centered-element-Japan">
            <button value="japan">Japan</button>
        </div>

    </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { RouterLink, RouterView } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

const router = useRouter()
const centeredElement = ref(null)
const store = useCounterStore()

const handleClick = function (event) {
    const button = event.target
    if (button.tagName === 'BUTTON') {
        const region = button.value
        store.goRecommendedMovie(region)
    }
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})

const container = ref(null)

const handleScroll = () => {
    if (centeredElement.value && container.value) {
        const containerRect = container.value.getBoundingClientRect()
        const containerTop = containerRect.top
        centeredElement.value.style.position = 'absolute'
        centeredElement.value.style.top = `${containerTop}px`
    }

}
const goidnav = ()=>{
    store.goIndexNav()
}
const gocomunav = ()=>{
    store.goCommunityNav()
}
const gopronav = ()=>{
    store.goProfileNav()
}


</script>

<style scoped>
.container-inner{
    position: relative;
    width: 100%;
    height: 100vh;
}

.centered-element-north{
  position: absolute;
  left: 20%;
  top: 250px;
  transform: translateX(-50%);
  width: 100px;
  height: 50px;
}
.centered-element-north button{
    text-overflow: ellipsis;
    width: 100px;
    height: 50px;

    border: 5px solid #FF7070;
    border-radius: 30px; 
    background-color: white;
    color: black;
    white-space: nowrap;
    font-weight: bold;
}

.centered-element-sorth{
  position: absolute;
  left: 33%;
  top: 500px;
  transform: translateX(-50%);
  width: 100px;
  height: 50px;
}
.centered-element-sorth button{
    text-overflow: ellipsis;
    width: 100px;
    height: 50px;

    border: 5px solid #FFEF5E;
    border-radius: 30px; 
    background-color: white;
    color: black;
    white-space: nowrap;
    font-weight: bold;
}

.centered-element-europe{
  position: absolute;
  left: 55%;
  top: 240px;
  transform: translateX(-50%);
  width: 100px;
  height: 50px;
}
.centered-element-europe button{
    text-overflow: ellipsis;
    width: 100px;
    height: 50px;

    border: 5px solid #BDE5C1;
    border-radius: 30px; 
    background-color: white;
    color: black;
    white-space: nowrap;
    font-weight: bold;
}

.centered-element-india{
  position: absolute;
  left: 70%;
  top: 370px;
  transform: translateX(-50%);
  width: 100px;
  height: 50px;
}
.centered-element-india button{
    text-overflow: ellipsis;
    width: 100px;
    height: 50px;

    border: 5px solid #7B88FB;
    border-radius: 30px; 
    background-color: white;
    color: black;
    white-space: nowrap;
    font-weight: bold;
}
.centered-element-China{
  position: absolute;
  left: 77%;
  top: 330px;
  transform: translateX(-50%);
  width: 100px;
  height: 50px;
}
.centered-element-China button{
    text-overflow: ellipsis;
    width: 100px;
    height: 50px;

    border: 5px solid #CAA9FF;
    border-radius: 30px; 
    background-color: white;
    color: black;
    white-space: nowrap;
    font-weight: bold;
}
.centered-element-Korea{
  position: absolute;
  left: 82%;
  top: 280px;
  transform: translateX(-50%);
  width: 100px;
  height: 50px;
}
.centered-element-Korea button{
    text-overflow: ellipsis;
    width: 100px;
    height: 50px;

    border: 5px solid #F69DE3;
    border-radius: 30px; 
    background-color: white;
    color: black;
    white-space: nowrap;
    font-weight: bold;
}
.centered-element-Japan {
  position: absolute;
  left: 87%;
  top: 370px;
  transform: translateX(-50%);
  width: 100px;
  height: 50px;
}
.centered-element-Japan button{
    text-overflow: ellipsis;
    width: 100px;
    height: 50px;

    border: 5px solid #FF3131;
    border-radius: 30px; 
    background-color: white;
    color: black;
    white-space: nowrap;
    font-weight: bold;
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