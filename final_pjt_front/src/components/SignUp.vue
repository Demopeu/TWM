<template>
    <div class="signup-box">
        <div class="signup-box-title">
            <img src="" alt="">
            <h1></h1>
            <button @click="goBack">X</button>
        </div>
        <div>
            <form class="signup-box-content">
                <div class="input-container">
                    <input
                        type="text"
                        v-model="username"
                        placeholder="Username"
                        required
                        />
                    <input
                        type="password"
                        v-model="password"
                        placeholder="Password"
                        required
                        />
                    <input
                        type="password"
                        v-model="confirmPassword"
                        placeholder="Confirm Password"
                        required
                        />
                    <input
                        type="email"
                        v-model="email"
                        placeholder="Email (optional)"
                        />
                </div>
                <div class="input-button-container">
                    <button type="submit">SIGNUP</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script setup>

</script>

<style scoped>

.signup-box {
  width: 300px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
  text-align: center;
}

.input-container {
  display: flex;
  flex-direction: column;
}

.input-container input {
  margin-bottom: 10px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.input-button-container {
  display: flex;
  justify-content: center;
}

.input-button-container button {
  padding: 10px 20px;
  border: none;
  background-color: #007bff;
  color: white;
  border-radius: 5px;
  cursor: pointer;
}

.input-button-container button:hover {
  background-color: #0056b3;
}

</style>