<template>
<v-app>
    <div id="app">
        <app-header></app-header>
        <v-content>
             <sign-in elevation=20 temporary v-on:signin="showSignin=!showSignin" v-if="showSignin" ></sign-in>   
<!--             <button v-on:click="sign=!sign">регистрация</button>-->
        <main-part v-if="!showSignin" ></main-part>
        </v-content>
        <Footer></Footer>
    </div>
</v-app>
</template>

<script>
    import SignIn from '@/components/SignIn'
    import AppHeader from '@/components/AppHeader'
    import MainPart from '@/components/MainPart'
    import Footer from '@/components/Footer'
    
    export default{
         data(){
                return{
                    showSignin:true
                }
        },
        methods:{
            
        },
        components:{
            SignIn,
            AppHeader,
            MainPart,
            Footer
        },
    }
</script>
