import { createRouter, createWebHistory } from 'vue-router'
import IndexView from '@/views/IndexView.vue'
import Login from '@/components/Login.vue'
import Signup from '@/components/SignUp.vue'
import Selectcontry from '@/components/SelectContry.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'index',
      component: IndexView,
      children:[
        {
          path: '/',
          name: 'login',
          component: Login,
        },
        {
          path: '/signup',
          name: 'signup',
          component: Signup
        },
        {
          path: '/selectcontry',
          name:'selectcontry',
          component: Selectcontry,
        }
      ]
    },
  ]
})

export default router
