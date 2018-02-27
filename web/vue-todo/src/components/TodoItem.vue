<template>
  <div
    class="todo-item"
  >
    <input
      type="checkbox"
      :id="'todo_'+id"
      v-model="isDone"
      @change="toggleStatus"
    >
    <span>{{text}}</span>
    <a
      href="#"
      @click="removeTodo"
    >
      (remove)
    </a>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'TodoItem',
  props: {
    todo: {
      type: Object,
      required: true
    }
  },
  data () {
    return {
      id: this.todo.id,
      isDone: this.todo.status,
      text: this.todo.text
    }
  },
  methods: {
    toggleStatus: function () {
      axios.patch('http://localhost:8000/todos/'+this.id+'/', {
        status: this.isDone
      })
    },
    removeTodo: function () {
      axios.delete('http://localhost:8000/todos/'+this.id+'/')
      this.$emit('remove', this.id)
    }
  }
}
</script>

<style scoped>
a {
  text-decoration: none;
}
</style>
