import { createRouter, createWebHistory } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import { useToast } from 'vue-toastification'
import IndexView from '@/views/IndexView.vue'
import Login from '@/components/Login.vue'
import SignUp from '@/components/SignUp.vue'
import SelectCountry from '@/components/SelectCountry.vue'
import CommunityView from '@/views/CommunityView.vue'
import MovieView from '@/views/MovieView.vue'
import RecommendMovies from '@/components/RecommendMovies.vue'
import RecommendMoviesDetail from '@/components/RecommendMoviesDetail.vue'
import ArticleList from '@/components/ArticleList.vue'
import DetailView from '@/views/DetailView.vue'
import CreateView from '@/views/CreateView.vue'
import ProfileView from '@/views/ProfileView.vue'

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
      component: CommunityView,
      children:[
        {
          path: '/community',
          name: 'ArticleList',
          component: ArticleList,
        },
      ]
    },
    {
      path: '/community/:articleId',
      name: 'DetailView',
      component: DetailView,
    },
    {
      path: '/movies',
      name: 'movies',
      component: MovieView,
      children:[
        {
          path: '/movies/:country',
          name: 'RecommendMovies',
          component: RecommendMovies,
        },
        {
          path: '/movies/:country/:id',
          name: 'MovieDetail',
          component: RecommendMoviesDetail,
        },
      ]
    },
    {
      path: '/community/create',
      name: 'CreateView',
      component: CreateView,
    },
    {
      path: '/profile/:userId',
      name: 'ProfileView',
      component: ProfileView,
    }
  ]
})

router.beforeEach((to,from)=>{
 const store = useCounterStore()
 const toast = useToast()

 if (to.name !== 'login' && to.name !== 'signup' && to.name !== 'mainpage' && store.token===null) {
    toast.error("로그인이 필요합니다.")
    return {name: 'login'}
  }
})
export default router
