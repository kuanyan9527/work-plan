<template>
  <div id="header" class="header">
    <div id="header_name" class="header_name">
      <i @click="toMainPage">WorkPlan</i>
    </div>
    <div id="main_tab" class="main_tab">
      <div id="project" class="project"
        @click="toProjectPage($refs, 0)"
        :class="{'tab-selected': tab_selected_arr[0]}">Project</div>
      <div id="task" class="task" @click="toTaskPage($refs, 1)"
        :class="{'tab-selected': tab_selected_arr[1]}">Task</div>
      <div id="user" class="user" @click="toUserPage($refs, 2)"
        :class="{'tab-selected': tab_selected_arr[2]}">User</div>
    </div>
    <div id="header_tail" class="header_tail">
      <div id="login" class="login">login</div>
      <div id="to-github" class="to-githu">github</div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import { ref } from 'vue'

const router = useRouter()

let tab_selected_arr = ref([0, 0, 0])
const toProjectPage = (item: any, idx: number) => {
  router.push('/project/')
  selected(idx)
  
}

const toTaskPage = (item: any, idx: number) => {
  router.push('/task/')
  selected(idx)
  
}

const toUserPage = (item: any, idx: number) => {
  router.push('/user/')
  selected(idx);
}

const toMainPage = () => {
  router.push('/')
  selected(0, true)
}

const selected = (idx: number, cancel: boolean = false) => {
  for(let i = 0; i < tab_selected_arr.value.length; ++i) {
    (tab_selected_arr.value)[i] = 0
  }
  if (!cancel) {
    (tab_selected_arr.value)[idx] = 1
  } 
}
</script>

<style lang="css" scoped>
.header {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin: 0 auto;
  width: 100%;
  height: 3rem;
  box-shadow: 1px 1px 5px 1px rgba(0, 0, 0, 0.1);
}

.header_name {
  padding-left: .6rem;
  width: 20%;
  height: 100%;
  line-height: 3rem;
  font-size: 1.5rem;
  color: rgb(247, 132, 132);
}

.header i {
  cursor: pointer
}

.main_tab {
  flex-grow: 1;
  display: flex;
  height: 100%;
}

.main_tab > div {
  padding: auto .6rem;
  padding: 0 .5rem;
  width: 4.5rem;
  line-height: 3rem;
  text-align: center;
  cursor: pointer;
}

.tab-selected {
  border-bottom: 2px solid rgb(2, 210, 252);
  background-color: aliceblue;
}

.main_tab > div:hover {
  border-bottom: 2px solid rgb(2, 210, 252);
  background-color: aliceblue;
}

.header_tail {
  display: flex;
  width: 20%;
  height: 100%;
  font-size: .8rem;
  line-height: 3rem;
  justify-content: end;
}

.header_tail > div {
  margin: 0 .4rem;
  cursor: pointer;
}
</style>