<template>
  <div>
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
          <ArticleListItem
            v-for="article in store.articles"
              :key="article.id"
              :article="article">
          </ArticleListItem>
          <hr>
        </div>
        <div class="write-button-container">
          <button @click="goCreate" class="write-button">글쓰기</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter';
import ArticleListItem from '@/components/ArticleListItem.vue';
import router from '@/router';

const store = useCounterStore()
onMounted(() => {
  store.getArticles()
})

const goCreate = () => router.push({name:'CreateView'})
</script>

<style scoped>

.button-box{
  display: flex;
}
.articleList-box{
  padding-top: 10vh;
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
  margin: 3% auto 1% auto;
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
.write-button-container {
  display: flex;
  justify-content: flex-end;;
  width: 100%;
  margin-right: 5%;
  margin-bottom: 1%;
}

.write-button {
  background-color: #7979e9; /* Dark Blue */
  color: white;
  padding: 10px 20px;
  font-size: 18px;
  font-weight: bold;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  margin: 10px 0;
}
.write-button:hover {
  background-color: #4e4eff; /* Medium Blue for hover effect */
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
</style>