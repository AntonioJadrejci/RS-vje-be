
<script setup>
import { ref } from 'vue'

const tasks = ref([
  { id: 1, title: 'Naučiti HTTP protokol', completed: false },
  { id: 2, title: 'Napraviti REST API', completed: false }
])

const newTask = ref('')

function addTask() {
  const title = newTask.value.trim()

  if (!title) return

  tasks.value.push({
    id: Date.now(),
    title: title,
    completed: false
  })

  newTask.value = ''
}

function deleteTask(id) {
  tasks.value = tasks.value.filter(task => task.id !== id)
}
</script>

<template>
  <main class="container">
    <h1>My Task Manager</h1>
    <p>Raspodijeljeni sustavi - Vježba 1</p>

    <div class="input-group">
      <input
        v-model="newTask"
        placeholder="Unesi novi zadatak..."
        @keyup.enter="addTask"
      />
      <button @click="addTask">Dodaj</button>
    </div>

    <ul>
      <li v-for="task in tasks" :key="task.id">
        <label>
          <input type="checkbox" v-model="task.completed" />
          <span :class="{ completed: task.completed }">
            {{ task.title }}
          </span>
        </label>

        <button class="delete" @click="deleteTask(task.id)">
          Obriši
        </button>
      </li>
    </ul>
  </main>
</template>

<style scoped>
.container {
  max-width: 650px;
  margin: 60px auto;
  padding: 30px;
  font-family: Arial, sans-serif;
}

h1 {
  color: #42b883;
}

.input-group {
  display: flex;
  gap: 10px;
  margin: 25px 0;
}

.input-group input {
  flex: 1;
  padding: 12px;
}

button {
  padding: 10px 16px;
  background: #42b883;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

li {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 10px 0;
  padding: 12px;
  background: #f1f1f1;
  color: #222;
  border-radius: 5px;
}

.completed {
  text-decoration: line-through;
  color: gray;
}

.delete {
  background: #e74c3c;
}
</style>
