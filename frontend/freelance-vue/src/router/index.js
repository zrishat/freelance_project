import { createRouter, createWebHistory } from 'vue-router'
import Register from '../views/Register.vue'
import Login from '../views/Login.vue'
import ProfileCustomerView from "@/views/ProfileCustomerView";
import CreateTaskView from "@/views/CreateTaskView";
import ProfileExecutorView from "@/views/ProfileExecutorView";

const routes = [
  {
    path: '/register',
    name: "Register",
    component: Register,
    meta: { guest: true },
  },
  {
    path: '/login',
    name: "Login",
    component: Login,
    meta: { guest: true },
  },
  {
    path: '/profile-customer',
    name: "Profile customer",
    component: ProfileCustomerView,
    meta: {requiresAuth: true}
  },
  {
    path: '/profile-executor',
    name: "Profile executor",
    component: ProfileExecutorView,
    meta: {requiresAuth: true}
  },
  {
    path: '/create-task',
    name: "Create-task",
    component: CreateTaskView,
    meta: {requiresAuth: true}
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
