<template>
  <div>
    <div class="outer-area">
      <div class="auth-box">
        <div v-if="showForm" class="registration-form-container">
          <h2 style="font-weight:bold; text-align:center">Registration Page</h2><br><br>
          <form  @submit.prevent="RegisterUser">
            <div class="row">

              <div class="col-md-6 mt-2 mb-2">
                <label >First Name</label>
              </div>
              <div class="col-md-6 mt-2 mb-2">
                  <input type="text" v-model="first_name"
                  required autofocus
                  placeholder="First Name">
              </div>

              <div class="col-md-6 mt-2 mb-2">
                <label >Last Name</label>
              </div>
              <div class="col-md-6 mt-2 mb-2">
                  <input type="text" v-model="last_name"
                  required autofocus
                  placeholder="Last Name">
              </div>

              <div class="col-md-6 mt-2 mb-2">
                <label for="email" >E-Mail Address</label>
              </div>
              <div class="col-md-6 mt-2 mb-2">
                  <input id="email" type="email"
                  v-model="email" required
                  placeholder="Email">
              </div>

              <div class="col-md-6 mt-2 mb-2">
                <label >Username</label>
              </div>
              <div class="col-md-6 mt-2 mb-2">
                  <input type="text" v-model="username" required
                  autofocus placeholder="Username">
              </div>

              <div class="col-md-6 mt-2 mb-2">
                <label for="password">Password</label>
              </div>
              <div class="col-md-6 mt-2 mb-2" >
                  <input id="password" type="password"
                  v-model="password1" required
                  placeholder="Password">
              </div>

              <div class="col-md-6 mt-2 mb-2">
                <label for="password-confirm">Confirm Password</label>
              </div>
              <div class="col-md-6 mt-2 mb-2">
                  <input
                      id="password-confirm" type="password"
                      v-model="password2" required
                      placeholder="Confirm Password">
              </div>

              <div class="col-md-6 mt-4 mb-2">
                  <button type="submit">Register</button>
              </div>
            </div>
          </form>

          <p v-if="error" class="error mt-2" > {{ error }}</p>


        </div>
        <div v-else class="user_profile">
          <h1> Congratulations! </h1>
          <h3>You have completed your registration.</h3><br><br>
          <h5> <span class="properties"> First Name:  </span> {{profile.first_name}} </h5>
          <h5> <span class="properties">Last Name: </span>{{profile.last_name}} </h5>
          <h5> <span class="properties">Username: </span>{{profile.username}} </h5>
          <h5> <span class="properties">Email: </span>{{profile.email}} </h5> <br><br>

          <router-link
                :to="{ name: 'Login' }"
                class = ""
                style="text-align:center; font-weight:bold; border-radius:10px; font-size:20px; padding:5px 10px 5px 10px;"
                > Login with your username/Email
          </router-link>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";

export default {
  name: "Register",

  data(){
    return {
      first_name: null,
      last_name: null,
      email: null,
      username: null,
      password1: null,
      password2: null,
      error: "",
      // userRegistered: false,
      showForm: true,
      profile: [],
    }
  },

  methods: {
    async RegisterUser(){
      if (!this.first_name || !this.last_name || !this.email || !this.username || !this.password1 || !this.password2){
        this.error = "Please fill in all the fields!"
      } else {
        let endpoint = `rest/api/users/`;
        let method = "POST"
        var data = {
          "first_name": this.first_name,
          "last_name": this.last_name,
          "email": this.email,
          "username": this.username,
          "password": this.password1,
          "confirm_password": this.password2,
        }
        apiService(endpoint, method, data)
            .then( response=> {
              this.error = null;
              console.log(response)
              if (response.email && response.username && !response.first_name){
                this.error = "A user with that username and email already exists."
              } else if (response.email == "user with this email address already exists."){
                this.error = response.email
              } else if(response.username == "A user with that username already exists."){
                this.error = response.username
              } else {
                console.log("else part registration")
                // this.userRegistered: true,
                this.error = null,
                this.showForm = false,
                this.profile = response
              }
            })
      }
    }
  }

}

</script>


<style scoped>
.user_profile{
  padding: 20px 20px 20px 20px;
}
.properties{
  color:#70231d;
  font-weight:bold;
}
.fields{
  martin-top:2px;
}
.auth-box{
  border: 3px solid lightgray;
  border-radius: 10px;
  padding: 50px 0px 50px 0px ;
  width: 600px;
  margin: auto ;
}
.registration-form-container{
  width: 300px;
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
