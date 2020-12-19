// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import { BImg } from 'bootstrap-vue'
import { BCarousel } from 'bootstrap-vue'
import App from './App'
import vueRouter from 'vue-router'




import router from './router'
Vue.use(vueRouter)
Vue.use(BootstrapVue)
Vue.component('b-img', BImg)
Vue.component('b-carousel', BCarousel)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  router,
  el: '#app',
  components: { App },
  template: '<App/>'
})
