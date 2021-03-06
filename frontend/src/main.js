import Vue from 'vue'
import App from './App.vue'

import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

import VueRouter from 'vue-router'
import VueResource from 'vue-resource'

import routes from './router'

Vue.use(VueResource)
Vue.use(VueRouter)

const router = new VueRouter({
  routes: routes,
  mode: 'history'
})

// eslint-disable-next-line no-new
new Vue({
  el: '#app',
  render: h => h(App),
  router: router
})
