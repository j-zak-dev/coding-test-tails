<script setup lang="ts">
const props = defineProps<{
  placeholder: string
}>()

const model = defineModel<string>({ default: '' })

const emit = defineEmits<{
  submit: []
}>()

function onSubmit() {
  emit('submit')
}
</script>

<template>
  <form class="search-form" @submit.prevent="onSubmit">
    <input v-model="model" type="text" :placeholder="props.placeholder" />
    <button type="submit">Search</button>
  </form>
</template>