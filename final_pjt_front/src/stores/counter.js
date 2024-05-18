import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'
import { useToast } from 'vue-toastification'

export const useCounterStore = defineStore('counter', () => {
  const token = ref(null)
  const router = useRouter()
  const toast = useToast()
  
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
        toast.error("인증 정보가 정확하지 않습니다. 다시 시도해주세요.")
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
  return { login, token, signUp }
})
