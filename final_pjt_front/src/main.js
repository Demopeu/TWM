import { createApp } from 'vue'
import { createPinia } from 'pinia'
import 'bootstrap/dist/css/bootstrap.css'
import "vue-toastification/dist/index.css"
import Toast, { POSITION } from "vue-toastification"

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(Toast, {
    position: POSITION.TOP_MIDDLE,
  })

app.mount('#app')
