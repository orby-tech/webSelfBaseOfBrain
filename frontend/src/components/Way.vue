<template>
  <div class="way" :key="contextMenuShow" @click="selectWay" @wheel="wheelSelectWay">
      <div class="header">
        <p @contextmenu="handler($event)" v-bind:class="{ noDisplay: width < 5 }">{{ store.state.waysIds[id] || id }}</p>
        <div class="lisOfArticles" v-bind:class="{ noDisplay: width < 30 }">
            <div class="article"
                v-for="i in ( store.state.ways[id] ? store.state.ways[id].articles.slice(0,3) : [])" 
                :key='i' 
                v-bind:id="i"  
                @click="selectArticle($event, i)"
                v-bind:width="width / store.state.ways[id].childs.length">
                {{store.state.articlesIds[i] || i}}
            </div>
        </div>
      </div>

    <div 
        class="grid" 
        v-bind:class="{ noDisplay: width < 5 }"
        v-bind:style="{ 
            gridTemplateColumns : 'repeat( ' + (store.state.ways[id] ? store.state.ways[id].childs.length : 1 ) + ', 1fr )' 
            }"> 
        <way 
            v-for="i in (store.state.ways[id] ? store.state.ways[id].childs : [])" 
            :key='i' 
            v-bind:id="i"  
            v-bind:width="width / store.state.ways[id].childs.length" />
    </div>
    

  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import store from '@/store'

import { ax } from '@/variables.ts'
//

@Component
export default class Way extends Vue {
    @Prop() private id!: string;
    @Prop() private width!: number;
      store = store
    private contextMenuShow = false
    private selectArticle = (e, i:string) => {
        this.store.commit('setWaysMode', false)
        this.store.commit('setSelectedArticle', i)
        e.stopPropagation()
    }
    private handler = (event: any)=> {
        let x = event.clientX > 100 ? event.clientX : 100
            x = x < (window.innerWidth - 200) ? x : (window.innerWidth - 200) 
        let y = event.clientY > 100 ? event.clientY : 100
            y = y < (window.innerHeight - 200) ? y : (window.innerHeight - 200)             
        this.store.commit('setContextShow', { id: this.id, x: x, y: y })
        console.log(this.store.state.showHideContextMenu)
        event.preventDefault()
    }
    private selectWay(e){
        //console.log(this.id)
        if (this.store.state.ways[this.store.state.selectedWay[0]].childs.includes(this.id) ) {
            console.log(this.id)
            this.store.commit('setSelectedWay', [this.id, ...this.store.state.selectedWay])
        }
        //e.stopPropagation()
    }
    private wheelSelectWay (e) {
        if ( !this.store.state.waysMode) return
        if (e.deltaY > 0 ) {
            if (this.store.state.ways[this.store.state.selectedWay[0]].childs.includes(this.id) ) {
                this.store.commit('setSelectedWay', [this.id, ...this.store.state.selectedWay])
            }
        }
    }
}

</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.way {
    text-align: center;
    font-size: 70%;
    border: 1px solid rgba(184, 182, 182, 0.24);

    padding-top: 10px;
    padding-bottom: 10px;
}
.header {
    border: 1px solid rgba(184, 182, 182, 0.582);
    padding: 5px;
    border-radius: 5px;
}
.article {
    font-size: 70%;
    border: 1px solid rgba(184, 182, 182, 0.24);
}
.grid {
    display: grid;
    grid-gap: 0.5vw;
}
.noDisplay{
    display: none;
}
</style>
