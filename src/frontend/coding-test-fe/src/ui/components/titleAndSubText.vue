
<script setup lang="ts">
defineProps<{
  title: string
  subText: string
}>()
</script>

<template>
  <div class="home-page">
    <h1>{{ title }}</h1>
    <p>{{ subText }}</p>
  </div>
</template>