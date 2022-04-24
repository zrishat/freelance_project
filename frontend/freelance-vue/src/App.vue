<template>
  <nav>
    <router-link to="/about">About</router-link> |
<!--    <router-link to="/login">Login</router-link> |-->
<!--    <router-link to="/register">Register</router-link> |-->
@
    <span v-if="isLoggedIn">
      <a @click="logout">Logout</a>
    </span>
    <span v-else>
      <router-link to="/register">Register</router-link> |
      <router-link to="/login">Login</router-link>
    </span>
  </nav>
  <router-view/>
</template>
<script>
export default {
  computed: {
    isLoggedIn: function() {
      return this.$store.getters.isAuthenticated;
    },
  },
  methods: {
    async logout() {
      // await this.$store.dispatch("LogOut");
      localStorage.clear()
      await this.$router.push("/login");
      location.reload()
    },
  },
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
