
<script setup lang="ts">
import { ref, watch } from 'vue'

import { StoreService } from '../../application/services/storeService'
import type { Store, RichStore } from '../../domain/aggregates/Store'
import { ApiStoreRepository } from '../../infrastructure/repositories/ApiStoreRepository'
import searchBar from '../components/searchBar.vue'
import storeList from '../components/storeList.vue'
import titleAndSubText from '../components/titleAndSubText.vue'

const searchSuggestions = ref<Store[]>([])
const stores = ref<RichStore[]>([])
const loading = ref(false)
const errorMessage = ref('')
const nameSearchQuery = ref('')

const apiBaseUrl = import.meta.env.VITE_API_URL ?? 'http://127.0.0.1:8000'
const storeService = new StoreService(new ApiStoreRepository(apiBaseUrl))

watch(nameSearchQuery, async (value) => {
  await searchStoresByName(value)
})

async function searchStoresByName(name: string) {
  if (!name.trim()) {
    searchSuggestions.value = []
    return
  }

  try {
    searchSuggestions.value = await storeService.searchStoresByName(name)
  } catch {
    errorMessage.value = 'Failed to update suggestions. Please try again.'
  }
}

async function getEnrichedStores() {
  loading.value = true
  errorMessage.value = ''
  try {
    stores.value = await storeService.getEnrichedStores(nameSearchQuery.value)
  } catch {
    errorMessage.value = 'Failed to load stores. Please try again.'
  } finally {
    loading.value = false
  }
}

</script>

<template>
  <titleAndSubText
    title="Welcome to the coding test!"
    subText="This is the home page. You can find the instructions for the test in the README file."
  />
  <searchBar v-model="nameSearchQuery" :suggestions="searchSuggestions" placeholder="Search for stores by name..." @submit="getEnrichedStores" />
  <p v-if="loading">Loading stores...</p>
  <p v-if="errorMessage">{{ errorMessage }}</p>
  <storeList v-if="!loading && !errorMessage" :stores="stores" />
</template>