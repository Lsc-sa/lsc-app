import { createRouter, createWebHistory } from "vue-router";
import LoginView from "../views/LoginView.vue";
import SignupView from "../views/SignupView.vue";
import UserHome from "../views/UserHome.vue";

const router = createRouter({
  base: "/landing/",
  history: createWebHistory("/landing"),
  routes: [
    {
      path: "/",
      name: "login",
      component: LoginView,
    },
    {
      path: "/signup",
      name: "signup",
      component: SignupView,
    },
    {
      path: "/home",
      name: "userhome",
      component: UserHome,
    }
  ],
});

export default router;
