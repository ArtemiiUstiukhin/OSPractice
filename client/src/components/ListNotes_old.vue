<template>
    
        <v-list v-if="notes" color="orange" class="pt-0">
            <v-subheader >
                <div>Всего записей: {{notes.length}}</div>
            </v-subheader>

            <v-divider></v-divider>

            <v-list-tile v-for="(note,index) in notes" :key="index" >
               
                <v-list-tile-content >
                    <v-list-tile-title v-html="note"></v-list-tile-title>
                </v-list-tile-content>
            </v-list-tile>
                                    
        </v-list>
   
</template>
<script>
    export default{
        data:()=> ({
            
            
        }),
        methods:{

        },
        computed:{
            
            notes(){
                return this.$store.getters.getNotes  
            },
           
            
            
        }
            

    }
</script>

<style scoped>
   
    
</style>
