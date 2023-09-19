import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import avvvatar from  'vue-avvvatars'
import Slideout from '@hyjiacan/vue-slideout'
import '@hyjiacan/vue-slideout/dist/slideout.css'
import {firebaseApp,firestore} from './firebase'

const app = createApp(App)
app.use(store)
app.use(router)
app.use(avvvatar)
app.use(Slideout)
app.use(firebaseApp)
app.use(firestore)
app.mount('#app')
