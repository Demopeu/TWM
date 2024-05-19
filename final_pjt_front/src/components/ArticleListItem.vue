<template>
  <div>
    <RouterLink :to="{ name: 'DetailView', params: { articleId: article.id} }">
      <span>{{ article.id }}</span>
      <span>{{ article.title }}</span>
      <span>{{ article.user.id }}</span>
      <span>{{ article.created_at }}</span>
    </RouterLink>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';

defineProps({
  article: Object
})


</script>

<style scoped>

</style>