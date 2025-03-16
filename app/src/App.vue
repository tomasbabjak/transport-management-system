<template>
  <div class="p-6 bg-gray-100 min-h-screen">
    <nav class="mb-6 space-x-4 bg-white p-4 rounded shadow">
      <RouterLink to="/orders" class="text-blue-600 hover:text-blue-800">View Orders</RouterLink>
      <RouterLink to="/order/create" class="text-blue-600 hover:text-blue-800">Create Order</RouterLink>
    </nav>
    <div class="bg-white p-6 rounded shadow">
      <RouterView />
    </div>
  </div>
</template>

<script setup lang="ts">
</script>
