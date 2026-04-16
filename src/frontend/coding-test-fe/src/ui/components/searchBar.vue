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
}

.search-form input {
  flex: 1;
  padding: 8px;
  font-size: 16px;
  border-radius: 10px;
  width: 50%;
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
}

.dropdown {
  position: relative;
  display: block;
  max-height: 200px;
  overflow-y: auto;
  width: 50%;
}

.search-suggestion:hover {
  background-color: #e0e0e0;
  cursor: pointer;
}
</style>