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
          <div v-for="article in articles"
          :key="article.id">
          <div class="index-box" style="background-color: white;">
            <span class="index-item" style="flex: 2">{{ article.id }}</span>
            <span class="index-item" style="flex: 3">{{ article.title }}</span>
            <span class="index-item" style="flex: 2">{{ article.account_id }}</span>
            <span class="index-item" style="flex: 2">{{ article.created_at }}</span>
            <span v-if="article.likes"  class="index-item" style="flex: 1">{{ article.likes.length }}</span>
          </div>
          <hr>
          </div>
        </div>
      </div>
      
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
const articles = ref(
  [{id: '1', title: '라라랜드 영화 촬영지 여행', account_id: '고등어아저씨', created_at: '2021-09-01',likes: [{id: '1', account_id: '고등어아저씨'}]},
  {id: '2', title: '라라랜드 영화 촬영지 여행', account_id: '고등어아저씨', created_at: '2021-09-01',likes: [{id: '1', account_id: '고등어아저씨'}]},
  {id: '3', title: '라라랜드 영화 촬영지 여행', account_id: '고등어아저씨', created_at: '2021-09-01',likes: [{id: '1', account_id: '고등어아저씨'}]},
  {id: '4', title: '라라랜드 영화 촬영지 여행', account_id: '고등어아저씨', created_at: '2021-09-01',likes: [{id: '1', account_id: '고등어아저씨'}]},
  {id: '5', title: '라라랜드 영화 촬영지 여행', account_id: '고등어아저씨', created_at: '2021-09-01',likes: [{id: '1', account_id: '고등어아저씨'}]},
  {id: '6', title: '라라랜드 영화 촬영지 여행', account_id: '고등어아저씨', created_at: '2021-09-01',likes: [{id: '1', account_id: '고등어아저씨'}]},
  {id: '7', title: '라라랜드 영화 촬영지 여행', account_id: '고등어아저씨', created_at: '2021-09-01',likes: [{id: '1', account_id: '고등어아저씨'}]},
  {id: '8', title: '라라랜드 영화 촬영지 여행', account_id: '고등어아저씨', created_at: '2021-09-01',likes: [{id: '1', account_id: '고등어아저씨'}]},
  {id: '9', title: '라라랜드 영화 촬영지 여행', account_id: '고등어아저씨', created_at: '2021-09-01',likes: [{id: '1', account_id: '고등어아저씨'}]},
  {id: '10', title: '라라랜드 영화 촬영지 여행', account_id: '고등어아저씨', created_at: '2021-09-01',likes: [{id: '1', account_id: '고등어아저씨'}]},
  {id: '11', title: '라라랜드 영화 촬영지 여행', account_id: '고등어아저씨', created_at: '2021-09-01',likes: [{id: '1', account_id: '고등어아저씨'}]},
  {id: '12', title: '라라랜드 영화 촬영지 여행', account_id: '고등어아저씨', created_at: '2021-09-01',likes: [{id: '1', account_id: '고등어아저씨'}]},
  {id: '13', title: '라라랜드 영화 촬영지 여행', account_id: '고등어아저씨', created_at: '2021-09-01',likes: [{id: '1', account_id: '고등어아저씨'}]},
  {id: '14', title: '라라랜드 영화 촬영지 여행', account_id: '고등어아저씨', created_at: '2021-09-01',likes: [{id: '1', account_id: '고등어아저씨'}]},
  {id: '15', title: '라라랜드 영화 촬영지 여행', account_id: '고등어아저씨', created_at: '2021-09-01',likes: [{id: '1', account_id: '고등어아저씨'}]},
  {id: '16', title: '라라랜드 영화 촬영지 여행', account_id: '고등어아저씨', created_at: '2021-09-01',likes: [{id: '1', account_id: '고등어아저씨'}]},
])
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