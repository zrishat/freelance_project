<template>
  <div class="login">
    <div>
      <form @submit.prevent="submit">
        <div>
          <label for="username">Username:</label>
          <input type="text" name="username" v-model="form.username"/>
        </div>
        <div>
          <label for="password">Password:</label>
          <input type="password" name="password" v-model="form.password"/>
        </div>
        <button type="submit">Submit</button>
      </form>
      <p v-if="showError" id="error">Username or Password is incorrect</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "SignInForm",

  data() {
    return {
      form: {
        username: "",
        password: ""
      },
      showError: false,
      userId: ''
    };
  },

  methods: {
    submit(event) {
      event.preventDefault()

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
        console.log(response)
        let token = response.data.token
        this.setLogined(token)
        this.setUserId(token)
        this.setCustomerId(token)
        this.setExecutorId(token)
        this.showError = false

      }).catch(err => {
        console.error(err)
        this.showError = true
      })
    },
    setLogined(token) {
      localStorage.setItem('token', token);
    },
    // getRole(token){
    //   const headers = {
    //     "Content-Type": "application/json",
    //     "Authorization": `Token ${token}`,
    //   };
    //   axios.get("http://127.0.0.1:8000/api/customers/", {headers})
    //       .then(response => {})
    // },
    setUserId(token) {
      const headers = {
        "Content-Type": "application/json",
        "Authorization": `Token ${token}`,
      };
      axios.get("http://127.0.0.1:8000/auth/users/me/", {headers})
          .then(response => {
                localStorage.setItem('userId', response.data.id);
                localStorage.setItem('userName', response.data.username);
                localStorage.setItem('userEmail', response.data.email);
              }
          )
    },
    setExecutorId(token) {
      const headers = {
        "Content-Type": "application/json",
        "Authorization": `Token ${token}`,
      };
      axios.get("http://127.0.0.1:8000/api/executors/", {headers})
          .then(response => {
            let userId = localStorage.getItem('userId');
            for (let prop in response.data) {
              if (response.data[prop]['user'] == userId) {
                localStorage.setItem('executorId', response.data[prop]['id'])
                localStorage.setItem('currentRole', "executor")
              }
            }
            this.$router.push("/profile-executor");
          })
    },
    setCustomerId(token) {
      const headers = {
        "Content-Type": "application/json",
        "Authorization": `Token ${token}`,
      };
      axios.get("http://127.0.0.1:8000/api/customers/", {headers})
          .then(response => {
            let userId = localStorage.getItem('userId');
            for (let prop in response.data) {
              if (response.data[prop]['user'] == userId) {
                localStorage.setItem('currentRole', "customer")
                localStorage.setItem('customerId', response.data[prop]['id'])              }
            }
            this.$router.push("/profile-customer");
            location.reload()
          })
    },
  }
}
;
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