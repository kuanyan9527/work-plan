<template>
  <div id="project" class="project">
    <div id="operate" class="operate">
      <div id="p-new" class="p-new">
        <el-button type="primary">New Project</el-button>
      </div>
      <div id="p-delete" class="delete">
        <el-button type="primary" :disabled=false>Edit Project</el-button>
      </div>
      <div id="p-edit" class="p-edit">
        <el-button type="danger" :disabled=true>Delete Project</el-button>
      </div>
    </div>
    
    <div id="p-table" class="p-table">
      <el-table :data="tableData" 
        @select="handleSelect"
        @select-all="handleSelectAll"
        style="width: 100%">
        <el-table-column type="selection" width="50" />
        <el-table-column prop="p_name" label="Name" width="180" />
        <el-table-column prop="p_status" label="Status" width="180" />
        <el-table-column prop="p_task_in_progress" label="Task in progress" width="180" />
        <el-table-column prop="p_manpower" label="Manpower" />
      </el-table>
    </div>
  </div>
</template>

<script setup lang="ts">
interface Project {
  p_name: string,
  p_status: number,
  p_task_in_progress: number,
  p_manpower: number
}

const selection: Project[] = []
const tableData: Project[] = [
  {
    p_name: "project1",
    p_status: 1,
    p_task_in_progress: 5,
    p_manpower: 2
  },
  {
    p_name: "project1",
    p_status: 0,
    p_task_in_progress: 7,
    p_manpower: 2
  },
  {
    p_name: "project1",
    p_status: 1,
    p_task_in_progress: 0,
    p_manpower: 1
  }
]

const handleSelect = (selection: Project[], row: Project) => {
  console.log(selection);
  console.log(row);
  
}

const handleSelectAll = (selection: Project[]) => {
  console.log(selection);
  
}
</script>

<style lang="css" scoped>
.project {
  margin: 1rem auto 0;
  width: 70%
}

.operate {
  display: flex;
  justify-content: start;
}

.operate > div {
  margin-right: .5rem;
}

.p-table {
  
}
</style>