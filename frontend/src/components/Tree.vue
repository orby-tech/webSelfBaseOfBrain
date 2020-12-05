<template>
  <div class="hello"  @wheel="wheelSelectWay" v-if="renderComponent">
    <ul 
    :key='store.state.showHideContextMenu.id'
      v-bind:class="{noDisplay: store.state.showHideContextMenu.id === null || store.state.showHideContextMenu.article }" 
      @mouseleave="closeContext"
      v-bind:style="{
        left: (store.state.showHideContextMenu.x - 100) + 'px', 
        top: (store.state.showHideContextMenu.y - 100 )+ 'px'
        }">

      <li ><button @click="showHideAddWayDialog(false)"> add way </button></li>
      <li ><button @click="showHideAddArticleDialog(false)"> add article </button></li>
      <li ><button @click="showHideDeleteDialog(false)"> delete </button></li>
      <li ><button> move </button></li>
      <li ><button> Rename </button></li>
    </ul>
    <ul 
    :key='store.state.showHideContextMenu.id'
      v-bind:class="{noDisplay: store.state.showHideContextMenu.id === null || !store.state.showHideContextMenu.article }" 
      @mouseleave="closeContext"
      v-bind:style="{
        left: (store.state.showHideContextMenu.x - 100) + 'px', 
        top: (store.state.showHideContextMenu.y - 100 )+ 'px'
        }">
      <li ><button @click="showHideDeleteArticleDialog(false)"> delete </button></li>
      <li ><button> move </button></li>
      <li @click="showHideRenameArticleDialog(false)"><button> Rename </button></li>
    </ul>    
    <Way v-bind:id="store.state.selectedWay[0]"  v-bind:width="width"  v-bind:class="{ noDisplay: !store.state.waysMode }"/>

    <Article   v-if="!store.state.waysMode"/>


    <dialog class="addWay" ref="addWayDialog">
      <button class="close"><img :src="close"  @click="showHideAddWayDialog(true)"></button>
      <label for="addWayName"> Name of Way: </label>
      <input id="addWayName" ref="addWayName" type='text'>
      <button @click="addWayButton"> Add </button>
    </dialog>    

    <dialog class="addArticle" ref="addArticleDialog">
      <button class="close"><img :src="close"  @click="showHideAddArticleDialog(true)"></button>
      <label for="addArticleName"> Name of Article: </label>
      <input id="addArticleName" ref="addArticleName" type='text'>
      <button @click="addArticleButton"> Add </button>
    </dialog>  

    <dialog class="renameArticle" ref="renameArticleDialog">
      <button class="close"><img :src="close"  @click="showHideRenameArticleDialog(true)"></button>
      <label for="renameArticleName"> Name of Article: </label>
      <input id="renameArticleName" ref="renameArticleName" type='text'>
      <button @click="renameArticleButton"> Rename </button>
    </dialog> 

    <dialog class="delete" ref="deleteDialog">
      <button class="close"><img :src="close"  @click="showHideDeleteArticleDialog(true)"></button>
      Вы уверены?
      <button @click="delItem(true)"> Да </button>
    </dialog>
  </div>
</template>



<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import store from '@/store'

import Way from '@/components/Way.vue'
import Article from '@/components/Article.vue'
import close from '@/assets/close.png'

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
  close = close
  id = -1
  delComponent = { id: -1,  article: false}
  renderComponent = true

  private mounted (){
    this.loadingAll()
  }

  private loadingAll(){
    this.renderComponent = false
    this.getWays()
    this.getWaysIds()
    this.getArticlesIds()  
    this.width = window.innerWidth
    this.renderComponent = true  
  }

  private closeContext(){ this.store.commit('setContextShow', { id: null, x: 0, y: 0 }) }

  async getWays(){
    const answer = (await ax( '/ways/getWays' ) ).data.data
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

  private async addWayButton() {
    await ax('/addWay', {name: this.$refs.addWayName.value, id: this.id})
    this.showHideAddWayDialog(true)
    this.loadingAll()
  }

  private async addArticleButton(){
    await ax('/addArticle', {name: this.$refs.addArticleName.value, id: this.id})
    this.showHideAddArticleDialog(true)
    this.loadingAll()
  }

  private async renameArticleButton () {
    await ax('/renameArticle', {name: this.$refs.renameArticleName.value, id: this.id})
    this.showHideRenameArticleDialog(true)
    this.loadingAll()
  }

  private showHideAddWayDialog(arg){
    if (arg){ this.$refs.addWayDialog.close() }
    else{
      if ( this.store.state.ways[this.store.state.showHideContextMenu.id].childs.length >= 5) {
        alert("Sorry, not more 5 ways in one")
        return
      }
      this.$refs.addWayDialog.show()   
      this.id = this.store.state.showHideContextMenu.id
    }
  }  

  private showHideAddArticleDialog(arg) {
    if (arg){ this.$refs.addArticleDialog.close() }
    else{
      if ( this.store.state.ways[this.store.state.showHideContextMenu.id].articles.length >= 5) {
        alert("Sorry, not more 5 articles in one")
        return
      }
      this.$refs.addArticleDialog.show()   
      this.id =   this.store.state.showHideContextMenu.id
    }
  }

  private showHideDeleteDialog(arg){
    if (arg){ this.$refs.deleteDialog.close() }
    else{
      this.$refs.deleteDialog.show()  
      this.delComponent = { id: this.store.state.showHideContextMenu.id,  article: !!this.store.state.showHideContextMenu.article}   
    }
  }

  private showHideDeleteArticleDialog(arg) {
    if (arg){ this.$refs.deleteDialog.close() }
    else{
      this.$refs.deleteDialog.show()   
      this.delComponent = { id: this.store.state.showHideContextMenu.id,  article: !!this.store.state.showHideContextMenu.article}    
    }
  }

  private showHideRenameArticleDialog(arg){
    if (arg){ this.$refs.renameArticleDialog.close() }
    else{
      this.$refs.renameArticleDialog.show()    
      this.id =   this.store.state.showHideContextMenu.id
    }
  }

  private wheelSelectWay (e) {
    if ( !this.store.state.waysMode) return
    if (e.deltaY < 0 ) {
        if(this.store.state.selectedWay.length <= 1) return
        this.store.commit('setSelectedWay', [...this.store.state.selectedWay.slice(1)])
    }
  } 
  
  private async delItem () {
    if ( this.delComponent.article ) {
      await ax('/deleteArticle', {id: this.delComponent.id })
      this.renderComponent = false
      this.showHideDeleteArticleDialog(true)
      this.loadingAll()
      this.width = window.innerWidth
      this.renderComponent = true
    }    
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
dialog {
  position: fixed;
  top: 50%;
  left: 50%;
  width: 300px;
  height: 100px;
  margin:0;
  transform: translate(-50%, -50%);
  }
dialog img {
  width: 20px;
  height: 20px;
  margin:0;
  padding: 0;
}
dialog button.close {
  display: block;
  width: 22px;
  height: 22px;
  position: absolute;
  top: 15px;
  right: 15px;
  margin:0;
  padding: 0;
}
.hello{
  font-size: 200%;

}
.noDisplay{
    display: none;
}
</style>
