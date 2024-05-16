import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
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
  return { }
})
