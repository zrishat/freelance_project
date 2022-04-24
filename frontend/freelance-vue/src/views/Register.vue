<template>
  <div class="register">
    <div>
      <form @submit.prevent="submit">
        <div>
          <label for="username">Username:</label>
          <input type="text" name="username" v-model="form.username">
        </div>
        <div>
          <label for="email">Email:</label>
          <input type="text" name="email" v-model="form.email">
        </div>
        <div>
          <label for="role1">Executor:</label>
          <input id="role1" type="radio" name="role" v-model="form.role" value="executor" checked>
        </div>
        <div>
          <label for="role2">Customer:</label>
          <input id="role2" type="radio" name="role" v-model="form.role" value="customer">
        </div>
        <div>
          <label for="password">Password:</label>
          <input type="password" name="password" v-model="form.password">
        </div>
        <button type="submit"> Submit</button>
      </form>
    </div>
    <p v-if="showError" id="error">Username already exists</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Register",
  components: {},
  data() {
    return {
      form: {
        username: "",
        email: "",
        password: "",
        role: "executor",
        registerId: "",
        token: ""
      },
      showError: false
    };
  },
  methods: {
    async submit() {
      axios.post(
          `http://127.0.0.1:8000/auth/users/`,
          {
            'username': this.form.username,
            'password': this.form.password,
            'email': this.form.email
          },
          {
            headers: {
              'Content-Type': 'application/json',
            }
          },
      ).then(response => {
        this.registerId = response.data.id
        this.createToken()
        console.log("form.role", this.form.role)
        this.setRole(this.form.role)
        // this.$router.push("/login");
        this.showError = false
      }).catch(err => {
        console.error(err)
        this.showError = true
      })
    },
    createToken() {
      axios.post(
          `http://127.0.0.1:8000/auth/token/`,
          {
            'username': this.form.username,
            'password': this.form.password
          },
          {
            headers: {
              'Content-Type': 'application/json',
            }
          },
      ).then(response => {
        console.log("createToken", response)
        this.token = response.data.token
      })
    },
    setRole(role) {
      console.log("role", role)
      let url = ''
      if (role == 'customer') {
        url = 'http://127.0.0.1:8000/api/customers/'
      }
      if (role == 'executor') {
        url = 'http://127.0.0.1:8000/api/executors/'
      }
      axios.post(
          url,
          {
            "user": this.registerId
          },
          {
            headers: {
              'Content-Type': 'application/json',
              "Authorization": `Token ${this.token}`,
            }
          },
      ).then(response => {
        console.log("setRole", response)
        this.$router.push("/login");
      }).catch(err => {
        console.error(err)
      })

    }

  }
}
</script>

<style scoped>
* {
  box-sizing: border-box;
}

label {
  padding: 12px 12px 12px 0;
  display: inline-block;
}

button[type=submit] {
  background-color: #4CAF50;
  color: white;
  padding: 12px 20px;
  cursor: pointer;
  border-radius: 30px;
}

button[type=submit]:hover {
  background-color: #45a049;
}

input {
  margin: 5px;
  box-shadow: 0 0 15px 4px rgba(0, 0, 0, 0.06);
  padding: 10px;
  border-radius: 30px;
}

#error {
  color: red;
}
</style>
