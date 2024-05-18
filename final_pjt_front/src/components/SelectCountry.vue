<template>
    <div class="container-inner">
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
            <button value="south_america">Korea</button>
        </div>
        <div @click="handleClick" ref="centeredElement " class="centered-element-Japan">
            <button value="south_america">Japan</button>
        </div>

    </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const centeredElement = ref(null)

const handleClick = function (event) {
    const button = event.target
    if (button.tagName === 'BUTTON') {
        const region = button.value
        goRecommendedMovie(region)
    }
}

const goRecommendedMovie = function (region) {
    const country = region

    axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/recommend/${country}/`,
    })
    .then(response => {
        console.log('데이터 받기 성공!')
        console.log(response.data)
    })
    .catch(error => {
        console.log(error)
    })
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

        // 요소가 현재 보이는 페이지의 절대 위치에 고정됩니다.
        centeredElement.value.style.position = 'absolute'
        centeredElement.value.style.top = `${containerTop}px`
    }

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
  left: 25%;
  top: 250px;
  transform: translateX(-50%);
  width: 100px;
  height: 50px;
}
.centered-element-north button{
    text-overflow: ellipsis;
    width: 100px;
    height: 50px;
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
}
.centered-element-China{
  position: absolute;
  left: 77%;
  top: 200px;
  transform: translateX(-50%);
  width: 100px;
  height: 50px;
}
.centered-element-China button{
    text-overflow: ellipsis;
    width: 100px;
    height: 50px;
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
}
.centered-element-Japan {
  position: absolute;
  left: 92%;
  top: 330px;
  transform: translateX(-50%);
  width: 100px;
  height: 50px;
}
.centered-element-Japan button{
    text-overflow: ellipsis;
    width: 100px;
    height: 50px;
}
</style>