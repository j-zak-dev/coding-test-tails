<script setup lang="ts">
import type { RichStore } from '../../domain/aggregates/Store'

defineProps<{
  store: RichStore
}>()

</script>

<template>
    <div class="store-item-wrapper">
        <div class="store-item">
            <h3>{{ store.name }}</h3>
            <p>Postal Code: {{ store.postalCode }}</p>
            <p>Latitude: {{ store.coordinates?.latitude ?? 'N/A' }}</p>
            <p>Longitude: {{ store.coordinates?.longitude ?? 'N/A' }}</p>
        </div>
    </div>
</template>

<style scoped>
.store-item {
  border: 1px solid #ccc;
  border-radius: 50px;
  padding: 30px;
  margin-bottom: 8px;
  font-family: 'Courier New', Courier, monospace;
}

.store-item h3 {
    font-size: x-large;
}
</style>