import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import avvvatar from  'vue-avvvatars'

import {firebaseApp,firestore} from './firebase'

const app = createApp(App)
app.use(store)
app.use(router)
app.use(avvvatar)

app.use(firebaseApp)
app.use(firestore)
app.mount('#app')
