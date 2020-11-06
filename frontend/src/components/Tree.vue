<template>
  <div class="hello">
    <Way v-bind:id="'root'" v-bind:width="width"  v-bind:class="{ noDisplay: !store.state.waysMode }"/>

    <Article   v-if="!store.state.waysMode"/>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import store from '@/store'

import Way from '@/components/Way.vue'
import Article from '@/components/Article.vue'


import { ax } from '@/variables.ts'

//
@Component ({
  components: {
    Way,
    Article
  }
})
export default class Tree extends Vue {
  store = store
  width = window.innerWidth


  private mounted (){
    this.getWays()
    this.getWaysIds()
    this.getArticlesIds()
  }
  async getWays(){
    const answer = (await ax( '/ways/getWays' ) ).data.data[0]
    this.width = this.width  / Object.keys(answer).length
    this.store.commit('setWays', answer)
    
  }
  async getWaysIds(){
    const answer = (await ax( '/ids/getWaysIds' ) ).data.data
    this.store.commit('setWaysIDs', answer)
  }
  async getArticlesIds(){
    const answer = (await ax( '/ids/getArticleIDs' ) ).data.data
    this.store.commit('setArticlesIDs', answer)
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.hello{
  font-size: 200%;

}
.noDisplay{
    display: none;
}
</style>
