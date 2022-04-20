import Vue from 'vue'
import './plugins/axios'
import App from './App.vue'
import router from './router'
import './plugins/element.js'
import axios from "axios";

let api = "https://api.dlxz.xyz"
// let api = "http://127.0.0.1:8000"
axios.defaults.baseURL = api
Vue.config.productionTip = false

new Vue({
    router,
    render: h => h(App)
}).$mount('#app')
