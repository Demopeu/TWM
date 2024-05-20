<template>
    <div class="container min-vw-100 min-vh-100">
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark ">
            <img class="img-logo" src="@/assets/Logo_white.png" alt="Logo_black.png" @click="goidnav">
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav d-flex ms-auto">
            <li class="nav-item">
                <button @click="gocomunav" class="btn btn-outline-light" style="border: black;">게시판</button>
            </li>
            <li class="nav-item">
                <button @click="gopronav" class="btn btn-outline-light" style="border: black;">프로필</button>
            </li>
            <li class="nav-item">
                <button @click="" class="btn btn-outline-light" style="border: black;">로그아웃</button>
            </li>
            </ul>
          </div>
        </nav>
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
                <div v-if="article">
                <h1>{{ article.title }}</h1>
                <hr style="margin: 0.5vh;">
                <div class="content-box">
                  <div style="display: flex;">
                    <h6>{{ article.user.username }}</h6>
                    <h6>{{ article.new_created_at }}</h6>
                  </div>
                  <div style="display: flex;">
                    <h6 class="index-item" >좋아요 : {{ article.like_users_count }}</h6>
                    <h6 class="index-item" >댓글 : {{ article.comment_count }}</h6>
                  </div>
                </div>
                  <h3>{{ article.content }}</h3>
                  <div class="like-button-container">
                    <button class="like-button" @click="store.likeButton(article.id)"></button>
                  </div>
                  <hr style="margin: 0.5vh; color: #2FB2FC; border-width: 2px; border-style: solid;">
                    <div v-if="article.comment_set">
                        <div v-for="comment in article.comment_set" :key="comment.id">
                            <h6>{{ comment.user.username }}</h6>
                            <h6>{{ comment.content }}</h6>
                            <form @submit="store.deleteComment(comment.id)">
                                <input type="submit" value="삭제">
                            </form>
                        </div>
                    </div>
                    <form @submit="createComment">
                        <input type="text" v-model="comment">
                        <input type="submit">
                    </form>
            </div>
        </div>
      </div>
        </div>
    </div>
 
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useRoute } from 'vue-router';
import { useCounterStore } from '@/stores/counter';
import axios from 'axios'
import router from '@/router';

const route = useRoute()
const article = ref(null)
const comment = ref(null)
const store = useCounterStore()

const createComment = function() {
    const payload = {
        userId: article.value.user.id,
        articleId: article.value.id,
        comment: comment.value
    }
    store.createComment(payload)
}


onMounted(() => {
    axios({
        method: 'get',
        url: `http://127.0.0.1:8000/community/articles/${route.params.articleId}/`
    })
    .then((response) => {
        console.log(response.data)
        article.value = response.data
    })
    .catch((error) => {
        console.log(error)
    })
})



</script>

<style scoped>
.container {
  background-color: #E9FCE7;
  width: 100%;
  height: 100vh;
  overflow-y: auto;
  padding: 0;
}
.content-box{
  display: flex;
  justify-content: space-between;
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
  margin: 3% auto;
  min-height: 90%;
}
.button-box{
  display: flex;
  margin-top: 20px;
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

.navbar-brand {
  font-size: 1.5em;
}

.navbar-nav .nav-link {
  color: #fff !important;
  font-size: 1.2em;
  padding: 10px 20px;
}

.navbar-nav .nav-item {
  margin-left: 10px;
}

.navbar {
  width: 100vw;
  padding: 0;
}

.img-logo {
  
  width: 190px;
  height: 70px;
  padding: 0;
}
h1 {
  font-weight: bold;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  padding-top: 1vh;
  padding-left: 2vh;
}
h3{
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  padding-left: 2vh;
  padding-top: 3vh;
  letter-spacing: -2px;
}
h6 {
  font-weight: bold;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  padding-right: 5vh;
  padding-left: 2vh;
  padding-top: 0;
}

.like-button-container {
  display: flex;
  justify-content: center;
  margin-top: 5vh;
  margin-bottom: 5vh;
}

.like-button {
  position: relative;
  padding: 40px;
  font-size: 14px;
  background-color: #5EB9EC;
  color: white;
  border: none;
  border-radius: 50%; /* 동그랗게 만듭니다 */
  cursor: pointer;
}

.like-button::before {
  content: "\2605"; /* 별 아이콘 유니코드 */
  position: absolute;
  top: 30%;
  left: 50%;
  transform: translate(-50%, -50%); /* 가운데로 이동 */
  font-size: 50px;
}

.like-button::after {
  content: "좋아요";
  position: absolute;
  top: 70%;
  left: 50%;
  transform: translate(-50%, -15%);
  white-space: nowrap;
}

</style>