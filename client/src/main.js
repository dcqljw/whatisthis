import Vue from 'vue'
import './plugins/axios'
import App from './App.vue'
import router from './router'
import './plugins/element.js'
import axios from "axios";

let api = window.server.SERVER_API
console.log(api)
axios.defaults.baseURL = api
Vue.config.productionTip = false

new Vue({
    router,
    render: h => h(App)
}).$mount('#app')
