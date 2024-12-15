<template>
  <div id="app">
    <Header />
    <RouterView />
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';
import Header from './components/Header.vue';

const router = useRouter()
router.push("/")

</script>

<style scoped>

</style>
