<template>
   <v-container >
        <v-layout  class="nav" >
            <v-flex > 
                <v-navigation-drawer 
                    stateless 
                    value="true" 
                    class="grey lighten-4" 
                    v-slimscroll="options" 
                    floating 
                    width="100%" >
                    <v-tooltip right>
                        <template v-slot:activator="{ on }" >
                                <v-treeview  :active.sync="active" :items="items" item-key="id" open-on-click activatable transition return-object active-class="black--text" 
                                    >
                                    <template v-slot:label="{ item }">
                                        <div  v-on="on" v-on:mouseover="tips(item)">{{item.name}}</div>
                                    </template>                             
                                </v-treeview>                   
                        </template>
                       <span >{{remark}}</span>
                    </v-tooltip>
                    
                </v-navigation-drawer>
                
            </v-flex>
        </v-layout>
    </v-container> 
</template>

<script >
    
    
  export default{
        data: () => ({
            active:[],
            remark:{} ,
            options:{
                height:'320px',
                size:'0px'
            
            
        }
  }),
           
        computed:{
            items(){
                return this.$store.getters.getItems
            },
            
        },
        watch: {
            active: function(){
                if (this.active.length) {
                    this.$store.dispatch('stateCurrentObj',this.active[0])
                    //this.$store.dispatch('showOnMap',this.active[0].id)
                    console.log("remark: "+this.remark)
                }
            }
        },
        methods:{
            tips: function(item){
                if (item.remark)
                    {this.remark=item.remark}
                else if(item.group_remark)
                    {this.remark=item.group_remark}
                else if(item.group_type_remark)
                    {this.remark=item.group_type_remark}
                else
                    {this.remark=''}
                
            }
        },
        
       
  }
</script>

<style scoped>
</style>
