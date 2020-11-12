import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Login from "../views/Login.vue";
import Register from "../views/Registration.vue";
import Users from "../views/Users.vue";
import NotFound from "../views/NotFound.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/users/",
    name: "Users",
    component: Users
  },
  {
    path: "/login/",
    name: "Login",
    component: Login
  },
  {
    path: "/register/",
    name: "Register",
    component: Register
  },
  {
    path:"*",
    name: "page-not-found",
    component: NotFound,
  },

];

const router = new VueRouter({
  mode: "history",
  // base: process.env.BASE_URL,
  routes
});

export default router;
