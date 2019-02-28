import axios from 'axios';

export default{
    state:{
        loading:true,
        errored:false,
        root_group:'test1', 
        map_coords:[59.94, 30.32],
        current_obj:{},
        current_note:{},
        
	items:[],
	/*
	items: [
            {
            id:'102',
            name: 'group102',
            children:[{
                id:'11',
                name:'object11',
                notes:[
                    {id:'First note 11',
                    events:[
                        {
                          id: 'Event1-11-1',
                          data: '159',
                          device: '6.0',
                          ip: '24',
                          priority: '4.0',

                        },
                        {
                         id: 'Event2-11-1',
                          data: '159',
                          device: '6.0',
                          ip: '24',
                          priority: '4.0',
                        },
                        {
                          id: 'Event3-11-1',
                          data: '159',
                          device: '6.0',
                          ip: '24',
                          priority: '4.0',
                        }
                    ]},
                    {id:'Second note 11',
                    events:[
                        {
                          id: 'Event1-11-2',
                          data: '159',
                          device: '6.0',
                          ip: '24',
                          priority: '4.0',

                        },
                        {
                         id: 'Event2-11-2',
                          data: '159',
                          device: '6.0',
                          ip: '24',
                          priority: '4.0',
                        },
                        {
                          id: 'Event3-11-2',
                          data: '159',
                          device: '6.0',
                          ip: '24',
                          priority: '4.0',
                        }
                    ]}
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
                        {id: 'First note 211',
                        events:[
                            {
                              id: 'Event1-211-1',
                              data: '159',
                              device: '6.0',
                              ip: '24',
                              priority: '4.0',

                            },
                            {
                             id: 'Event2-211-1',
                              data: '159',
                              device: '6.0',
                              ip: '24',
                              priority: '4.0',
                            },
                            {
                              id: 'Event3-211-1',
                              data: '159',
                              device: '6.0',
                              ip: '24',
                              priority: '4.0',
                            }
                        ]},
                        {id:'Second note 211',
                        events:[
                            {
                              id: 'Event1-211-2',
                              data: '159',
                              device: '6.0',
                              ip: '24',
                              priority: '4.0',

                            },
                            {
                             id: 'Event2-211-2',
                              data: '159',
                              device: '6.0',
                              ip: '24',
                              priority: '4.0',
                            },
                            {
                              id: 'Event3-211-2',
                              data: '159',
                              device: '6.0',
                              ip: '24',
                              priority: '4.0',
                            }
                    ]}
                        ]
                    }]
                },
                {
                id:'22',
                name: 'object22',
                notes:[
                    {id:'First note 22',
                    events:[
                        {
                          id: 'Event1-22-1',
                          data: '159',
                              device: '6.0',
                              ip: '24',
                              priority: '4.0',

                        },
                        {
                         id: 'Event2-22-1',
                          data: '159',
                              device: '6.0',
                              ip: '24',
                              priority: '4.0',
                        },
                        {
                          id: 'Event3-22-1',
                          data: '159',
                              device: '6.0',
                              ip: '24',
                              priority: '4.0',
                        }
                    ]}
                    ]
                },
                {
                id:'23',
                name: 'object23',
                notes:[
                    {id:'First note 23',
                    events:[
                        {
                          id: 'Event1-23-1',
                          data: '159',
                              device: '6.0',
                              ip: '24',
                              priority: '4.0',

                        },
                        {
                         id: 'Event2-23-1',
                          data: '159',
                              device: '6.0',
                              ip: '24',
                              priority: '4.0',
                        },
                        {
                          id: 'Event3-23-1',
                          data: '159',
                              device: '6.0',
                              ip: '24',
                              priority: '4.0',
                        }
                    ]},
                    {id:'Second note 23',
                    events:[
                        {
                          id: 'Event1-23-2',
                          data: '159',
                              device: '6.0',
                              ip: '24',
                              priority: '4.0',

                        },
                        {
                         id: 'Event2-23-2',
                          data: '159',
                              device: '6.0',
                              ip: '24',
                              priority: '4.0',
                        },
                        {
                          id: 'Event3-23-2',
                         data: '159',
                              device: '6.0',
                              ip: '24',
                              priority: '4.0',
                        }
                    ]}
                    ]
            
                }
            ]
            },
            {
            id:'01',
            name: 'object01',
            notes:[
                {id:'First note 01',
                events:[
                    {
                      id: 'Event1-01-1',
                      data: '159',
                              device: '6.0',
                              ip: '24',
                              priority: '4.0',

                    },
                    {
                     id: 'Event2-01-1',
                      data: '159',
                              device: '6.0',
                              ip: '24',
                              priority: '4.0',
                    },
                    {
                      id: 'Event3-01-1',
                      data: '159',
                              device: '6.0',
                              ip: '24',
                              priority: '4.0',
                    }
                ]},
                {id:'Second note 01',
                events:[
                    {
                      id: 'Event1-01-2',
                      data: '159',
                              device: '6.0',
                              ip: '24',
                              priority: '4.0',

                    },
                    {
                     id: 'Event2-01-2',
                      data: '159',
                              device: '6.0',
                              ip: '24',
                              priority: '4.0',
                    },
                    {
                      id: 'Event3-01-2',
                      data: '159',
                              device: '6.0',
                              ip: '24',
                              priority: '4.0',
                    }
                 ]},
                {id:'Third note 01',
                events:[
                   {
                      id: 'Event1-01-3',
                      data: '159',
                              device: '6.0',
                              ip: '24',
                              priority: '4.0',

                    },
                    {
                     id: 'Event2-01-3',
                      data: '159',
                              device: '6.0',
                              ip: '24',
                              priority: '4.0',
                    },
                    {
                      id: 'Event3-01-3',
                      data: '159',
                              device: '6.0',
                              ip: '24',
                              priority: '4.0',
                    }
                ]}
                ]
        
            },
            {
            id:'02',
            name: 'object02',
            notes:[
                {id:'First note 02',
                events:[
                    {
                      id: 'Event1-02-1',
                      data: '159',
                              device: '6.0',
                              ip: '24',
                              priority: '4.0',

                    },
                    {
                     id: 'Event2-02-1',
                      data: '159',
                              device: '6.0',
                              ip: '24',
                              priority: '4.0',
                    },
                    {
                      id: 'Event3-02-1',
                      data: '159',
                              device: '6.0',
                              ip: '24',
                              priority: '4.0',
                    }
                ]}
                ]
        
            }
            ],
	*/
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
	set_item_list (state,payload){
	    state.items=payload
	},
        set_root_group(state,payload){
            state.root_group=payload
        },
        set_map_coords(state,payload){
            state.map_coords=payload
        },
        set_current_obj(state,payload){
            state.current_obj=payload
        },
        set_current_note(state,payload){
            state.current_note=payload
        }
        
    
    },
    actions:{
        isGroups(context,payload){
	   console.log(payload);
           axios
            .get("http://localhost:8000/first_list_creating")
            //({method:'get',
	    // url:'http://localhost:8080/statj',
	    //  params: { sortby: payload.sort_type }})
            .then(response =>{
		  console.log(response.data);
		  context.commit('set_item_list', response.data);
		  console.log("first list creating");
                  })
            .catch(error =>{
                  console.log(error);
                  this.errored =true;
                  })
            .finally(() => (this.loading = false));
        },
        isClass(){
            console.log("creating class list")
	    axios
            .get("http://localhost:8000/set_class_list")
            .then(response =>{
                  console.log(response.data);
                  context.commit('set_item_list', response.data);
                  console.log("Item class list creted!");
                  })
            .catch(error =>{
                  console.log(error);
                  this.errored =true;
                  })
            .finally(() => (this.loading = false));
        },
        isGroup(){
            console.log("creating group list")
            axios
            .get("http://localhost:8000/set_group_list")
            .then(response =>{
                  console.log(response.data);
                  context.commit('set_item_list', response.data);
                  console.log("Item group list creted!");
                  })
            .catch(error =>{
                  console.log(error);
                  this.errored =true;
                  })
            .finally(() => (this.loading = false));
        },
        isRootGroup(context, payload){
            context.commit('set_root_group', payload);
        },
        showOnMap(context, payload){
            var placemark=this.getters.getPlacemarks.find((placemark)=> placemark.id==payload)
            context.commit('set_map_coords',placemark.coords)
        },
        stateCurrentObj(context,payload){
            context.commit('set_current_obj',payload)
        },
        setCurrentNote(context,note){
            context.commit('set_current_note',note)
        }
        
        
        
        
    },
    getters:{
        getItems: (state) => state.items,
        getPlacemarks:(state)=> state.placemarks,
        getMapCoords:(state)=> state.map_coords,
        getNotes:(state)=>{
              var item=state.current_obj
              return item.notes
        },
        getEvents: (state)=>{
                    var note  = state.current_note
                    return note.events
                
           
        }
        
    }
}
