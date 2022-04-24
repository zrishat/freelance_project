<template>
  <p>Это кабинет заказчика</p>
  <div v-if="User">
    <p>Hi {{ User }}</p>
  </div>
  <div v-if="allTasks">
    <p>All my tasks:</p>
    <div v-for="task in allTasks" :key="task.id">
      <div v-if="task.customer == this.customerId">
        <div class="task">
          <p>Title: <strong>{{ task.name }}</strong></p>
          <p>Description: {{ task.description }}</p>
          <p>Price: {{ task.price }}</p>
          <p>
            <button type="button" @click="deleteTask(task.id)">Delete</button>
          </p>
        </div>
      </div>
    </div>
  </div>
  <div v-else>
    You not created tasks
  </div>
  <div>
    <p>
      <router-link to="/create-task">Create task</router-link>
    </p>
  </div>

</template>

<script>

import axios from 'axios'

export default {
  data() {
    return {
      User: localStorage.getItem('userName'),
      allTasks: "",
      token: localStorage.getItem('token'),
      customerId: localStorage.getItem('customerId'),
    };
  },
  created() {
    const headers = {
      "Content-Type": "application/json",
      "Authorization": `Token ${this.token}`,
    };
    axios.get("http://127.0.0.1:8000/api/tasks/", {headers})
        .then(response => this.allTasks = response.data);
  },
  methods: {
    deleteTask(id) {
      const headers = {
        "Content-Type": "application/json",
        "Authorization": `Token ${this.token}`,
      };
      axios.delete(`http://127.0.0.1:8000/api/tasks/${id}`, {headers}).then(response => {
        console.log(response.data)
        location.reload()
      }).catch(err => {
        console.error(err)
      })
    }
  }
};
</script>
<style>
.task {
  border: 1px solid springgreen;
}
</style>