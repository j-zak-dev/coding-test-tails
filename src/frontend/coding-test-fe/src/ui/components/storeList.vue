<script setup lang="ts">
defineProps<{
  stores: Array<{ name: string; postcode: string }>
}>()
</script>

<template>
  <div class="store-list">
    <h2>Store List</h2>
    <ul>
      <li v-for="store in stores" :key="store.name">
        {{ store.name }} - {{ store.postcode }}
      </li>
    </ul>
  </div>
</template>