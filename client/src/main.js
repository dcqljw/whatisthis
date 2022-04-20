import Vue from 'vue'
import './plugins/axios'
import App from './App.vue'
import router from './router'
import './plugins/element.js'
import axios from "axios";

let api = require("../public/ServerApiConfig.json")
console.log(api)
axios.defaults.baseURL = api.API_DOMAIN
Vue.config.productionTip = false

new Vue({
    router,
    render: h => h(App)
}).$mount('#app')
