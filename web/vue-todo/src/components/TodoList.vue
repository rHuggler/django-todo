<template>
  <ul
    class="todo-list"
  >
    <li
      v-for="todo in todos"
      :key="todo.id"
    >
      <todo-item
        :todo="todo"
        @remove="removeTodo"
      >
      </todo-item>
    </li>
    <li>
      <input
        type="text"
        v-model="newTodoText"
        @keyup.enter="createTodo"
      >
    </li>
  </ul>
</template>

<script>
import axios from 'axios'
import TodoItem from './TodoItem'

export default {
  name: 'TodoList',
  data () {
    return {
      todos: [],
      errors: [],
      newTodoText: ''
    }
  },
  components: { TodoItem },
  methods: {
    getTodos: function () {
      axios.get('http://localhost:8000/todos/')
        .then(response => {
          this.todos = response.data
        })
        .catch(e => {
          this.errors.push(e)
        })
    },
    createTodo: function () {
      axios.post('http://localhost:8000/todos/', {
        text: this.newTodoText
      })
        .then(response => {
          this.todos.push(response.data)
          this.newTodoText = ''
        })
        .catch(e => {
          this.errors.push(e)
        })
    },
    removeTodo: function (id) {
      let index = this.todos.findIndex(todo => { return todo.id === id})
      this.todos.splice(index, 1)
    }
  },
  created () {
    this.getTodos()
  }
}
</script>

<style scoped>
li {
  list-style: none;
}
</style>
