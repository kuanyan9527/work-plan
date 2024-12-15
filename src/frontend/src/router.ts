import { createMemoryHistory, createRouter } from 'vue-router'

import Header from './components/Header.vue'
import MainPage from './components/MainPage.vue'
import Project from './components/Project.vue'
import Task from './components/Task.vue'
import User from './components/User.vue'

const routes = [
  {path: '/project/', component: Project},
  {path: '/task/', component: Task},
  {path: '/user/', component: User},
  {path: '/', component: MainPage}
]

const router = createRouter({
  history: createMemoryHistory(),
  routes,
})

export default router