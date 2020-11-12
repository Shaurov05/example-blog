<template>
  <!-- Navigation -->
  <nav class="navbar fixed-top navbar-expand-lg navbar-dark bg-dark fixed-top">
      <div class="container">
          <a class="navbar-brand" href="/home/">Example Blog</a>
          <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarResponsive">

              <ul class="navbar-nav ml-auto">
                  <li class="nav-item">
                      <a class="nav-link" href="/posts">Posts</a>
                  </li>


                  <li class="nav-item">
                      <a class="nav-link" href="/auth/login/">Login</a>
                  </li>


                  <li class="nav-item">
                      <a class="nav-link" href="/auth/register">Register</a>
                  </li>

              </ul>
          </div>
      </div>
  </nav>
</template>


<script>
import { apiService } from "@/common/api.service.js";

export default{
  name: "NavbarComponent",

  data (){
    return {
      username: null,
      is_authenticated: false,
    }
  },

  methods : {
    getUsername() {
      let endpoint = "/rest/api/current/user/";
      let method = "GET";
      console.log("navbar data ")
      apiService(endpoint, method)
          .then(data => {
            console.log("navbar data ", data)
            if(data.username){
              this.username = data.username
              this.is_authenticated = true
            }
            else {
              this.is_authenticated = false
            }
          })
          return this.is_authenticated
      }
    },
    created(){
      this.getUsername()
    }
  }
</script>
