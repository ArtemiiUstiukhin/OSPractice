<template>
   
    <div>
    
       
    <v-container  fluid grid-list-md  >
      <v-layout align-space-between justify-center column fill-height>
        <v-layout>
            <v-flex d-flex sm3 md3 class="form-top">
                <v-card color="grey lighten-4" light class="CardTextPadding">
                    <v-card-title color="blue-grey darken-1" class="title px-1 pb-2 pt-0">Навигация  
                        <v-spacer></v-spacer> 
                            <v-menu bottom left>
                                <v-btn slot="activator" icon>
                                    <v-icon right>fas fa-list</v-icon>
                                </v-btn>
                                <v-list >
                                    <v-list-tile  v-for="(item, i) in nav_view_mode" :key="i" @click="ViewModeSwitch(item)" >
                                        <v-list-tile-title>{{ item.title }}</v-list-tile-title>
                                    </v-list-tile>
                                </v-list>
                            </v-menu>
                    </v-card-title> 
                    
                        <v-select class="pa-0 ma-0" v-model="selectedRootGroup" menu-props="right" :items="root_group" label="test1" color="orange darken-3" solo @change="RootGroupSelector()"></v-select>
                    
                    <v-card-text class="CardTextPadding pa-0 ma-0" >
                        <Navigation class="pl-0 pt-0 " ></Navigation>
                     </v-card-text>
                </v-card>

            </v-flex>
            <v-flex d-flex sm12 md12 grid class="form-top">
                <v-card color="grey lighten-4" >
                    <v-card-title primary class="title px-3 pb-0 pt-0 mb-0  ">Контент
                        <v-spacer></v-spacer>
                        <div> 
<!--                            div for correct alignment-->
                             <v-radio-group  v-model="selectedViewContent" row>
                                <v-radio label="Список" value="list" color="orange darken-3" ></v-radio>
                                <v-radio label="Карта" value="map" color="orange darken-3"></v-radio>
                            </v-radio-group>
                        </div>
                    </v-card-title>
                        <v-layout wrap fill-height px-3 pb-3 pt-0 ma-0>
                            <v-flex v-if="selectedViewContent=='list'" >
                                <ListNotes></ListNotes>
                            </v-flex>
                            <v-flex v-if="selectedViewContent=='map'">
                                <yandex-map
                                  :coords="mapCoords"
                                  zoom="10"
                                  style="width: 100%; height: 400px;"
                                  :behaviors="['drag','scrollZoom']"
                                  :controls="['zoomControl']"
                                  :placemarks="placemarks"
                                  map-type="map">
                                </yandex-map>
                            </v-flex>
                        </v-layout>
                </v-card> 
            </v-flex>
        </v-layout>
        <v-layout  >
            <v-flex d-flex grid class="form-bottom" >
                <v-card color="grey lighten-4" mx-3>
                    <v-card-title class="title px-3 pb-2 pt-3">События</v-card-title>
                    <EventTable ></EventTable>
                </v-card>
            </v-flex>
        </v-layout>
      </v-layout>
    </v-container>
 
</div>

</template>

<script>
    import Navigation from '@/components/Navigation'
    import ListNotes from '@/components/ListNotes'
    import EventTable from '@/components/EventTable'
    
    export default{
        data:()=> ({

             nav_view_mode: [
                { title: 'Классы' ,
                    tab: 'class'},
                { title: 'Группы',
                    tab: 'group'}
                ],
            root_group:[
                { text: 'test 1' ,
                  value: 'test1'},
                { text: 'test 2',
                  value:'test2'}
            ],
            selectedRootGroup: 
                    { text: 'test 1' ,
                    value: 'test1'},
            selectedViewContent:'list'
        }),
        components:{           
            Navigation,
            ListNotes,
            EventTable
        },
        methods:{
            ViewModeSwitch: function(item){
                if(item.tab=='class'){
                    this.$store.dispatch('isClass');
		    
                }else if(item.tab=='group'){
                    this.$store.dispatch('isGroup');
		    
                }
            },
            RootGroupSelector: function(){
                 setTimeout(() => {
                    this.$store.dispatch('isRootGroup', this.selectedRootGroup)}, 1)
                // Without setTimeout this.selectedRootGroup have a previous value
            }
        },
	mounted: function(){
		this.$nextTick(function (){
			this.$store.dispatch('isGroups',{sort_type:'group'});
			
		})
	},
        computed:{
            items(){
                return this.$store.getters.getItems
            },
            notes(){
                return this.$store.getters.getNotes  
            },
            placemarks(){
                return this.$store.getters.getPlacemarks
            },  
            mapCoords(){
                return this.$store.getters.getMapCoords
            },
	}
    }
</script>

<style scoped>
    .form-top{
        height: 520px
    }
    .form-bottom{
        min-height: 200px
    }
    .CardTextPadding{
        padding: 10px   
    }
    
</style>
