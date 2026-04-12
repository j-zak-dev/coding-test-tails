<script setup lang="ts">
defineProps<{
  placeholder: string
}>()
</script>

<template>
  <input type="text" :placeholder="placeholder" />
</template>