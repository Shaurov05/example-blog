<template>
  <div class="home">
    <br><br><br><br><br>
    <div class="container mt-4 mb-4">
      <h1 class="mb-4" style="text-align:center;"> Welcome to List of registered Users Page </h1>
      <div style="text-align:center;" class="mt-2 mb-2">
        <a >
          <router-link
                :to="{ name: 'Home' }"
                class = ""
                style="color:white; background-color:red; text-align:center; font-weight:bold; border-radius:10px; font-size:20px; padding:5px 10px 5px 10px;"
                > Return to Vue js Home Page
          </router-link>
        </a>
      </div>
      <br><h4> There are {{ total }} registered users! Registered users are listed below: </h4>
      <br><br><hr>
      <div v-for="user in users"
            :key="user.pk">
          <p class="mb-0"> First Name:
            <span class="user_fname"> {{ user.first_name }} </span>
          </p>

          <p class="mb-0"> Last Name:
            <span class="user_fname"> {{ user.last_name }} </span>
          </p>

          <p class="mb-0"> Email:
            <span class="user_fname"> {{ user.email }} </span>
          </p>

          <hr>
      </div>

      <div class="my-4">
        <p v-show="loadingUsers">...loading...  </p>
        <button
            v-show="next"
            @click="getUsers"
            class="btn btn-sm btn-outline-success"
        > Load More </button>
      </div>

    </div>
  </div>
</template>

<script>
import { apiService } from "../common/api.service.js";

export default {
  name: "Users",
  data() {
    return {
      users : [],
      next: null,
      total: null,
      loadingUsers: false,
    }
  },

  methods :{
    check_authentication(){
      if (localStorage.getItem('token')){
        console.log("My user is logged in!");
      } else {
        console.log("My user is not logged in!");
      }
    },

    getUsers() {
      let endpoint = "/rest/api/users/";
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingUsers = true

      apiService(endpoint)
        .then(data => {
          this.users.push(...data.results)
          this.loadingUsers = false;
          this.total = data.count;

          if(data.next){
            this.next = data.next;
          } else {
            this.next = null;
          }
        })
    },
  },

  created() {
    this.check_authentication()
    this.getUsers()
    document.title = "Blog Users"
  },
  // components: {
  //
  // }
};
</script>


<style scoped>
.user_fname{
  font-weigh: bold;
  color: #DC3545;
}

.question-link{
  font-weight: bold;
  color: black;
}

.question-link:hover {
  color: #343A40;
  text-decoration: none;
}

</style>
