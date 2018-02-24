<template>
  <div class="to-do-list">
    <h1
      class="main-header">
      To-Do List
    </h1>
    <ul
      class="to-dos">

      <li
        class="to-do"
        v-for="todo in todos"
        :key="todo.id">

        <input
          type="checkbox"
          :id="todo.id"
          v-model="todo.status"
          @change="changeTodoStatus(todo)">

        <label
          :for="todo.id"
          :class="{ strike: todo.status }">
          {{todo.text}}
        </label>

        <button
          @click="deleteTodo(todo)">
          x
        </button>
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
            event.target.value = ''
          })
          .catch(e => {
            this.errors.push(e)
          })
      }
    },

    deleteTodo (todo) {
      if (confirm('This will delete "' + todo.text + '" to-do.')) {
        requester.delete('todos/' + todo.id + '/')
          .catch(e => {
            this.errors.push(e)
          })
        let i = this.todos.indexOf(todo)
        let _ = this.todos.splice(i, 1)
      }
    }
  },

  created () {
    this.getTodoList()
  }
}
</script>

<style>
.to-do-list {
  width: 40%;
  margin: 0 auto;
}

.to-dos {
  margin-top: 40px;
  padding-left: 40px;
  text-align: left;
}

.main-header {
  margin: 0;
}

li {
  list-style: none;
  margin-bottom: 10px;
}

.strike {
  text-decoration: line-through;
}

button {
  border: none;
  margin-left: 5px;
  background-color: #fff;
  font-weight: bold;
}

button:hover {
  color: red;
}
</style>
