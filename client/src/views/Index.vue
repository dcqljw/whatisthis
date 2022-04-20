<template>
  <div>
    <div>
      <el-input
          placeholder="请输入内容"
          v-model="text"
          clearable>
      </el-input>
      <el-button type="primary" round @click="submit">主要按钮</el-button>
      <el-link v-if="isShowHref" :href="href">分享链接</el-link>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Index",
  data() {
    return {
      text: '',
      href: '',
      isShowHref: false
    }
  },
  methods: {
    submit() {
      axios({
        url: "api/create_article",
        method: 'POST',
        data: {
          "text": this.text,
          "date": Date.now()
        }
      }).then((result) => {
        console.log(result)
        this.href = result.data.href
        this.isShowHref = true
      })
    }
  },
}
</script>

<style scoped>

</style>