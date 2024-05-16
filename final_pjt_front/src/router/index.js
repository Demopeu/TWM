import { createRouter, createWebHistory } from 'vue-router'
import IndexView from '@/views/IndexView.vue'
import Login from '@/components/Login.vue'
import SignUp from '@/components/SignUp.vue'
import SelectCountry from '@/components/SelectCountry.vue'
import CommunityView from '@/views/CommunityView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'mainpage',
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
          component: SignUp
        },
        {
          path: '/selectcountry',
          name:'selectcountry',
          component: SelectCountry,
        }
      ]
    },
    {
      path: '/community',
      name: 'community',
      component: CommunityView
    }
  ]
})

export default router
