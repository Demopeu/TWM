<template>
  <div>
    <RouterLink :to="{ name: 'DetailView', params: { articleId: article.id} }">
      <span>{{ article.id }}</span> |
      <span>{{ article.title }}</span> |
      <span>{{ article.user.username }}</span> |
      <span>{{ article.new_created_at }}</span> |
      <div v-if="article.created_at !== article.updated_at">
        수정됨!
      </div>
      <span>{{ article.like_users_count }}</span>
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