<template>
  <div
  >
    <label>
      <input
        type="checkbox"
        :id="'todo_'+id"
        v-model="isDone"
        @change="toggleStatus"
      />
      <span
        :class="classObject"
      >
        {{text}}
      </span>
      <a
        href="#"
        @click="removeTodo"
      >
      <i
        class="material-icons delete-icon"
      >
        delete_forever
      </i>
      </a>
      <span
        class="timestamp"
      >
        {{timestamp}}
      </span>
    </label>
  </div>
</template>

<script>
import axios from 'axios'
import moment from 'moment'

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
      text: this.todo.text,
      lastModified: this.todo.last_modified
    }
  },
  methods: {
    toggleStatus: function () {
      axios.patch('http://localhost:8000/todos/'+this.id+'/', {
        status: this.isDone
      })
        .then(response => {
          this.lastModified = response.data.lastModified
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
    },
    timestamp: function () {
      return moment(this.lastModified).fromNow()
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
.timestamp {
  font-size: 0.9em;
}
.delete-icon {
  vertical-align: middle;
}
</style>
