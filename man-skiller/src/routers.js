import DashBoard from './components/DashBoard.vue';
import NavBar from './components/NavBar.vue';
import ProfilePage from './components/ProfilePage.vue';
import ProjectTasks from './components/ProjectTasks.vue';
import ResourcesPage from './components/ResourcesPage.vue';
import AddProject from './components/AddProject.vue'
import SignUp from './components/SignUp.vue'
import ViewTask from './components/ViewTask.vue'
import ViewProject from './components/ViewProject.vue'
import EditProject from './components/EditProject.vue'
import AddTask from './components/AddTask.vue'
import EditTask from './components/EditTask.vue'
import TaskView from './components/TaskView.vue'
import ViewResource from './components/ViewResource.vue'
import AddResource from './components/ViewResource.vue'
import LandPage from './components/LandPage.vue';
import LogIn from './components/LogIn.vue';
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    name: 'LandPage',
    component: LandPage,
    path: '/',
  },
  {
    name: 'LogIn',
    component: LogIn,
    path: '/log-in',
  },

  {
    name: 'SignUp',
    component: SignUp,
    path: '/sign-up',
  },

  {
    name: 'DashBoard',
    component: DashBoard,
    path: '/dashboard',
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
  },
  {
    name: 'ViewTask',
    component: ViewTask,
    path: '/tasks',
  },
  {
    name: 'ViewProject',
    component: ViewProject,
    path: '/view-project/:id',
  },
  {
    name: 'EditProject',
    component: EditProject,
    path: '/edit-project/:id',
  },
  {
    name: 'AddTask',
    component: AddTask,
    path: '/add-task',
  },
  {
    name: 'EditTask',
    component: EditTask,
    path: '/edit-task',
  },
  {
    name: 'TaskView',
    component: TaskView,
    path: '/task-view',
  },
  {
    name: 'ViewResource',
    component: ViewResource,
    path: '/view-resource',
  },

  {
    name: 'AddResource',
    component: AddResource,
    path: '/add-resource',
  },
  
]




const router = createRouter({
  history: createWebHistory(), routes
})

export default router