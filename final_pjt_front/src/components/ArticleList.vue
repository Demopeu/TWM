<template>
  <div>
    <div class="logo-box">
      <img class="img-logo" src="@/assets/Logo_black.png" alt="Logo_black.png">
    </div>
    <div class="articleList-box">
      <div class="button-box">
      <div class="Nomal-button" style="background-color: #A7A7A7;">Global</div>
      <div class="Nomal-button" style="background-color: #FFAFAF;">N.America</div>
      <div class="Nomal-button" style="background-color: #FFEDAF;">S.America</div>
      <div class="Nomal-button" style="background-color: #CFE4C5;">Europe</div>
      <div class="Nomal-button" style="background-color: #AFBCFF;">India</div>
      <div class="Nomal-button" style="background-color: #F4AFFF;">Korea</div>
      <div class="Nomal-button" style="background-color: #FF6767;">Japan</div>
      </div>
      <div class="articleList-List-box">
        <div class="articleList-List-box-in">
          <div class="index-box">
            <span class="index-item" style="flex: 2">번호</span>
            <span class="index-item" style="flex: 3">제목</span>
            <span class="index-item" style="flex: 2">글쓴이</span>
            <span class="index-item" style="flex: 2">작성일</span>
            <span class="index-item" style="flex: 1">좋아요</span>
          </div>
          <div class="index-box" style="background-color: white;"> 
            <ArticleListItem
              v-for="article in store.articles"
              :key="article.id"
              :article="article"
            />
              <!-- <span class="index-item" style="flex: 2">{{ article.id }}</span>
              <span class="index-item" style="flex: 3">{{ article.title }}</span>
              <span class="index-item" style="flex: 2">{{ article.user.id }}</span>
              <span class="index-item" style="flex: 2">{{ article.created_at }}</span>
              <span v-if="article.likes"  class="index-item" style="flex: 1">{{ article.likes.length }}</span> -->
          </div>
          <hr>
        </div>
      </div>
      
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter';
import ArticleListItem from '@/components/ArticleListItem.vue';

const store = useCounterStore()
onMounted(() => {
  store.getArticles()
})
</script>

<style scoped>

.logo-box {
  margin-bottom: 20px;
}
.button-box{
  display: flex;
}
.articleList-box{
  width: 80%;
  height: 100%;
  margin-left: auto;
  margin-right: auto;
}
.articleList-List-box {
  background-color: #D9D9D9;
  width: 100%;
  min-width: 75vh;
  border-radius: 1vw;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.articleList-List-box-in{
  background-color: white;
  width: 95%;
  border-radius: 1vw;
  margin: 3% auto;
  min-height: 90%;
}
.index-box{
  width: 95%;
  height: 5vh;
  background-color: #D9D9D9;
  margin: 2vh auto;
  display: flex;
  justify-content: space-around;
  align-items: center;
}
.index-item {
  font-weight: 1000;
  text-align: center;
}
.Nomal-button {
  width: 10%;
  height: 6vh;
  margin-left: 2vh;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
  text-align: center;
  line-height: 6vh;
  font-weight: bold;
  display: inline-block;
  text-overflow: ellipsis;
  font-size: 24px;
  white-space: nowrap;
  text-overflow: ellipsis;
}

@media screen and (max-width: 1800px) {
  .Nomal-button {
    font-size: 20px; /* 변경할 폰트 크기 */
  }
}

@media screen and (max-width: 1400px) {
  .Nomal-button {
    overflow: hidden;
    text-overflow: ellipsis;
  }
}
.img-logo {
  
  width: 19vh;
  height: 7vh;
  margin-left: 5vh;
  margin-top: 30px;
}
</style>