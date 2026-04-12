<script setup lang="ts">
import type { Store } from '../../domain/aggregates/Store'

defineProps<{
  stores: Store[]
}>()
</script>

<template>
  <div class="store-list">
    <h2>Store List</h2>
    <ul>
      <li v-for="store in stores" :key="store.name">
        {{ store.name }} - {{ store.postalCode }}
      </li>
    </ul>
  </div>
</template>