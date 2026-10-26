
<script setup>

import { ref, onMounted } from 'vue'

const API_URL = 'https://rs-vjezba1-backend.onrender.com'

const tasks = ref([])
const newTask = ref('')

async function loadTasks() {
  const response = await fetch(`${API_URL}/tasks`)
  tasks.value = await response.json()
}

async function addTask() {
  const title = newTask.value.trim()
  if (!title) return

  const response = await fetch(`${API_URL}/tasks`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ title })
  })

  if (!response.ok) return

  newTask.value = ''
  await loadTasks()
}

async function deleteTask(id) {
  const response = await fetch(`${API_URL}/tasks/${id}`, {
    method: 'DELETE'
  })

  if (response.ok) {
    await loadTasks()
  }
}

async function updateTask(task) {
  await fetch(`${API_URL}/tasks/${task.id}`, {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ completed: task.completed })
  })
}

onMounted(loadTasks)

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
          <input
  type="checkbox"
  v-model="task.completed"
  @change="updateTask(task)"
/>
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
