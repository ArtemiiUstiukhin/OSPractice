<template>
   
    <div>
    
       
    <v-container  fluid grid-list-md  >
      <v-layout align-space-between justify-center column fill-height>
        <v-layout>
            <v-flex d-flex sm3 md3 class="form-top">
                <v-card light>
                    <v-card-title color="blue-grey darken-1" primary class="title">Навигация
                        <v-spacer></v-spacer> 
                            <v-menu bottom left>
                                <v-btn slot="activator" icon>
                                    <v-icon right>fas fa-list</v-icon>
                                </v-btn>
                                <v-list>
                                    <v-list-tile v-for="(item, i) in nav_view_mode" :key="i" @click="" >
                                        <v-list-tile-title>{{ item.title }}</v-list-tile-title>
                                    </v-list-tile>
                                </v-list>
                            </v-menu>
                    
                    </v-card-title>   
                    
                     <v-overflow-btn dense right :items="root_group" label="test1" item-value="text" ></v-overflow-btn>
                  
                    <Navigation ></Navigation>
                     
                </v-card>

            </v-flex>
            <v-flex d-flex grid class="form-top">
                <v-card  >
                    <v-card-title primary class="title">Контент</v-card-title>
                    <v-card-text> 2 </v-card-text>
                </v-card> 
            </v-flex>
        </v-layout>
        <v-layout>
            <v-flex d-flex grid class="form-bottom">
                <v-card >
                    <v-cart-title primary class="title">События</v-cart-title>
                    <v-card-text> 3 </v-card-text>
                </v-card>
            </v-flex>
        </v-layout>
      </v-layout>
    </v-container>
 
</div>

</template>

<script>
    import Navigation from '@/components/Navigation'
    
    export default{
        data:()=> ({
             nav_view_mode: [
                { title: 'Классы' },
                { title: 'Типы объектов'}
                ],
            root_group:[
                { text: 'test1' },
                { text: 'test2'}
            ]
        }),
        components:{
            
            Navigation
        }

    }
</script>

<style scoped>
    .form-top{
        min-height: 520px
    }
    .form-bottom{
        min-height: 200px
    }
</style>
