<template>
  <div class="index-box-in">
    <RouterLink :to="{ name: 'DetailView', params: { articleId: article.id } }" class="index-link">
      <span class="index-item" style="flex: 2">{{ article.id }}</span>
      <span class="index-item" style="flex: 3">{{ article.title }}</span>
      <span class="index-item" style="flex: 2">{{ article.user.username }}</span>
      <span class="index-item" style="flex: 2">{{ article.new_created_at }}</span>
      <span class="index-item" style="flex: 1">{{ article.like_users_count }}</span>

    </RouterLink>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';

const props = defineProps({
  article: Object
})

</script>

<style scoped>

.index-box-in{
  width: 95%;
  height: 5vh;
  background-color: white;
  margin: 2vh auto;
  display: flex;
  justify-content: space-around;
  align-items: center;
}

.index-link {
  display: flex;
  flex: 1;
  text-decoration: none;
  color: inherit;
}
.index-item {
  font-weight: 1000;
  text-align: center;
}
</style>