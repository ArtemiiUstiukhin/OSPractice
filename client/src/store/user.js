export default{
    state:{
        userId:'111',
        login:'qwerty',
        password:'qwerty'
    },
    mutation:{
        set_group(state,payload){
            state.groups = payload
        },
        change_show(group){
            group.isShow = !group.isShow
    }
    
    },
    actions:{
        signin(context){
            context.commit('change_show')
        }
    }
    
}
