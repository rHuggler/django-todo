<template>
  <div class="to-dos">
    <ul
      class="to-do-list">

      <li
        class="to-do"
        v-for="todo in todos"
        :key="todo.id">

        <input
          type="checkbox"
          :id="todo.id"
          v-model="todo.status"
          v-on:change="changeTodoStatus(todo)">

        <label
          :for="todo.id"
          :class="{ strike: todo.status }">
          {{todo.text}}
        </label>
      </li>

      <input
        type="checkbox"
        disabled>
      <input
        type="text"
        placeholder="New To-Do"
        @keyup.enter="postNewTodo">

    </ul>
  </div>
</template>

<script>
import axios from 'axios';

var requester = axios.create({
  baseURL: 'http://localhost:8000/',
  timeout: 5000,
})

export default {
  name: 'TodoList',
  data () {
    return {
      todos: [],
      errors: []
    }
  },

  methods: {
    getTodoList () {
      requester.get('todos/')
        .then(response => {
          this.todos = response.data
        })
        .catch(e => {
          this.errors.push(e)
        })
    },

    changeTodoStatus (todo) {
      requester.patch('todos/' + todo.id + '/', {
        status: todo.status
      })
    },

    postNewTodo (event) {
      let inputText = event.target.value
      if (inputText) {
        requester.post('todos/', {
          text: inputText
        })
          .then(response => {
            this.todos.push(response.data)
          })
          .catch(e => {
            this.errors.push(e)
          })
      }
    }
  },

  created () {
    this.getTodoList()
  }
}
</script>

<style>
li {
  list-style: none;
  margin-bottom: 10px;
}

.strike {
  text-decoration: line-through;
}
</style>
