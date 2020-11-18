<template>
<div>
    <code v-bind:class="{ noDisplay: type !== 'code' }">{{ newLine }}</code>
    <p v-bind:class="{ noDisplay: type !== 'str' }">{{ newLine }}</p>
</div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import store from "@/store";

import { ax } from "@/variables.ts";
//

@Component
export default class OneLine extends Vue {
  @Prop() private line!: string;
  
  type = this.typeOfLine()
  newLine = this.lineFormater()

  private typeOfLine() : string{
    if(this.line[0] === '|') return 'code'
    return 'str'
  }

  private lineFormater() : string {
    let temp: string = this.line
    if(temp[0] === '|'){
      temp = temp.slice(1)
    }
    return temp
  }

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
p {
  margin: 0px;
}
code {
  border-left: 1px solid black;
  padding-bottom: 10px;
  padding-left: 15px;
  margin-left: 20px;
}
.noDisplay {
  display: none;
}
</style>
