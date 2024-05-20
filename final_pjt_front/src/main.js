import { createApp } from 'vue'
import { createPinia } from 'pinia'
import 'bootstrap/dist/css/bootstrap.css'
import "vue-toastification/dist/index.css"
import Toast, { POSITION } from "vue-toastification"
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'


import App from './App.vue'
import router from '@/router'

const app = createApp(App)
const pinia = createPinia()

pinia.use(piniaPluginPersistedstate)

app.use(pinia)
app.use(router)
app.use(Toast, {
    position: POSITION.TOP_MIDDLE,
  })

app.mount('#app')
