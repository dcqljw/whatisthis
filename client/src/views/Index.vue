<template>
  <div>
    <div>
      <el-input
          placeholder="请输入内容"
          v-model="input"
          clearable>
      </el-input>
      <el-button type="primary" round @click="submit">主要按钮</el-button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Index",
  data() {
    return {
      input: ''
    }
  },
  methods: {
    submit() {
      axios({
        url: "api/create_article",
        method: 'POST',
        data: {
          "text": "123",
          "date": "123123"
        }
      }).then((result) => {
        console.log(result)
      })
    }
  },
}
</script>

<style scoped>

</style>