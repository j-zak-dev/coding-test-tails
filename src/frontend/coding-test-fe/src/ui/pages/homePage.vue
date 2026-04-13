
<script setup lang="ts">
import { onMounted, ref } from 'vue'

import { StoreService } from '../../application/services/storeService'
import type { Store } from '../../domain/aggregates/Store'
import { ApiStoreRepository } from '../../infrastructure/repositories/ApiStoreRepository'
import searchBar from '../components/searchBar.vue'
import storeList from '../components/storeList.vue'
import titleAndSubText from '../components/titleAndSubText.vue'

const stores = ref<Store[]>([])
const loading = ref(false)
const errorMessage = ref('')
const nameSearchQuery = ref('')
const postalCodeSearchQuery = ref('')

const apiBaseUrl = import.meta.env.VITE_API_URL ?? 'http://127.0.0.1:8000'
const storeService = new StoreService(new ApiStoreRepository(apiBaseUrl))

async function searchStoresByName() {
  loading.value = true
  errorMessage.value = ''
  try {
    stores.value = await storeService.searchStoresByName(nameSearchQuery.value)
  } catch {
    errorMessage.value = 'Search failed. Please try again.'
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
  <searchBar v-model="nameSearchQuery" placeholder="Search for stores by name..." @submit="searchStoresByName" />
  <p v-if="loading">Loading stores...</p>
  <p v-if="errorMessage">{{ errorMessage }}</p>
  <storeList v-if="!loading && !errorMessage" :stores="stores" />
</template>