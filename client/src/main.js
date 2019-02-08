
import Vue from 'vue'
import App from './App.vue'
import store from './store.js'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'

Vue.config.productionTip = false
Vue.use(Vuetify, {
    iconfont:'fa'
})

new Vue({
    store,
    render: h => h(App),
}).$mount('#app')

 