export default{
    state:{
        loading:true,
        errored:false,
        root_group:'test1', 
        map_coords:[59.94, 30.32],
        current_obj:{},
        items: [
            {
            id:'102',
            name: 'group102',
            children:[{
                id:'11',
                name:'object11',
                notes:[
                    'First note 11',
                    'Second note 11'
                    ]
                }]
            },
            {
            id:'202',
            name: 'group202',
            children: [
                {
                id:'21',
                name: 'group21',
                children: [{
                    id:'211',
                    name: 'object211',
                    notes:[
                        'First note 211',
                        'Second note 211'
                        ]
                    }]
                },
                {
                id:'22',
                name: 'object22',
                notes:[
                    'First note 22'
                    ]
                },
                {
                id:'23',
                name: 'object23',
                notes:[
                    'First note 23',
                    'Second note 23'
                    ]
            
                }
            ]
            },
            {
            id:'01',
            name: 'object01',
            notes:[
                'First note 01',
                'Second note 01',
                'Third note 01'
                ]
        
            },
            {
            id:'02',
            name: 'object02',
            notes:[
                'First note 02'
                ]
        
            }
            ],
        placemarks: [
            {
                id:'11',
                type:'point',
                coords: [59.94, 30.32],
                balloonTemplate: 'object11'
                
            },
            
            {
                id: '211',
                type:'point',
                coords: [59.92, 30.3557],
                balloonTemplate: 'object211'
            },
            {
                id: '22',
                type:'point',
                coords: [59.9423, 30.32112],
                balloonTemplate: 'object22'
           
            },
            {
                id: '23',
                type:'point',
                coords: [59.942, 31.02113],
                balloonTemplate: 'object23'
            
            },
            {
                id: '01',
                type:'point',
                coords: [59.9454, 30.33],
                balloonTemplate: 'object01'
        
            },
            {
                id: '02',
                type:'point',
                coords: [59.88, 30.324],
                balloonTemplate: 'object02'
        
            }
            ]
    },
    mutations:{
        set_root_group(state,payload){
            state.root_group=payload
        },
        set_map_coords(state,payload){
            state.map_coords=payload
        },
        set_current_obj(state,payload){
            state.current_obj=payload
        }
        
    
    },
    actions:{
//        isGroups(){
//           axios
//            .get('')
//            .then(response =>{
//                  this.items=respone.data
//                  })
//            .catch(error =>{
//                  console.log(error);
//                  this.errored =true;
//                  })
//            .finally(() => (this.loading = false));
//        },
        isClass(){
            console.log("isClass action")
        },
        isGroup(){
            console.log("isGroup action")
        },
        isRootGroup(context, payload){
            context.commit('set_root_group', payload);
            console.log("New root group: "+context.state.root_group)
        },
        showOnMap(context, payload){
            var placemark=this.getters.getPlacemarks.find((placemark)=> placemark.id==payload)
            context.commit('set_map_coords',placemark.coords)
        },
        stateCurrentObj(context,payload){
            context.commit('set_current_obj',payload)
        }
        
        
        
    },
    getters:{
        getItems: (state) => state.items,
        getPlacemarks:(state)=> state.placemarks,
        getMapCoords:(state)=> state.map_coords,
        getNotes:(state)=>{
              var item=state.current_obj
              return item.notes  
        }                      
        
    }
}