<template>
<div>
    <div
      class="reader"
      id="reader"
      @keyup="keyup()"
      v-for="(i, index) in article"
      :key="i + index"
    >
      <one-line v-bind:line="i" />
    </div>
</div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import store from "@/store";
import OneLine from "@/components/oneLineOfArticle.vue"

import { ax } from "@/variables.ts";
//

@Component({
    components:{
        OneLine
    }
})
export default class Reader extends Vue {
  @Prop() private article!: [];

  private oneLine(line: string) {
    return this.$createElement(
      'code',
      'line'
    )


  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

</style>
