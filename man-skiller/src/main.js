import { createApp } from 'vue'
import App from './App.vue'
import router from './routers'
import { reactive } from '@vue/reactivity';

// Create a reactive global data object and set it to null
const globalData = reactive({
    someValue: null,
});

const app = createApp(App);
app.config.globalProperties.$globalData = globalData;

// Use the router
app.use(router);

app.mount('#app');
