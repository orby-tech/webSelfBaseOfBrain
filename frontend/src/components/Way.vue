<template>
  <div class="way">
      <div class="header">
        <p v-bind:class="{ noDisplay: width < 10 }">{{ store.state.waysIds[id] || id }}</p>
        <div class="lisOfArticles" v-bind:class="{ noDisplay: width < 30 }">
            <div class="article"
                v-for="i in ( store.state.ways[id] ? store.state.ways[id].articles.slice(0,3) : [])" 
                :key='i' 
                v-bind:id="i"  
                @click="selectArticle(i)"
                v-bind:width="width / store.state.ways[id].childs.length">
                {{store.state.articlesIds[i] || i}}
            </div>
        </div>
      </div>
      
    <div 
        class="grid" 
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

    private selectArticle = (i:string) => {
        this.store.commit('setWaysMode', false)
        this.store.commit('setSelectedArticle', i)
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
    padding: 10px;
    border-radius: 10px;
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
