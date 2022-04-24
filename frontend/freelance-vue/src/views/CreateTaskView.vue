<template>
  This is form to create task
  <form @submit.prevent="createTask">
    <p>Title: <input v-model="taskName"/></p>
    <p>Description: <textarea v-model="taskDesc"/></p>
    <p>Price: <input v-model="taskPrice" type="number"/></p>
    <!-- input v-model="taskEnd" type="datetime"/ -->
    <p>
      <button type="submit">Save</button>
    </p>
  </form>
</template>
<script>
import axios from 'axios'

export default {
  data() {
    return {
      taskName: "",
      taskDesc: "",
      taskPrice: "",
      taskEnd: "",
      token: localStorage.getItem('token'),
      userId: parseInt(localStorage.getItem('customerId'))
    };
  },
  methods: {
    createTask() {
      axios.post(
          "http://127.0.0.1:8000/api/tasks/",
          {
            'name': this.taskName,
            'description': this.taskDesc,
            'price': this.taskPrice,
            'start_task': "2022-04-20T07:25:30Z",
            'end_task': "2022-04-22T07:25:30Z",
            'status': "1",
            'customer': this.userId,
            'executor': ""
          },
          {
            headers: {
              "Content-Type": "application/json",
              "Authorization": `Token ${this.token}`,
            }
          }
      ).then(response => {
            console.log(response.data)
            this.$router.push("/profile-customer")
          }
      ).catch(err => {
        console.error(err)
      })
    },
  }
};
</script>
