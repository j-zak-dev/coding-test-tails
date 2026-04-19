<script setup lang="ts">

import type { RichStore } from '../../domain/aggregates/Store'
import StoreItem from './storeItem.vue'

defineProps<{
  stores: RichStore[]
}>()
</script>

<template>
  <div class="store-list">
    <h2>Store List</h2>
    <ul>
      <li v-for="store in stores" :key="store.name">
        <StoreItem :store="store" />
      </li>
    </ul>
  </div>
</template>

<style scoped>
.store-list {
  padding-top: 32px;
  max-width: 51%;
  margin: 0 auto;
  font-family: 'Courier New', Courier, monospace;
  color: white;
}
.store-list h2 {
  text-align: center;
  margin-bottom: 24px;
}
.store-list ul {
  list-style-type: none;
  padding: 0;
  animation: fadeIn 0.5s ease-in-out;
}
.store-list li {
  margin-bottom: 16px;
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