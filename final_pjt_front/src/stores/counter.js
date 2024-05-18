import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter, useRoute } from 'vue-router'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const token = ref(null)
  const router = useRouter()
  const login = function(payload) {
    const username = payload.username
    const password = payload.password
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/accounts/login/',
      data: {
        username: username,
        password: password
      }
    })
      .then(response => {
        router.push({ name:'selectcountry' })
      })
      .catch(error => {
        console.log(error)
      })
  }

  const signUp = function(payload) {
    const username = payload.username
    const password1 =  payload.password1
    const password2 =  payload.password2
    const email =  payload.email
    const trophys =  payload.trophys
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/accounts/signup/',
      data: {
        username: username,
        password1: password1,
        password2: password2,
        email: email,
        trophys: trophys
      }
    })
     .then(response => {
        router.push({ name:'selectcountry' })
      })
     .catch(error => {
        console.log(error.response.data)
      })
  }

  const movies = ref([])
  const goRecommendedMovie = function (region) {
    const country = region
    axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/recommend/${country}/`,
    })
    .then(response => {
        movies.value = response.data
        router.push({ name: 'RecommendMovies', params: {country: country} })
    })
    .catch(error => {
        console.log(error)
    })
  }

  return { login, token, movies, signUp, goRecommendedMovie }
})
