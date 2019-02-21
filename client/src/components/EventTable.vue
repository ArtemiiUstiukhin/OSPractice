<template>
    
     <v-data-table
         
      :headers="headers"
      :items="events"     
     class="px-3">
      <template  
         slot="items" slot-scope="props">
        <td>{{ props.item.id }}</td>
        <td >{{ props.item.data }}</td>
        <td class="text-xs-left">{{ props.item.device}}</td>
        <td class="text-xs-left">{{ props.item.ip }}</td>
        <td class="text-xs-left">{{ props.item.priority }}</td>
        
      </template>
    </v-data-table>
   
</template>
<script>
    export default{
        data:()=> ({
            headers: [
        {
          text: 'ID',
          align: 'left',
          sortable: false,
          value: 'id'
        },
        
        { text: 'Data', value: 'data' },
        { text: 'Device', value: 'device' },
        { text: 'IP', value: 'ip' },
        { text: 'Priority', value: 'priority' }
      ],
//            events:[
//                    {
//                      id: 'Event1-02-1',
//                      data: '159',
//                              device: '6.0',
//                              ip: '24',
//                              priority: '4.0',
//
//                    },
//                    {
//                     id: 'Event2-02-1',
//                      data: '159',
//                              device: '6.0',
//                              ip: '24',
//                              priority: '4.0',
//                    },
//                    {
//                      id: 'Event3-02-1',
//                      data: '159',
//                              device: '6.0',
//                              ip: '24',
//                              priority: '4.0',
//                    }
//                ]
//     
            
        }),
        methods:{

        },
        computed:{
          events(){
                return this.$store.getters.getEvents
            }  
            
            
        }
            

    }
</script>

<style scoped>
   
    
</style>
