import items from './components/items.vue';
import home from './components/home.vue';
import login from './components/login.vue';
import register from './components/register.vue';
import review from './components/review/Components/review';


const routes = [
    { path: '/', component: home},
    { path: '/login', component: login},
    { path: '/register', component: register},
    { path: '/items', component: items },
    { path: '/reviews', component: review },
];

export default routes;