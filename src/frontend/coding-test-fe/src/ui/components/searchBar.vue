<script setup lang="ts">
import type { Store } from '../../domain/aggregates/Store'

const props = defineProps<{
  placeholder: string
  suggestions?: Store[]
}>()

const model = defineModel<string>({ default: '' })

const emit = defineEmits<{
  submit: []
}>()

function onSubmit() {
  emit('submit')
  model.value = ''
}

function onSuggestionClick(suggestion: Store) {
  model.value = suggestion.name
  onSubmit()
}

</script>

<template>
  <form class="search-form" @submit.prevent="onSubmit">
    <input v-model="model" type="text" :placeholder="props.placeholder" />
    <div class="dropdown">
      <ul class="search-suggestions" v-if="model">
        <li class="search-suggestion" v-for="suggestion in props.suggestions" :key="suggestion.name" @click="onSuggestionClick(suggestion)">{{ suggestion.name }}</li>
      </ul>
    </div>
  </form>
</template>

<style scoped>
.search-form {
  display: block;
  gap: 8px;
  margin: 16px auto;
  text-align: center;
}

.search-form input {
  flex: 1;
  padding: 10px;
  font-size: 16px;
  border-radius: 10px;
  border-width: 3px;
  border-color: white;
  width: 50%;
  background: transparent;
  appearance: none;
  color: white;
}

.search-form input::placeholder {
  color: white;
  opacity: 1;
}

.search-suggestions {
  list-style: none;
  margin: 0;
  padding: 0;
}

.search-suggestions li {
  padding: 8px;
  background-color: #f0f0f0;
  border-bottom: 1px solid #ccc;
  animation: fadeIn 0.1s ease-in-out;
  background-color: rgba(37, 37, 37);
  color: white;
  border-radius: 20px;
 
}

.dropdown {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  display: block;
  max-height: 200px;
  overflow-y: auto;
  width: 50%;
  margin:auto;
}

.dropdown::-webkit-scrollbar {
  display: none;              /* Chrome, Safari */
}

.search-suggestion:hover {
  background-color: #000000;
  cursor: pointer;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
</style>