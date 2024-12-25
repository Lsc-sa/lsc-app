<template>
  <div
    class="flex flex-col sm:flex-row w-full px-6 gap-5 mt-24 lg:mt-40 pb-24 pay"
  >
    <div
      v-if="messageStatus != null"
      class="card items-center bg-white rounded-box flex-grow px-4 py-10 gap-10 shadow-md"
    >
      <h1 v-if="messageStatus" class="text-success text-3xl font-bold">
        {{ $t("Payment Successful") }}
      </h1>
      <h1 v-else class="text-success text-3xl font-bold">
        {{ $t("Payment Rejected") }}
      </h1>
      <font-awesome-icon
        v-if="messageStatus"
        icon="fa-solid fa-circle-check"
        shake
        class="text-success text-8xl"
      />
      <font-awesome-icon
        v-else
        icon="fa-solid fa-circle-xmark"
        bounce
        class="text-danger text-8xl"
      />
      <h2 class="text-success text-3xl font-bold">
        {{ $t("Redirecting you to the profile page...") }}
      </h2>
      <font-awesome-icon
        icon="fa-solid fa-spinner"
        spin
        class="text-2xl text-black"
      />
    </div>
  </div>
  <Loader v-if="loading" />
  <!-- <BottomNav /> -->
</template>

<script setup>
import { useI18n } from "vue-i18n";
const { t, locale } = useI18n();

import Loader from "@/components/Loader.vue";
import LoggedInTopNav from "../components/LoggedInTopNav.vue";
// import BottomNav from "@/components/BottomNav.vue";
import { useRouter, useRoute } from "vue-router";
import { ref, onMounted } from "vue";

const route = useRoute();
const loading = ref(false);
const transId = route.query.invoice_id;
const messageStatus = ref(null);
const navigate = useRouter();
const requestOptions = {
  method: "GET",
  headers: { Cookie: document.cookie },
  redirect: "follow",
};

fetch("/api/method/frappe.auth.get_logged_user", requestOptions)
  .then((response) => {
    if (!response.ok) {
      throw new Error("You are not logged In");
    }
    return response.json();
  })
  .then()
  .catch(() => navigate.replace("/"));

async function getResponse() {
  loading.value = true;
  try {
    const response = await fetch(
      `/api/method/lsc_api.lsc_api.get_payment_status.get_payment_status?id=${transId}`
    );
    const data = await response.json();

    // `/api/method/lsc_api.lsc_api.get_payment_status.refund?id=${transId}`

    if (data.message.status == "paid") {
      messageStatus.value = true;
    } else {
      messageStatus.value = false;
    }
  } catch (error) {
    console.error("error" + error);
  } finally {
    loading.value = false;
  }
}

onMounted(() => {
  getResponse();
  setTimeout(() => {
    // navigate.replace("/home");
    window.close();
    console.log("Window.close");
  }, 2500);
  setTimeout(() => {
    // navigate.replace("/home");
    console.log("Window.close");
    window.close();
  }, 3500);
});
</script>

<style scoped>
.pay {
  direction: ltr;
}
</style>
