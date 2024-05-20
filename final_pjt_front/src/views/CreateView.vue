<template>
  <div>
    <form @submit.prevent="createArticle">
      <select name="country" id="country-select" v-model.trim="country">
        <option value="" selected disabled hidden>국가 혹은 대륙을 선택하세요.</option>
        <option value="north-america">North America</option>
        <option value="south-america">South America</option>
        <option value="europe">Europe</option>
        <option value="india">India</option>
        <option value="korea">korea</option>
        <option value="china">china</option>
        <option value="japan">japan</option>
      </select>
      <input type="text" name="title" id="title" v-model.trim="title">
      <textarea name="content" id="content" cols="30" rows="10" v-model.trim="content"></textarea>
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter';
const title = ref(null)
const content = ref(null)
const country = ref(null)
const store = useCounterStore()

const createArticle = function () {
  const payload = {
    title: title.value,
    content: content.value,
    country: country.value
  }
  store.createArticle(payload)
}


</script>

<style lang="scss" scoped>

</style>