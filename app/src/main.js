import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';

export const app = createApp(App);
app.use(router);
app.use(store);
app.config.globalProperties.$store = store;
app.mount('#app');
