import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'index',
        component: () => import('../views/Index.vue')
    }, {
        path: '/xby',
        name: 'article',
        component: () => import('../views/Article.vue')
    }
]

const router = new VueRouter({
    mode: "hash",
    routes
})

export default router
