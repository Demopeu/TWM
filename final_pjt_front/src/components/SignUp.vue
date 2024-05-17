<template>
    <div class="signup-box">
        <div class="signup-box-title">
            <img class="img-logo" src="@/assets/Logo_black.png" alt="Logo_black.png">
            <h1>Welcome to</h1>
            <h2>Travel With Movie!</h2>
            <button class="close-button" @click="goBack">X</button>
        </div>
        <form class="signup-box-content" @submit.prevent="signUp">
          <div class="input-container">
            <h3>Enter your username *</h3>
            <input
              type="text"
              v-model="username"
              placeholder="Username"
              required
              />
            <h3>Enter your password *</h3>
            <input
              type="password"
              v-model="password1"
              placeholder="Password"
              required
              />
            <h3>Confirm your password *</h3>
            <input
              type="password"
              v-model="password2"
              placeholder="Confirm Password"
              required
              />
            <h3>Enter your email *</h3>
            <input
              type="email"
              v-model="email"
              placeholder="Email"
              />
        </div>
        <div class="input-button-container">
            <button type="submit">SIGN UP</button>
        </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue"
import { useCounterStore } from "@/stores/counter";

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const email = ref(null)
const trophys = ref(null)
const store = useCounterStore()

const signUp = function() {
  const payload = {
    username: username.value,
    password1:  password1.value,
    password2:  password2.value,
    email: email.value,
    trophys: trophys.value,
  }
  store.signUp(payload)
  username.value = null
  password1.value = null
  password2.value = null
  email.value = null
}

</script>

<style scoped>
/* 회원가입 박스 관련 */
.signup-box {
  position: relative;
  width: 80%;
  height: 100%;
  margin: 0 auto;
  padding: 20px;
  background-color: rgba(237, 255, 237, 0.8);
}

.close-button {
  position: absolute;
  top: 1vw;
  right: 4vh;
  font-size: 58px;
  background: none;
  border: none;
  cursor: pointer;
  color: #C2C2C2;
}
.img-logo {
  
  width: 19vh;
  height: 7vh;
  margin-top: 5%;
  margin-left: 5vh;
}

/* form 관련 */

.signup-box-content {
  display: block;
  justify-content: space-between;
}
.input-container {
  display: flex;
  flex: 8;
  flex-direction: column;
  margin-bottom: 5vh;
}

.input-container input {
  width: 60%;
  margin-left: 5vh;
  margin-bottom: 10px;
  padding: 10px;
  border: none;
  background-color: #E1E1E1;
  border-radius: 5px;
  color: black;
  margin-right: auto;
}

.input-button-container {
  display: flex;
  flex: 2;
  justify-content: space-between;
}

.input-button-container button {
  margin-left: 5vh;
  padding: 10px 20px;
  border: none;
  background-color: #ADD8E6;
  color: white;
  border-radius: 5px;
  font-weight: bold;
  cursor: pointer;
}
@media screen and (max-width: 768px) {
  .input-container {
    display: flex;
    flex-direction: column;
  }
}

/* 글씨체 관련 */
h1 {
  font-size: 48px;
  margin-left: 5vh;
  font-weight: bold;
  letter-spacing: -2px;
}
h2 {
  font-size: 48px;
  margin-left: 10%;
  margin-bottom: 5vh;
  font-weight: bold;
  letter-spacing: -2px;
  
}
h3{
  margin-left: 5vh;
  font-size: 24px;
  font-weight: bold;
  letter-spacing: -2px;
}
</style>