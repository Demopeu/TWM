<template>
  <div>
    <div class="articleList-box">
      <div class="button-box">
        <div class="Nomal-button" :class="{ 'large-button': selectedCountry === 'Global' }"
        :style="{ 
          border: selectedCountry === 'Global' ? '8px solid #A7A7A7' : '', 
          backgroundColor: selectedCountry === 'Global' ? '#696969' : '#A7A7A7',
          'line-height': selectedCountry === 'Global' ? '4vh' : '6vh'
          }" 
         @click="filterArticles('Global')">Global</div>
        <div class="Nomal-button" 
        :style="{ 
          border: selectedCountry === 'korea' ? '8px solid #F4AFFF' : '', 
          backgroundColor: selectedCountry === 'korea' ? '#9a72a0' : '#F4AFFF',
          'line-height': selectedCountry === 'korea' ? '4vh' : '6vh'
          }"
        @click="filterArticles('korea')">Korea</div>
        <div class="Nomal-button"
        :style="{ 
          border: selectedCountry === 'north-america' ? '8px solid #FFAFAF' : '', 
          backgroundColor: selectedCountry === 'north-america' ? '#b97f7f' : '#FFAFAF',
          'line-height': selectedCountry === 'north-america' ? '4vh' : '6vh'
          }"
       @click="filterArticles('north-america')">N.America</div>
        <div class="Nomal-button"
        :style="{ 
          border: selectedCountry === 'south-america' ? '8px solid #FFEDAF' : '', 
          backgroundColor: selectedCountry === 'south-america' ? '#d1b75a' : '#FFEDAF',
          'line-height': selectedCountry === 'south-america' ? '4vh' : '6vh'
          }"
         @click="filterArticles('south-america')">S.America</div>
        <div class="Nomal-button"
        :style="{ 
          border: selectedCountry === 'europe' ? '8px solid #CFE4C5' : '', 
          backgroundColor: selectedCountry === 'europe' ? '#9cac94' : '#CFE4C5',
          'line-height': selectedCountry === 'europe' ? '4vh' : '6vh'
          }"
        @click="filterArticles('europe')">Europe</div>
        <div class="Nomal-button"
        :style="{ 
          border: selectedCountry === 'india' ? '8px solid #AFBCFF' : '', 
          backgroundColor: selectedCountry === 'india' ? '#868fbe' : '#AFBCFF',
          'line-height': selectedCountry === 'india' ? '4vh' : '6vh'
          }"
        @click="filterArticles('india')">India</div>
        <div class="Nomal-button"
        :style="{ 
          border: selectedCountry === 'china' ? '8px solid #e2f5c8' : '', 
          backgroundColor: selectedCountry === 'china' ? '#a1ad90' : '#e2f5c8',
          'line-height': selectedCountry === 'china' ? '4vh' : '6vh'
          }"
        @click="filterArticles('china')">China</div>
        <div class="Nomal-button"
        :style="{ 
          border: selectedCountry === 'japan' ? '8px solid #FF6767' : '', 
          backgroundColor: selectedCountry === 'japan' ? '#af4848' : '#FF6767',
          'line-height': selectedCountry === 'japan' ? '4vh' : '6vh'
          }"
        @click="filterArticles('japan')">Japan</div>
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
          <button class="pagination-button" @click="prevPage" :disabled="currentPage === 1">이전</button>
          <span class="page-info">Page: {{ currentPage }} / {{ totalPages }}</span>
          <button class="pagination-button" @click="nextPage" :disabled="currentPage === totalPages">다음</button>
        </div>
        <div class="write-button-container">
          <button @click="goCreate" class="write-button">글쓰기</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useCounterStore } from '@/stores/counter';
import ArticleListItem from '@/components/ArticleListItem.vue';
import router from '@/router'

const store = useCounterStore()
const selectedCountry = ref('Global');
const perPage = 10; // 페이지당 보여줄 아티클 수
const currentPage = ref(1); // 현재 페이지
const filteredArticles = ref([]);

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

onMounted(async () => {
  await store.getArticles();
  filteredArticles.value = store.articles;
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
.Nomal-button:hover {
  cursor: pointer;
}
.large-button {
  border: 2px solid 
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