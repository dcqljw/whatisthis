<template>
  <div>
    <div>article</div>
    <div>{{ text }}</div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Article",
  data() {
    return {
      text: ""
    }
  },
  created() {
    let sign = this.$route.query.xby
    axios({
      url: "xby?xby=" + sign,
      method: "GET"
    }).then((result) =>{
      console.log(result)
    })
  }
}
</script>

<style scoped>

</style>