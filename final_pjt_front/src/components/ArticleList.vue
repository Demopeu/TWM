<template>
  <div>
    <div class="articleList-box">
      <div class="button-box">
        <div class="Nomal-button" style="background-color: #A7A7A7;" @click="filterArticles('Global')">Global</div>
        <div class="Nomal-button" style="background-color: #FFAFAF;" @click="filterArticles('north-america')">N.America</div>
        <div class="Nomal-button" style="background-color: #FFEDAF;" @click="filterArticles('south-america')">S.America</div>
        <div class="Nomal-button" style="background-color: #CFE4C5;" @click="filterArticles('europe')">Europe</div>
        <div class="Nomal-button" style="background-color: #AFBCFF;" @click="filterArticles('india')">India</div>
        <div class="Nomal-button" style="background-color: #e2f5c8;" @click="filterArticles('china')">China</div>
        <div class="Nomal-button" style="background-color: #F4AFFF;" @click="filterArticles('korea')">Korea</div>
        <div class="Nomal-button" style="background-color: #FF6767;" @click="filterArticles('japan')">Japan</div>
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
            v-for="article in currentPageArticles"
            :key="article.id"
            :article="article">
          </ArticleListItem>
          <hr>
        </div>
        <div class="pagination-buttons">
          <button class="pagination-button" @click="prevPage" :disabled="currentPage === 1">Previous</button>
          <span class="page-info">Page: {{ currentPage }} / {{ totalPages }}</span>
          <button class="pagination-button" @click="nextPage" :disabled="currentPage === totalPages">Next</button>
        </div>
        <div class="write-button-container">
          <button @click="goCreate" class="write-button">글쓰기</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted,computed } from 'vue'
import { useCounterStore } from '@/stores/counter';
import ArticleListItem from '@/components/ArticleListItem.vue';
import router from '@/router'

const store = useCounterStore()
const selectedCountry = ref('Global');
const perPage = 10; // 페이지당 보여줄 아티클 수
const currentPage = ref(1); // 현재 페이지

const filteredArticles = computed(() => {
  if (selectedCountry.value === 'Global') {
    return store.articles;
  }
  return store.articles.filter(article => article.country === selectedCountry.value);
});

const totalPages = computed(() => Math.ceil(filteredArticles.value.length / perPage));

const currentPageArticles = computed(() => {
  const startIndex = (currentPage.value - 1) * perPage;
  const endIndex = startIndex + perPage;
  return filteredArticles.value.slice(startIndex, endIndex);
});

const filterArticles = (country) => {
  selectedCountry.value = country;
};

const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--;
  }
};

const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++;
  }
};

onMounted(() => {
  store.getArticles();
});

const goCreate = () => router.push({ name: 'CreateView' });
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

.pagination-buttons {
  display: flex;
  align-items: center;
}

.pagination-button {
  background-color: #7979e9; /* Green */
  border: none;
  color: white;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  border-radius: 5px;
}

.pagination-button:hover {
  background-color: #45a049;
}

.page-info {
  margin: 0 10px;
  font-size: 16px;
}
</style>