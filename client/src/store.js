import Vue from 'vue'
import Vuex from 'vuex'
import navigationModule from'./store/navigation'
import userModule from './store/user'

Vue.use(Vuex)

export default new Vuex.Store({
    modules:{
        navigationModule,
        userModule
    }
})