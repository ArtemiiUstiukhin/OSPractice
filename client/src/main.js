
import Vue from 'vue'
import App from './App.vue'
import store from './store.js'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import YmapPlugin from 'vue-yandex-maps'
import VueSlimScroll from 'vue-slimscroll'


Vue.config.productionTip = false
Vue.use(Vuetify, {
    iconfont:'fa'
})
Vue.use(YmapPlugin)
Vue.use(VueSlimScroll)
new Vue({
    store,
    render: h => h(App),
}).$mount('#app')

 
