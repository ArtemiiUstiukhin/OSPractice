<template>
   <v-container>
        <v-layout wrap class="nav" >
           <v-treeview v-model="tree"  :items="items" item-key="name" open-on-click>
            </v-treeview>
        </v-layout>
    </v-container> 
</template>

<script >
  export default{
        data: () => ({
    items: [
      {
        name: 'group1',
        children:[{
            name:'object11'
        }]
      },
      {
        name: 'group2',
        children: [
          {
            name: 'group21',
            children: [{
              name: 'object211',
              
            }]
          },
          {
            name: 'object22',
           
          },
          {
            name: 'object23',
            
          }
        ]
      },
      {
        name: 'object01',
        
      },
      {
        name: 'object02',
        
      }
    ]
  }),
        computed:{
            groups(){
                return this.$store.getters.getGroups
            },
            isShow(group){
                return group.$store.getters.getIsShow
            }
           
            
        }
       
       
  }
</script>

<style scoped>


</style>

        
