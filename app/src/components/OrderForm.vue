<template>
    <form @submit.prevent="submitOrder" class="max-w-lg mx-auto p-6 bg-white rounded-lg shadow-md">
        <div class="mb-4">
            <label class="block text-gray-700">Order Number</label>
            <input v-model="order.order_number" placeholder="Order Number" required
                class="w-full px-3 py-2 border rounded-lg" />
        </div>
        <div class="mb-4">
            <label class="block text-gray-700">Customer Name</label>
            <input v-model="order.customer_name" placeholder="Customer Name" required
                class="w-full px-3 py-2 border rounded-lg" />
        </div>
        <div class="mb-4">
            <label class="block text-gray-700">Date</label>
            <input v-model="order.date" type="date" required class="w-full px-3 py-2 border rounded-lg" />
        </div>

        <div v-for="(wp, index) in order.waypoints" :key="index" class="mb-4 p-4 border rounded-lg bg-gray-50">
            <div class="mb-2">
                <label class="block text-gray-700">Location</label>
                <input v-model="wp.location" placeholder="Location" required
                    class="w-full px-3 py-2 border rounded-lg" />
            </div>
            <div class="mb-2">
                <label class="block text-gray-700">Waypoint Type</label>
                <select v-model="wp.waypoint_type" class="w-full px-3 py-2 border rounded-lg">
                    <option>Pickup</option>
                    <option>Delivery</option>
                </select>
            </div>
            <button @click.prevent="removeWaypoint(index)" class="text-red-500 hover:text-red-700">
                Remove
            </button>
        </div>
        <button @click.prevent="addWaypoint"
            class="w-full mb-4 px-3 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-700">
            Add Waypoint
        </button>
        <button type="submit" class="w-full px-3 py-2 bg-green-500 text-white rounded-lg hover:bg-green-700">
            Create Order
        </button>
    </form>
</template>

<script lang="ts" setup>
import { reactive } from 'vue'
import type { TransportOrder, Waypoint } from '../types/index.ts'

const apiUrl = import.meta.env.VITE_API_URL;

const apiBase = `${apiUrl}/api/orders/`

const emptyWaypoint = (): Waypoint => ({ location: '', waypoint_type: 'Pickup' })

const order = reactive<TransportOrder>({
    order_number: '',
    customer_name: '',
    date: '',
    waypoints: [emptyWaypoint()]
})

const addWaypoint = () => {
    order.waypoints.push(emptyWaypoint())
}

const removeWaypoint = (index: number) => {
    order.waypoints.splice(index, 1)
}

const submitOrder = async () => {
    const response = await fetch(apiBase, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(order)
    })
    if (response.ok) {
        alert('Order created!')
        order.order_number = ''
        order.customer_name = ''
        order.date = ''
        order.waypoints = [emptyWaypoint()]
    } else {
        alert('Failed to create order.')
    }
}
</script>