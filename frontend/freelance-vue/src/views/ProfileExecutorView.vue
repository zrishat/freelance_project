<template>
  <p>Это кабинет фрилансера</p>
  <div v-if="User">
    <p>Hi {{ User }}</p>
  </div>
  <div v-if="allTasks">
    <p>All tasks:</p>
    <div v-for="task in allTasks" :key="task.id">
      <div class="task">
        <p>Title: <strong>{{ task.name }}</strong></p>
        <p>Description: {{ task.description }}</p>
        <p>Price: {{ task.price }}</p>
<!--        <p>{{ UserId }}</p>-->
<!--        <p>{{ task.executor_list && task.executor_list.split(',') }}</p>-->
        <p v-if="task.executor_list && task.executor_list.split(',').includes(UserId)">
            <button type="button" class="red" disabled>Selected</button>
        </p>
        <p v-else>
          <button type="button" class="blue" @click="selectTask(task.id)">Select</button>
        </p>
      </div>
    </div>
  </div>
  <div v-else>
    Not created tasks
  </div>
  <div>
  </div>

</template>

<script>

import axios from 'axios'

export default {
  data() {
    return {
      User: localStorage.getItem('userName'),
      UserId: localStorage.getItem('userId'),
      allTasks: "",
      token: localStorage.getItem('token'),
      listExecutors: ""
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
    updateTask(id) {
      axios.patch(`http://127.0.0.1:8000/api/tasks/${id}/`,
          {
            "executor_list": [...new Set((this.listExecutors + this.UserId + ',').split(','))].join()
          },
          {
            headers: {
              "Content-Type": "application/json",
              "Authorization": `Token ${this.token}`,
            }
          }
      ).then(response => {
        console.log(response.data)
        location.reload()
      }).catch(err => {
        console.error(err)
      })
    },
    selectTask(id) {
      axios.get(`http://127.0.0.1:8000/api/tasks/${id}/`,
          {
            headers: {
              "Content-Type": "application/json",
              "Authorization": `Token ${this.token}`,
            }
          }
      ).then(response => {
        this.listExecutors = response.data.executor_list
        this.updateTask(id)
      }).catch(err => {
        console.error(err)
      })
    },
  }
};
</script>
<style>
.task {
  border: 1px solid springgreen;
}

.blue {
  background: aqua;
}
.red{
  background: red;
}
</style>