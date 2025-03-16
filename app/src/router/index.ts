import { createRouter, createWebHistory } from 'vue-router'
import OrderList from '@/components/OrderList.vue'
import OrderForm from '@/components/OrderForm.vue'

const routes = [
  {
    path: '/orders',
    name: 'OrderList',
    component: OrderList,
  },
  {
    path: '/order/create',
    name: 'OrderForm',
    component: OrderForm,
  },
  {
    path: '/',
    redirect: '/orders',
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
