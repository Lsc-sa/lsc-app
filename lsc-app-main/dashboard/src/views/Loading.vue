<template>
  <Loader v-if="loading" />
</template>
<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import Loader from "@/components/Loader.vue";
import { useRoute } from "vue-router";

const route = useRoute();
const salesInvoiceName = route.query.sales_invoice || "";

const loading = ref(true);

async function handlePaynow() {
  try {
    const res = await axios.post(
      "/api/method/lsc_api.lsc_api.subscription_plan.subscription_plan.pay_subscription",
      { data: { sales_invoice: salesInvoiceName } },
      {
        headers: {
          "Content-Type": "application/json",
        },
        withCredentials: true,
      }
    );
    loading.value = false;
    window.location.href = res.data.message.data.transaction;
  } catch (error) {
    loading.value = false;
    console.error("Error creating payment:", error);
  }
}
onMounted(() => {
  handlePaynow();
});
</script>
