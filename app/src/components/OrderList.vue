<template>
    <div class="p-4">
        <div class="mb-4 flex gap-4">
            <input v-model="filters.search" placeholder="Search" class="border p-2" />
            <input v-model="filters.date" type="date" class="border p-2" />
            <select v-model="sort" class="border p-2">
                <option value="">Sort by</option>
                <option v-for="(label, value) in sortOptions" :key="value" :value="value">
                    {{ label }}
                </option>
            </select>
            <button @click="fetchOrders()" class="bg-blue-500 text-white px-3 py-1 rounded">Apply</button>
        </div>

        <div class="grid grid-cols-3 gap-4 bg-gray-100 p-2 font-bold">
            <div>Order Number</div>
            <div>Customer</div>
            <div>Date</div>
        </div>
        <div v-for="order in orders" :key="order.id" class="grid grid-cols-3 gap-4 border-b p-2">
            <div>{{ order.order_number }}</div>
            <div>{{ order.customer_name }}</div>
            <div>{{ order.date }}</div>
        </div>

        <div class="mt-4 flex gap-2">
            <button :disabled="!prev" @click="goToPage(prev)" class="px-3 py-1 bg-gray-300 rounded disabled:opacity-50">
                Prev
            </button>
            <button :disabled="!next" @click="goToPage(next)" class="px-3 py-1 bg-gray-300 rounded disabled:opacity-50">
                Next
            </button>
        </div>
    </div>
</template>


<script setup lang="ts">
import { ref } from 'vue'

interface TransportOrder {
    id: number
    order_number: string
    customer_name: string
    date: string
}

const sortOptions = {
    'customer_name': 'Customer Name ↑',
    '-customer_name': 'Customer Name ↓',
    'date': 'Date ↑',
    '-date': 'Date ↓',
}
const orders = ref<TransportOrder[]>([])
const next = ref<string | null>(null)
const prev = ref<string | null>(null)

const filters = ref({
    search: '',
    date: '',
})

const sort = ref('')
const apiUrl = import.meta.env.VITE_API_URL;
const apiBase = `${apiUrl}/api/orders/`

const fetchOrders = async (url: string = apiBase) => {
    const params = new URLSearchParams()

    if (filters.value.search) {
        params.set('search', filters.value.search)
    }
    if (filters.value.date) {
        params.set('date', filters.value.date)
    }
    if (sort.value) {
        params.set('ordering', sort.value)
    }

    const fullUrl = `${url.split('?')[0]}?${params.toString()}`

    try {
        const res = await fetch(fullUrl)
        const data = await res.json()

        orders.value = data.results
        next.value = data.next
        prev.value = data.previous
    } catch (error) {
        console.error('Fetch error:', error)
    }
}

const goToPage = (url: string | null) => {
    if (url) fetchOrders(url)
}

fetchOrders()
</script>