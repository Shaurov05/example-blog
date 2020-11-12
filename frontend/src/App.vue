<template>
  <div id="app">
    <NavbarComponent />
    <router-view />
  </div>
</template>

<script>
// import { apiService } from "@/common/api.service.js";
import NavbarComponent from "@/components/navbar.vue";

export default {
  name: "App",

  components: {
    NavbarComponent
  },

  methods: {
    async setToken() {
      var token1 = localStorage.getItem('token')
      console.log("token1 :",token1)
      if (token1 === null){
        // var token = null;
        localStorage.setItem('token', "initialized");
        console.log("token1 :", localStorage.getItem('token'))
      }
    },
  },

  created(){
    this.setToken()
  },
}

</script>

<style>
    html, body{
      height: 100%;
      font-family: "Playfair Display", serif;
    }
    .btn:focus{
      box-shadow: none !important;
    }
</style>
