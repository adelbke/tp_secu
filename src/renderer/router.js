import Vue from 'vue'
import VueRouter from 'vue-router'

// import route components
import encrypt from './pages/encrypt.vue'
import decrypt from './pages/decrypt.vue'
import comms from './pages/comms.vue'
Vue.use(VueRouter)

const routes = [
  { path: '/encrypt', component: encrypt },
  { path: '/decrypt', component: decrypt },
  { path: '/comms', component: comms },
  { path: '*', component: encrypt }

]

const router = new VueRouter({
  routes // short for `routes: routes`
})

export default router
