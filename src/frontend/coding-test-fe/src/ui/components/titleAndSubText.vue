
<script setup lang="ts">
defineProps<{
  title: string
  subText: string
}>()
</script>

<template>
  <div class="title-subtext-wrapper">
    <h1>{{ title }}</h1>
    <p>{{ subText }}</p>
  </div>
</template>

<style scoped>
.title-subtext-wrapper {
  text-align: center;
  margin: 32px auto;
  color: white;
  font-family: 'Courier New', Courier, monospace;
}
</style>