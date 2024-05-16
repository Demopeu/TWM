import { createRouter, createWebHistory } from 'vue-router'
import IndexView from '@/views/IndexView.vue'
import CommunityView from '@/views/CommunityView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'mainpage',
      component: IndexView
    },
    {
      path: '/community',
      name: 'community',
      component: CommunityView
    }
  ]
})

export default router
