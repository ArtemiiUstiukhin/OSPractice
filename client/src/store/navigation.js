export default{
    state:{
       groups:[
           {id:'11qq1',
           name:'first',
            isShow:false,
           elements:[
                {
                id:'11221qq',
                name:'first-1'
                },
                {
                id:'11qq333',
                name:'first-2'
                }
                ]
           },
           {id:'22qq1',
           name:'second',
            isShow:false,
           elements:[
                {
                id:'13221qq',
                name:'second-1'
                },
                {
                id:'11qqw2223',
                name:'second-2'
                },
                {
                id:'11q9jj93',
                name:'second-3'
                }
           ]
           }
           
       ] 
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
        change_show(context){
            context.commit('change_show')
        }
    },
    getters:{
        getGroups: (state) => state.groups,
        getIsShow:(group) => group.isShow
    }
}