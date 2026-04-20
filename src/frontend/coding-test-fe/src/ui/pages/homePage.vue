
<script setup lang="ts">
import { onBeforeUnmount, onMounted, ref, watch } from 'vue'

import { StoreService } from '../../application/services/storeService'
import type { Store, RichStore } from '../../domain/aggregates/Store'
import { ApiStoreRepository } from '../../infrastructure/repositories/ApiStoreRepository'
import searchBar from '../components/searchBar.vue'
import storeList from '../components/storeList.vue'
import titleAndSubText from '../components/titleAndSubText.vue'
import { debounce } from 'lodash'

const searchSuggestions = ref<Store[]>([])
const stores = ref<RichStore[]>([])
const loading = ref(false)
const errorMessage = ref('')
const nameSearchQuery = ref('')
const suggestionNamesQueue = ref<string[]>([])
const nextSliceStartIndex = ref(0)
const hasMoreSlices = ref(false)

const PAGE_SIZE = 3
const PREFETCH_OFFSET_PX = 500

const apiBaseUrl = import.meta.env.VITE_API_URL ?? 'http://127.0.0.1:8000'
const storeService = new StoreService(new ApiStoreRepository(apiBaseUrl))

watch(nameSearchQuery, async (value) => {
  if (!value.trim()) {
    searchSuggestions.value = []
    resetLazyLoadingState()
  }
  await debouncedSearchStoresByName(value)
})

const debouncedSearchStoresByName = debounce(async (name: string) => {
  if (!name.trim()) {
    searchSuggestions.value = []
    return
  }

  try {
    searchSuggestions.value = await storeService.searchStoresByName(name)
    console.log('Search suggestions updated:', searchSuggestions.value.slice(0, 3))
  } catch {
    errorMessage.value = 'Failed to update suggestions. Please try again.'
  }
}, 100)

function resetLazyLoadingState() {
  stores.value = []
  suggestionNamesQueue.value = []
  nextSliceStartIndex.value = 0
  hasMoreSlices.value = false
}

function initializeLazyLoadingQueue() {
  suggestionNamesQueue.value = searchSuggestions.value.map((store) => store.name)
  nextSliceStartIndex.value = 0
  hasMoreSlices.value = suggestionNamesQueue.value.length > 0
  stores.value = []
}

async function loadNextStoresSlice() {
  if (loading.value || !hasMoreSlices.value) {
    return
  }

  const currentStart = nextSliceStartIndex.value
  const currentEnd = currentStart + PAGE_SIZE
  const storeNamesSlice = suggestionNamesQueue.value.slice(currentStart, currentEnd)

  if (storeNamesSlice.length === 0) {
    hasMoreSlices.value = false
    return
  }

  loading.value = true
  errorMessage.value = ''

  try {
    const enrichedStores = await storeService.getEnrichedStoresByNames(storeNamesSlice)
    stores.value = [...stores.value, ...enrichedStores]
    nextSliceStartIndex.value = currentEnd
    hasMoreSlices.value = nextSliceStartIndex.value < suggestionNamesQueue.value.length
  } catch {
    errorMessage.value = 'Failed to load stores. Please try again.'
  } finally {
    loading.value = false

    if (hasMoreSlices.value && shouldPrefetchNextSlice()) {
      void loadNextStoresSlice()
    }
  }
}

async function getEnrichedStores() {
  initializeLazyLoadingQueue()
  await loadNextStoresSlice()
}

function isNearBottomOfPage(): boolean {
  return shouldPrefetchNextSlice()
}

function shouldPrefetchNextSlice(): boolean {
  const scrollPosition = window.innerHeight + window.scrollY
  const distanceToBottom = document.documentElement.scrollHeight - scrollPosition
  return distanceToBottom <= PREFETCH_OFFSET_PX
}

function onWindowScroll() {
  if (isNearBottomOfPage()) {
    void loadNextStoresSlice()
  }
}

onMounted(() => {
  window.addEventListener('scroll', onWindowScroll, { passive: true })
})

onBeforeUnmount(() => {
  window.removeEventListener('scroll', onWindowScroll)
})

</script>

<template>
  <titleAndSubText
    title="Welcome to the coding test!"
    subText="This is the home page. You can find the instructions for the test in the README file."
  />
  <searchBar v-model="nameSearchQuery" :suggestions="searchSuggestions" placeholder="Search for stores by name..." @submit="getEnrichedStores" />

  <storeList v-if="!errorMessage" :stores="stores" />

  <p v-if="loading && stores.length === 0">Loading stores...</p>
  <p v-if="loading && stores.length > 0">Loading more stores...</p>
  <p v-if="errorMessage">{{ errorMessage }}</p>
</template>

<style scoped>

body p {
  color: white;
}

</style>