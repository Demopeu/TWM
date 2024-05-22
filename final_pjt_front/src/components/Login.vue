<template>
        <div class="login-box">
            <div class="login-box-title">
                <img class="img-logo" src="@/assets/Logo_black.png" alt="Logo_black.png">
                <h1>Login</h1>
            </div>
            <div class="login-box-sub-title">
                <h3>Please enter your</h3>
                <h3>Login and your</h3>
                <h3>Password</h3>
            </div>
            <form class="login-form" @submit.prevent="login">
                <div class="input-container">
                    <input type="text" placeholder="Username" v-model.trim="username">
                    <input type="password" placeholder="Password" v-model.trim="password">
                    <h6 style="margin-left: auto">Forgot Passwords?</h6>
                </div>
                <div class="input-button-container">
                    <button type="submit">Login</button>
                    <h6 style="margin-left: auto">Not a member yet? 
                    <span @click="goToSignUp" >Register!</span>
                    </h6>
                </div>               
            </form>
        </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter.js'
const router = useRouter()
const store = useCounterStore()
const username = ref(null)
const password = ref(null)

const login = function () {
    const payload = {
        username: username.value,
        password: password.value,
    }
    store.login(payload)
    username.value = null
    password.value = null

}

const goToSignUp = () => {
    router.push('/signup')
}

</script>

<style scoped>
/* 로그인 박스 관련 */
.login-box{
    width: 400px;
    height: 100%;
    margin-left: 10vh;
    background-color: #EDFFED; 
    position: relative;
    top: 0;
    left: 0;
    right: 50%;
    bottom: 0;
    display: block;
}
.login-box-title {
    margin-bottom: 60px;
}
.login-box-sub-title {
    margin-bottom: 40px;
}
.img-logo {
  
  width: 190px;
  height: 70px;
  margin-left: 5vh;
  margin-top: 120px;
}


/* form 관련 */
.login-form {
    width: 75%;
    margin-left: 5vh;
    display: flex;
    flex-direction: column;
}
.input-container {
    display: flex;
    flex-direction: column;
    margin-bottom: 30px;
}
.input-button-container{
    display: flex;
    flex-direction: column;
    margin-bottom: 30px;
}
input {
    width: 100%;
    padding: 15px;
    border: none;
    border-radius: 15px;
    background-color: #D9D9D9;
}
input[type="text"]{
    outline: none;
    margin-bottom: 25px;
    font-size: 20px;
}
input[type="password"]{
    outline: none;
    font-size: 20px;
    margin-bottom: 1px;
}
button {
    padding: 12px 10px;
    border: none;
    border-radius: 15px;
    background-color: #FF7676;
    color: black;
    cursor: pointer;
    font-size: 25px;
    font-weight: bold;
    letter-spacing: -2px;
}

/* 글씨체 관련 */
h1{
    font-weight: bold;
    margin-left: 5vh;
    font-size: 86px;
    letter-spacing: -5px;
}
h3{
    font-weight: bold;
    margin-top: 0vh;
    margin-left: 5vh;
    font-size: 24px;
    margin-bottom: 1px;
    letter-spacing: -2px;
}
h6{
    font-weight: bold;
    letter-spacing: -1px;
}
span{
    margin-left: 0.5vw;
    color: blue;
    text-decoration: underline;
}
</style>