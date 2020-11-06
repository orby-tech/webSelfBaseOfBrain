<template>
  <div class="article">
      <div class="exit" @click='exit()'>
          exit
      </div>
      <div @click="changeEditStatus()">
          {{ editStatus ? "Редактор" : "Чтение"  }}
      </div>
      {{ store.state.selectedArticle }}
      <div  v-bind:class="{ noDisplay: !editStatus}" class="editor" id="editor" @focus="focusEvent" @keyup="keyup()" contenteditable="true" style=""> </div>
      <div v-bind:class="{ noDisplay: editStatus}"  class="reader" id="reader" @keyup="keyup()"  style=""> {{text}} </div>

  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import store from '@/store'

import { ax } from '@/variables.ts'
//

@Component
export default class Article extends Vue {
    @Prop() private id!: string;
    store = store
    editStatus = true
    text = ''
    el: HTMLElement | null = document.getElementById('editor');
    private keyup() {
        if (this.el instanceof HTMLElement) {
            this.text = this.el.innerText.split('\n').join('\n')
            console.log(this.text)
        }
    }

    private focusEvent = (e:any) => {
        console.log(e)
    }

    private exit() {
        this.store.commit('setWaysMode', true)
        this.store.commit('setSelectedArticle', null)
    }

    private changeEditStatus() {
        this.editStatus = !this.editStatus
    }

    private tabEvent = () => {
        if (this.el instanceof HTMLElement) {
            this.text = this.el.innerText = this.el.innerText.split('\n').join('\n')
        }
    }

    private async mounted (){
        document.addEventListener("keydown", (e)=>{
            console.log(e.key)
            if (e.key==='Tab' && this.editStatus) {
                e.preventDefault()
                this.tabEvent()
            }
        })
        this.el = document.getElementById('editor');

        if ( !this.store.state.selectedArticle ) return

        const answer = (await ax( '/article/getArticle', { id: this.store.state.selectedArticle} ) ).data.data

        if (this.el instanceof HTMLElement) {
            this.text = (this.el.innerHTML) = answer
        }
        return
    }      
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.editor {
    height: 100vh;
    width: 100%;
    padding:20px;
    border: solid;
    border-width: 1px; 
    text-align: left;
    font-size: 70%;
}
.noDisplay{
    display: none;
}
</style>
