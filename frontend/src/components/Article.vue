<template>
  <div class="article">
    <button class="exit" @click="exit()">
      exit
    </button>
    <br/>
    <button @click="changeEditStatus()">
      {{ !editStatus ? "Редактор" : "Чтение" }}
    </button>
    <h1 contenteditable="true" @keyup="keyup(true)" id="header">
    {{ store.state.articlesIds[store.state.selectedArticle] || store.state.selectedArticle }}
    </h1>
    <div
      v-bind:class="{ noDisplay: !editStatus }"
      class="editor"
      id="editor"
      @keyup="keyup()"
      contenteditable="true"
      style=""
    ></div>
    <reader v-bind:article='text' v-bind:class="{ noDisplay: editStatus }" />
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import store from "@/store";
import Reader from "@/components/readerOfArticle.vue"
import { ax } from "@/variables.ts";
//

let updateArticleInterval
let removeUpdateArticleTimer


@Component({
    components:{
        Reader
    }
})
export default class Article extends Vue {
  @Prop() private id!: string;
  store = store;
  editStatus = false;
  text: string[] = [];
  el: HTMLElement | null = document.getElementById("editor");
  reader: HTMLElement | null = document.getElementById("reader");
  header: HTMLElement | null = document.getElementById("header");
  private keyup(header=false) {
    if (!header && this.el instanceof HTMLElement) {
      this.text = this.el.innerText.split("\n");
      if (!removeUpdateArticleTimer) {
        updateArticleInterval = setInterval( async ()=> {
           await ax('/article/updateArticle', ({id: this.store.state.selectedArticle, text: this.el.innerText }))
        }, 1000)
      }
      clearTimeout(removeUpdateArticleTimer)
      removeUpdateArticleTimer = setTimeout(()=>{
        clearInterval(updateArticleInterval)
        removeUpdateArticleTimer = null
        ax('/article/updateArticle', ({id: this.store.state.selectedArticle, text: this.el.innerText }))
      }, 300)
    }
    if ( header && this.header instanceof HTMLElement) {
      console.log(document.getElementById("header").textContent)
    }    
  }

  private exit() {
    this.store.commit("setWaysMode", true);
    this.store.commit("setSelectedArticle", null);
  }

  private changeEditStatus() {
    this.editStatus = !this.editStatus;
  }

  private tabEvent = () => {
    if (this.el instanceof HTMLElement) {
      //this.text = this.el.innerText.split("\n");
      //this.el.innerText =  this.el.innerText.split("\n").join("\n")
    }
  };


  private async mounted() {
    document.addEventListener("keydown", e => {
      if (e.key === "Tab" && this.editStatus) {
        e.preventDefault();
        this.tabEvent();
      }
    });
    this.el = document.getElementById("editor");

    if (!this.store.state.selectedArticle) return;

    const answer = (
      await ax("/article/getArticle", { id: this.store.state.selectedArticle })
    ).data.data;

    if (this.el instanceof HTMLElement) {
      this.el.innerText = answer;
      this.text = answer.split("\n");
    }
    return;
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h1{
  position: absolute;
  top: 0px;
  left: 50%;
  transform: translateX(-50%);
  margin:0;
  font-size: 120%;
}
.exit {
  width: 40px;
  height: 40px;
}
.editor {
  height: 100vh;
  width: 100%;
  padding: 20px;
  border: solid;
  border-width: 1px;
  text-align: left;
  font-size: 70%;
}
.noDisplay {
  display: none;
}
</style>
