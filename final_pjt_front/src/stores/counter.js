import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const token = ref(null)
  const router = useRouter()
  const articles = ref([
    { 
      id: 1,
      title: '제목1',
      content: '내용1'
    },
    { 
      id: 2,
      title: '제목2',
      content: '내용2'
    },
    {
      id: 3,
      title: '제목3',
      content: '내용3'
    }
  ])
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
  return { articles, login, token }
})
