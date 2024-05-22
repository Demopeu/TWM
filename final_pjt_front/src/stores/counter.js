import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter, useRoute } from 'vue-router'
import axios from 'axios'
import { useToast } from 'vue-toastification'

export const useCounterStore = defineStore('counter', () => {
  const token = ref(null)
  const router = useRouter()
  const toast = useToast()
  const articles = ref()
  const userId = ref()


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
        fetchUserProfile()
      })
      .catch(error => {
        toast.error("인증 정보가 정확하지 않습니다. 다시 시도해주세요.")
      })
  }

  const fetchUserProfile = function() {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/accounts/user/',
      headers: {
        'Authorization': `Token ${token.value}`
      }
    })
    .then(response => {
      userId.value = response.data.pk
      console.log(response.data)
    })
    .catch(error => {
      console.log(error);
    });
  }
  
  const logout = function() {
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/accounts/logout/',
      headers: {
        'Authorization': `Token ${token.value}`,
      }
    })
      .then(response => {
        localStorage.removeItem('auth_token')
        token.value = null
        userId.value = null
        router.push({ name:'login' })
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
  const goProfileNav = (realuserId = userId.value) => {
    console.log(userId.value)
    console.log(realuserId)
    router.push({ name: 'ProfileView', params: { userId: realuserId } });
  }
  
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
        toast.success('위시리스트에 담겼습니다')
    })
    .catch((error) => {
        console.log('이미 위시리스트에 담겨있습니다.')
        toast.error('이미 위시리스트에 담겨있습니다.')
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
      toast.error('제목,나라 혹은 내용이 없습니다. 다시 시도해주세요.')
    })
  }

  const createComment = function (payload) {
    const content = payload.comment
    const articleId = payload.articleId
    const userId = payload.userId
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/community/articles/${articleId}/comments/`,
      headers: {
        Authorization: `Token ${token.value}`
      },
      data: {
        user_id: userId,
        article_id: articleId,
        content: content
      }
    })
    .then(response => {
      console.log('댓글이 등록되었습니다.')
    })
    .catch(error => {
      console.log(error)
    })
  }

  const deleteComment = function (commentId) {
    axios({
      method: 'delete',
      url: `http://127.0.0.1:8000/community/comments/${commentId}/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then(response => {
      console.log('댓글이 삭제되었습니다.')
    })
    .catch(error => {
      console.log(error)
    })
  }

  const likeButton = function (articleId) {
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/community/articles/${articleId}/like/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
   .then(response => {
     console.log('좋아요를 눌렀습니다.')
   })
   .catch(error => {
     console.log(error)
   })
  }
  
  const isLogin = computed(()=>{
    if (token.value===null) {
    return false}
    else {
    return true}
  })

  const addWatchedMovie = function(movieId) {
    return axios({
      method: 'post',
      url: `http://127.0.0.1:8000/movies/${movieId}/add_to_watched/`,
      headers: {
        Authorization: `Token ${token.value}`
      },
      data: {
        movie_id: movieId
      }
    })
    .then(response => {
      console.log('전달 완료');
    })
    .catch(error => {
      console.log(error);
    })
  }

  const deleteArticle = function(articleId) {
    if (confirm("정말로 삭제하시겠습니까?")) {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/community/articles/${articleId}/`,
        headers: {
          Authorization: `Token ${token.value}`
        }
      })
     .then(response => {
      router.push({ name: 'community'})
     })
     .catch(error => {
        console.log(error)
      })
    } else {
      console.log('삭제 취소')
    }
  }

  const updateArticle = function(articleId, payload) {
    axios({
        method: 'put',
        url: `http://127.0.0.1:8000/community/articles/${articleId}/`,
        headers: {
          Authorization: `Token ${token.value}`,
          'Content-Type': 'application/json'
        },
        data: payload
      })
     .then(response => {
        router.push({ name: 'community'})
      })
     .catch(error => {
        console.log(error)
      })
    }

  

  return { articles, updateArticle, addWatchedMovie, deleteArticle, fetchUserProfile, likeButton, deleteComment, createArticle, createComment, logout, login, addWishList, getArticles, token, movies, signUp, goRecommendedMovie,goCommunityNav,goIndexNav,goProfileNav,isLogin }
}, { persist: true })