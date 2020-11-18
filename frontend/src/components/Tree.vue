<template>
  <div class="hello">
    <ul 
    :key='store.state.showHideContextMenu.id'
      v-bind:class="{noDisplay: store.state.showHideContextMenu.id === null }" 
      @mouseleave="closeContext"
      v-bind:style="{
        left: (store.state.showHideContextMenu.x - 100) + 'px', 
        top: (store.state.showHideContextMenu.y - 100 )+ 'px'
        }">

      <li ><button> add way </button></li>
      <li ><button> add article </button></li>
      <li ><button> delete </button></li>
      <li ><button> move </button></li>
    </ul>
    <Way v-bind:id="0" v-bind:width="width"  v-bind:class="{ noDisplay: !store.state.waysMode }"/>

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
  private closeContext(){
    this.store.commit('setContextShow', { id: null, x: 0, y: 0 })
  }
  async getWays(){
    const answer = (await ax( '/ways/getWays' ) ).data.data[0]
    console.log(answer)
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
ul {
  position: fixed;
  width: 200px;
  height: 200px;
  background-color: rgba(0, 255, 255, 0.671);
  margin: 0;
  list-style: none inside;
  padding: 0;
}
li {
  padding: 0;
  margin: 0;
  height: 30px;
}
button {
  width: 100%;
  border: 1px solid rgba(0, 0, 0, 0.171);
  border-radius: 0;
  height: 30px;
}
.hello{
  font-size: 200%;

}
.noDisplay{
    display: none;
}
</style>
