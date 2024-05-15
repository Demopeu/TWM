<template>
    <div>
        <div class="login-box">
            <div class="login-box-title">
                <img src="" alt="">
                <h1>Login</h1>
            </div>
            <div class="login-box-sub-title">
                <h3>Please enter your</h3>
                <h3>Login and your</h3>
                <h3>Password</h3>
            </div>
            <form class="login-form" @submit.prevent="submitForm">
                <div class="input-container">
                    <input type="text" placeholder="Username">
                    <input type="password" placeholder="Password">
                    <h6 style="margin-left: auto">Forgot Passwords?</h6>
                </div>
                <div class="input-button-container">
                    <button type="submit">Login</button>
                    <h6 style="margin-left: auto">Not a member yet? 
                    <span>Register!</span>
                    </h6>
                </div>               
    </form>
        </div>
    </div>
</template>

<script setup>

</script>

<style scoped>
/* 로그인 박스 관련 */
.login-box{
    width: 400px;
    height: 100vh;
    margin: auto;
    background-color: #EDFFED; 
    position: fixed;
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
    margin-top: 120px;
    margin-left: 5vh;
    font-size: 86px;
    letter-spacing: -5px;
}
h3{
    font-weight: bold;
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