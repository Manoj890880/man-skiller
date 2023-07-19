import DashBoard from './components/DashBoard.vue';
import NavBar from './components/NavBar.vue';
import ProfilePage from './components/ProfilePage.vue';
import ProjectTasks from './components/ProjectTasks.vue';
import ResourcesPage from './components/ResourcesPage.vue';
import AddProject from './components/AddProject.vue'
import { createRouter, createWebHistory } from 'vue-router'

const routes = [

  {
    name: 'Dashboard',
    component: DashBoard,
    path: '/',
  },
  {
    name: 'ProjectTasks',
    component: ProjectTasks,
    path: '/project-tasks',
  },
  {
    name: 'ResourcesPage',
    component: ResourcesPage,
    path: '/resources',
  },
  {
    name: 'ProfilePage',
    component: ProfilePage,
    path: '/profile',
  },
  {
    name: 'NavBar',
    component: NavBar,
    path: '/nav-bar',
  },
  {
    name: 'ResourcesPage',
    component: ResourcesPage,
    path: '/resources-page',
  },
  {
    name: 'AddProject',
    component: AddProject,
    path: '/add-project',
  }
]




const router = createRouter({
  history: createWebHistory(), routes
})

export default router