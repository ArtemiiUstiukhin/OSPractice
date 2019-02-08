<template>
   <div>

        <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4>
            <v-card class="elevation-12">
              <v-toolbar dark color="blue-grey darken-1">
                <v-toolbar-title>Вход</v-toolbar-title>
              </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-text-field prepend-icon="person" name="login" label="Логин" type="text" color="blue-grey darken-3"></v-text-field>
                  <v-text-field id="password" prepend-icon="lock" name="password" label="Пароль" type="password" color="blue-grey darken-3"></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn @click="$emit('signin')" dark color="orange accent-4">Вход</v-btn>
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>

     
   </div>
</template>

<script>
    export default {
        data: () => ({
           
        }),
            
        props: [
        
            
        ]
  }
</script>

<style scoped>

</style>
