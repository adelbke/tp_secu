import Vue from 'vue'

import './assets/main.css'

import App from './App'
// router in case multiple pages are added
import router from './router'
// vuex store for communicating with python and managing state
import store from './store'

import VueToast from 'vue-toast-notification'
import 'vue-toast-notification/dist/theme-default.css'

Vue.use(VueToast)

if (!process.env.IS_WEB) Vue.use(require('vue-electron'))
Vue.config.productionTip = false

/* eslint-disable no-new */
window.vue = new Vue({
  components: { App },
  store,
  router,
  template: '<App/>'
}).$mount('#app')
