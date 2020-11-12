<template>
  <div class="container">
    <br><br><br><br><br>
    <h1 style="color:#785429; text-weight:bold; text-align:center;"> Login Page </h1>

    <div class="outer-area">
      <div class="auth-box">
        <div class="login-form-container">
          <form @submit.prevent="authenticate">
            <div class="row">
                <div class="col-md-4">
                  <label style="color:#1a0507; text-weight:bold; " for="id_username">Username/Email </label>
                </div>
                <div class="col-md-4">
                  <input
                    v-model="username"
                    type="text"
                    placeholder="Username/Email"
                    autofocus="autofocus"
                    maxlength="150"
                    id="id_username">
              </div>
            </div>
            <div class="row mt-2">
              <div class="col-md-4">
                <label style="color:#1a0507; text-weight:bold; " for="id_password">Password </label>
              </div>
              <div class="col-md-4">
                <input
                  v-model="password"
                  type="password"
                  placeholder="Password"
                  id="id_password">
              </div>
            </div>
            <br>
            <button
              class="button primary"
              type="submit">
              Log In
            </button>
          </form>

          <p v-if="error" class="error mt-2" > {{ error }}</p>

        </div>
      </div>
    </div>
    <br><div style="text-align:center;" class="mt-2 mb-2">
      <a >
        <router-link
              :to="{ name: 'Home' }"
              class = ""
              style="color:white; background-color:red; text-align:center; font-weight:bold; border-radius:10px; font-size:20px; padding:5px 10px 5px 10px;"
              > Return to Vue js Home Page
        </router-link>
      </a>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";

export default {
  name: "Login",

  data () {
    return {
      username: null,
      password: null,
      error: null,
    }
  },
  methods: {
    getUsername() {
      let endpoint = "/rest/api/current/user/";
      let method = "GET";

      apiService(endpoint, method)
          .then(data => {
            console.log("data ", data)
            if(data.username){
              this.username = data.username
            } else if(data.detail){
              localStorage.setItem("token", "initialized");
              this.expired = data.detail
            }
          })
        // this.authenticate()
    },

    async authenticate () {
      if (!this.username || !this.password){
        this.error = "Username or Password field cannot be empty!"
      } else{
          try {
            let endpoint = `/rest/api/login/`;
            let method = "POST";

            apiService(endpoint, method, {"email": this.username, "password": this.password} )
                .then( response => {
                  if(response.token){
                      localStorage.setItem("token", response.token);

                      this.$router.push({
                        name:'Home',
                      })
                    } else {
                    this.username = null;
                    this.password = null;
                    this.error = response.non_field_errors;
                  }
                })
          }
          catch(err) {
            console.log(err)
          }

      }


    },
  },

  created(){
    this.getUsername()
    // this.authenticate()
  }

}
</script>

<style scoped>
  .auth-box{
    border: 3px solid lightgray;
    border-radius: 10px;
    padding: 50px 0px 50px 0px ;
    width: 600px;
    margin: auto ;
  }
  .login-form-container{
    width: 400px;
    margin: auto;
  }
  .outer-area{
    margin-top: 100px;
  }
  .error {
  font-weight: bold;
  color: red;
  }

</style>
