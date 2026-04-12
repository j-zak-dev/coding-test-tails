

<script setup lang="ts">
import titleAndSubText from '../components/titleAndSubText.vue'
import searchBar from '../components/searchBar.vue'
import storeList from '../components/storeList.vue'
</script>

<template>
  <titleAndSubText
    title="Welcome to the coding test!"
    subText="This is the home page. You can find the instructions for the test in the README file."
  />
  <searchBar placeholder="Search for stores..." />
  <storeList :stores="[
    { name: 'Store 1', postcode: 'ABC 123' },
    { name: 'Store 2', postcode: 'DEF 456' },
    { name: 'Store 3', postcode: 'GHI 789' }
  ]" />
</template>