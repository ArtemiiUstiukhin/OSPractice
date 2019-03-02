k<template>
   <v-container>
        <v-layout wrap class="nav" >
            <v-tooltip right>
                <template v-slot:activator="{ on }">
                    
                        <v-treeview  :active.sync="active" :items="items" item-key="id" open-on-click activatable transition return-object active-class="black--text"  >
                            <template v-slot:label="{ item }">
                                <div  v-on="on" v-on:mouseover="tips(item)">{{item.name}}</div>
                            </template>                             
                        </v-treeview>                   
                </template>
               <span>{{remark}}</span>
            </v-tooltip>
        </v-layout>
    </v-container> 
</template>

<script >
  export default{
        data: () => ({
           active:[],
           remark:{} 
           
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
                    this.$store.dispatch('showOnMap',this.active[0].id)
                    console.log("remark: "+this.remark)
                }
            }
        },
        methods:{
            tips: function(item){
                this.remark=item.remark
            }
        },
        
       
  }
</script>

<style scoped>
</style>
