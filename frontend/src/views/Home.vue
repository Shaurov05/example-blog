<template>
  <div class="home">
      <!-- <NavbarComponent /> -->
    <br><br>
    <div class="container mt-4">
      <h1 class="mb-4" style="color:#785429; text-align:center;"> Welcome to Home Page  </h1>
      <hr><h5 class="mb-4" style="text-align:center;"> This page is created using Vue Cli!  </h5>
      <h6 class="mb-4" style="text-align:center;"> This page communicates with Rest API  </h6>
      <hr><br><br><br>

      <p style="font-size:20px; font-weight:bold; color:#543a1a"> You can register and login via API and also can fetch information i.e. list of users. </p>
      <h3 v-if="username"> You are authorized as <span style="font-size:30px;" class='link'> {{ username }} </span> </h3>
      <h3 v-else>You are unauthorized </h3>
      <h3 v-if="expired" class="link"> {{ expired }} Please login again to continue </h3>
      <br><ul>
        <!-- <li> Username :  </li> -->
        <li>
          <a>
            <router-link
                  :to="{ name: 'Register' }"
                  class = "router_link"
                  style=""
                  > Register using Vue
            </router-link>
          </a>
        </li>
        <li>
          <a>
            <router-link
                  :to="{ name: 'Login' }"
                  class = "router_link"
                  style=""
                  > Login using Vue
            </router-link>
          </a>
        </li>

        <li>
          <a >
            <router-link
                  :to="{ name: 'Users' }"
                  class = "router_link"
                  style=""
                  > List of users
            </router-link>
          </a>
        </li>
      </ul><br><br>
      <div style="text-align:center;">
        <a v-if="username" @click="LogoutUser" class="router_link btn btn-sm btn-outline-secondary" >
          User Logout
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
// import NavbarComponent from "@/components/navbar.vue";

export default {
  name: "Home",

  components: {
    // NavbarComponent
  },

  data (){
    return {
      username: null,
      expired: null,
    }
  },

  methods: {
    LogoutUser() {
      localStorage.setItem("token", "initialized");
      this.username = null;
      this.$router.push({
        name:'Home',
      })
    },

    async getUsername() {
      let endpoint = "/rest/api/current/user/";
      let method = "GET";

      apiService(endpoint, method)
          .then(data => {
            console.log("data ", data)
            if(data.username){
              this.username = data.username
            } else if(data.detail){
              this.expired = data.detail
            }
          })
    }

  },

  created(){
    this.getUsername()
  }

};
</script>


<style scoped>
    .router_link{
      text-decoration: underline;
      color:#7a000e; font-size:20px; font-weight:bold;
    }

    .link{
      color:#7a000e; font-size:20px; font-weight:bold;
    }


</style>
