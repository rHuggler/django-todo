<template>
  <div
  >
    <label>
      <input
        type="checkbox"
        :id="'todo_'+id"
        v-model="isDone"
        @change="toggleStatus"
      >
      <span
        :class="classObject"
      >
        {{text}}
      </span>
      <a
        href="#"
        @click="removeTodo"
      >
        (remove)
      </a>
    </label>
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
  },
  computed: {
    classObject: function () {
      let textColor = this.isDone ? 'grey-text' : 'black-text'
      return {
        strikethrough: this.isDone,
        [textColor]: true
      }
    }
  }
}
</script>

<style scoped>
a {
  text-decoration: none;
}
.strikethrough {
  text-decoration: line-through;
}
</style>
