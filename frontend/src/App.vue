<template>
  <div id="app">
    <tree/>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import Tree from "./components/Tree.vue";

@Component({
  components: {
    Tree
  }
})
export default class App extends Vue {}
</script>

<style lang="scss">
#app {
margin: 0;
paddins: 0;
}
</style>
