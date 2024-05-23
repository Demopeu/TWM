<template>
  <div class="container min-vw-100 min-vh-100">
      <nav class="navbar navbar-expand-lg navbar-dark bg-dark ">
          <img class="img-logo" src="@/assets/Logo_white.png" alt="Logo_black.png">
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav d-flex ms-auto">
          <li class="nav-item">
              <button @click.prevent="gocomunav" class="btn btn-outline-light" style="border: black;">게시판</button>
          </li>
          <li class="nav-item">
              <button @click="gopronav(article.user.id)" class="btn btn-outline-light" style="border: black;">프로필</button>
          </li>
          <li class="nav-item">
              <button @click="logout" class="btn btn-outline-light" style="border: black;">로그아웃</button>
          </li>
          <li class="nav-item">
                <button @click="goback" class="btn btn-outline-light" style="border: black;">뒤로가기</button>
            </li>
          </ul>
        </div>
      </nav>
      <div class="articleList-box">
          <div class="button-box">
          <div class="Nomal-button" style="background-color: #afdbff; cursor: pointer;" @click="goUpdatePage(article.id)">수정</div>
          <div class="Nomal-button" style="background-color: #FF6767; cursor: pointer;" @click="store.deleteArticle(article.id)">삭제</div>
          </div>
          <div class="articleList-List-box">
          <div class="articleList-List-box-in">
              <div v-if="article">
              <h1>{{ article.title }}</h1>
              <hr style="margin: 0.5vh;">
              <div class="content-box">
                <div style="display: flex;">
                  <RouterLink :to="{ name: 'ProfileView', params: { userId: article.user.id } }">
                    <h6>{{ article.user.username }}</h6>
                  </RouterLink>
                  <h6>{{ article.new_created_at }}</h6>
                </div>
                <div style="display: flex;">
                  <h6 class="index-item" >좋아요 : {{ likeCountNumber}}</h6>
                  <h6 class="index-item" >댓글 : {{ article.comment_count }}</h6>
                </div>
              </div>
                <h4>{{ article.content }}</h4>
                <div class="like-button-container">
                  <button class="like-button" @click.prevent=pdtbutton(article.id)></button>
                </div>
                <hr style="margin: 0.5vh; color: #2FB2FC; border-width: 2px; border-style: solid;">
                <div v-if="commentList.length">
                  <div v-for="comment in commentList" :key="comment.id" style="margin-top: 1vh;">
                    <div style="display: flex;">
                      <h6 style="flex: 1;">{{ comment.user.username }}</h6>
                      <h6 style="flex: 4;">{{ comment.content }}</h6>
                      <form @submit.prevent="deleteComment(comment.id)" style="flex: 0.5;">
                        <input type="submit" value="X" style="height: 3vh; width: auto;">
                      </form>
                    </div>
                    <hr>
                  </div>
                </div>
                <div v-else style="margin-top: 1vh;">
                  <h6>첫 댓글을 달아주세요!</h6>
                </div>
                  <form @submit.prevent="createComment" style="margin: 1vh 0 1vh 2vh;">
                      <input type="text" v-model="comment" style="width: 70%; border-radius: 5vh;">
                      <input type="submit" style="margin-left: 3vh;" class="write-button">
                  </form>
          </div>
      </div>
    </div>
      </div>
  </div>

</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useRoute, RouterLink,useRouter } from 'vue-router';
import { useCounterStore } from '@/stores/counter';
import axios from 'axios'
import router from '@/router';
import { useToast } from 'vue-toastification'

const toast = useToast()
const store = useCounterStore()
const route = useRoute()
const article = ref(null)
const comment = ref(null)
const likeCountNumber = ref(0)
const commentList = ref([])
const routers = useRouter()

const fetchArticleData = () => {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/community/articles/${route.params.articleId}/`
  })
  .then((response) => {
    article.value = response.data
    likeCountNumber.value = article.value.like_users_count
    commentList.value = response.data.comment_set
    console.log(commentList.value)
  })
  .catch((error) => {
    console.log(error)
  })
}

const createComment = async () => {
  const payload = {
    userId: article.value.user.id,
    articleId: article.value.id,
    comment: comment.value
  };
  try {
    await store.createComment(payload)
    comment.value = ''
    await fetchArticleData()
  } catch (error) {
    console.log(error)
  }
}

const deleteComment = async (commentId) => {
  // for (const comment of commentList.value) {
  //   console.log(comment.id === commentId)
  //   if (comment.id === commentId) {
  //     console.log(comment.user.username)
      
  //   }
  //   }
  if (article.value.user.id === store.username) {
  try {
    await store.deleteComment(commentId)
    await fetchArticleData()
  } catch (error) {
    console.log(error)
  }
}
else {
  toast.error('댓글 삭제 권한이 없습니다.')
}
}

const goUpdatePage = (articleId) => {
  console.log(article.value.user.id)
  if (article.value.user.id === store.userId) {
  router.push({ name: 'UpdateView', params: { articleId: articleId } })
  }
  else {
    toast.error('수정 권한이 없습니다.')
  }
}

const pdtbutton = async (articleId) => {
  try {
    await store.likeButton(articleId)
    await fetchArticleData()
  } catch (error) {
    console.log(error)
  }
};

onMounted(fetchArticleData)

const goidnav = ()=>{
  store.goIndexNav()
}
const gocomunav = ()=>{
  console.log('gocomunav 확인')
  store.goCommunityNav()
}
const gopronav = (useId)=>{
  store.goProfileNav(useId)
}
const logout = ()=>{
store.logout()
}

const goback =()=>{
  routers.go(-1)
}
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
padding-top: 2vh;
padding-left: 3vh;
padding-bottom: 1vh;
}
h3{
white-space: nowrap;
overflow: hidden;
text-overflow: ellipsis;
padding-left: 2vh;
padding-top: 3vh;
letter-spacing: -2px;
}
h4 {
  overflow: hidden;
  padding-left: 2vh;
  padding-top: 3vh;
  word-wrap: break-word;
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

.write-button {
  background-color: #7979e9; /* Dark Blue */
  color: white;
  padding: 5px 20px;
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

</style>