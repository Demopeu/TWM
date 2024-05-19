<template>
    <div v-if="article">
        <h1>{{ article.title }}</h1>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios'

const route = useRoute()
const article = ref(null)

onMounted(() => {
    console.log(route)
    axios({
        method: 'get',
        url: `http://127.0.0.1:8000/community/articles/${route.params.articleId}/`
    })
    .then((response) => {
        article.value = response.data
    })
    .catch((error) => {
        console.log(error)
    })
})
</script>

<style lang="scss" scoped>

</style>