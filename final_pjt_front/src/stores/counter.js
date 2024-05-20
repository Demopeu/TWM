import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter, useRoute } from 'vue-router'
import axios from 'axios'
import { useToast } from 'vue-toastification'

export const useCounterStore = defineStore('counter', () => {
  const token = ref(null)
  const router = useRouter()
  const toast = useToast()
  const articles = ref([])

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
        token.value = response.data.key
        router.push({ name:'selectcountry' })
      })
      .catch(error => {
        toast.error("인증 정보가 정확하지 않습니다. 다시 시도해주세요.")
      })
  }
  
  const logout = function() {
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/accounts/logout/',
      headers: {
        'Authorization': `Token ${token.value}`,
      }
      .then(response => {
        localStorage.removeItem('auth_token')
        token.value = null
        router.push({ name:'login' })
      })
      .catch(error => {
        console.log(error)
      })
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
        router.push({ name:'login' })
      })
     .catch(error => {
      console.log(error.response.data)
      const error_message = ref([])
      for (const key in error.response.data) {
        error_message.value.push(...error.response.data[key])
      }
      toast.error(error_message.value.join('\n'))
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
  const goCommunityNav = () => {router.push({ name: 'community' })}
  const goIndexNav = () => {router.push({ name: 'login' })}
  // 임시
  const goProfileNav = () => {router.push({ name: 'community' })}
  
    const addWishList = (movieId) => {
    console.log(token.value)
    axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movies/${movieId}/add_to_wishlist/`,
        headers: {
          Authorization: `Token ${token.value}`
        },
        data: {
          movie: movieId
        }   
    })
    .then((response) => {
        console.log('위시리스트에 담겼습니다')
    })
    .catch((error) => {
        console.log('이미 위시리스트에 담겨있습니다.')
        console.log(error)
    })
  }

  const getArticles = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/community/articles/',
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then((response) => {
      articles.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
  }

  const createArticle = function (payload) {
    const title = payload.title
    const content = payload.content
    const country = payload.country
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/community/articles/',
      headers: {
        Authorization: `Token ${token.value}`
      },
      data: {
        title: title,
        content: content,
        country: country
      }
    })
    .then((response) => {
      router.push({ name: 'community'})
    })
    .catch((error) => {
      console.log(error)
    })
  }

  return { articles, createArticle, logout, login, addWishList, getArticles, token, movies, signUp, goRecommendedMovie,goCommunityNav,goIndexNav,goProfileNav }
}, { persist: true })

