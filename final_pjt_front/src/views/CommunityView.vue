<template>
  <div class="container min-vw-100 min-vh-100" >
    <ArticleList />
  </div>
</template>

<script setup>
import ArticleList from '@/components/ArticleList.vue';

</script>

<style scoped>
.container {
  background-color: #E9FCE7;
  width: 100%;
  height: 100vh;
  overflow-y: auto;
}
</style>