<template>
  <LoggedInTopNav :title="t('Pay Now')" :backArrow="true" />
  <div
    v-if="!selected"
    :dir="$i18n.locale == 'ar' ? 'rtl' : 'ltr'"
    class="payme flex flex-col min-h-screen gap-4 overflow-y-scroll px-4 py-20"
  >
    <h2 class="text-black font-bold">
      {{ $t("Choose payment method") }}
    </h2>
    <div class="paymethodSelect">
      <div class="tapMethod flex justify-between items-center">
        <input type="radio" name="radio-1" class="radio" checked="checked" />
        <span class="text-black font-bold">
          {{ $t("Pay With Moyasser") }}
        </span>
      </div>
    </div>
    <button
      class="btn btn-primary text-white border-white bg-primary"
      @click="
        () => {
          handlePlanSelecting(plan_name);
        }
      "
    >
      {{ $t("Subscribe Now") }}
    </button>
    <!-- <button class="btn  btn-primary text-white border-white	 bg-primary" @click="handlePaynow">ادفع الان</button> -->
  </div>
  <div
    v-else
    class="payme flex flex-col min-h-screen gap-4 overflow-y-scroll px-4 py-20"
  >
    <RouterLink
      class="btn btn-primary text-white border-white bg-primary"
      :to="{
        path: '/loading',
        query: { sales_invoice: salesInvoiceName },
      }"
      @click="nav()"
      target="_blank"
    >
      {{ $t("Confirm Payment Method") }}
    </RouterLink>
  </div>

  <!-- <iframe
    v-else
    class="mb-20 h-[90vh]"
    id="checkoutIframe"
    width="100%"
    style="border: none"
    :src="selected"
  ></iframe> -->
  <Loader v-if="loading" />
  <!-- <BottomNav /> -->
</template>
<script setup>
import { useI18n } from "vue-i18n";
const { t, locale } = useI18n();
// import BottomNav from "@/components/BottomNav.vue";
import Loader from "@/components/Loader.vue";
import LoggedInTopNav from "../components/LoggedInTopNav.vue";
import { ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import axios from "axios";

const loading = ref(false);
const route = useRoute();
const plan_name = route.query.plan_name || "";
const salesInvoiceName = ref("");
const selected = ref(false);

async function handlePlanSelecting(plan_name) {
  loading.value = true;
  try {
    const res = await axios.post(
      "/api/method/lsc_api.lsc_api.subscription_plan.subscription_plan.create_subscription",
      { data: { plan_name: plan_name } },
      {
        headers: {
          "Content-Type": "application/json",
        },
        withCredentials: true,
      }
    );
    salesInvoiceName.value = res.data.message.data.sales_invoice;
    selected.value = true;
    loading.value = false;
  } catch (error) {
    loading.value = false;
    console.error("Error creating subscription:", error);
  }
}
// let popupWindow = null;
const router = useRouter();
function nav() {
  setTimeout(() => {
    router.push({ path: `/profile` });
  }, 3000);
}
// function handlePaynow() {
//   // loading.value = true;
//   // const url = router.resolve({
//   //   name: "/loading",
//   //   query: { sales_invoice: salesInvoiceName.value },
//   // }).href;
//   // window.open(url, "_blank");

//   // popupWindow = window.open("/dashboard/loading", "_blank");

//   // try {
//   //   const res = await axios.post(
//   //     "/api/method/lsc_api.lsc_api.subscription_plan.subscription_plan.pay_subscription",
//   //     { data: { sales_invoice: salesInvoiceName.value } },
//   //     {
//   //       headers: {
//   //         "Content-Type": "application/json",
//   //       },
//   //       withCredentials: true,
//   //     }
//   //   );

//   //   selected.value = res.data.message.data.transaction.url;
//   //   loading.value = false;

//   //   if (selected.value) {
//   //     // Open the window immediately in response to user action
//   //     // Set the URL once the response is received
//   //     popupWindow.location.href = selected.value;
//   //     setTimeout(() => {
//   //       router.push({ path: `/profile` });
//   //     }, 500);
//   //   }
//   // } catch (error) {
//   //   popupWindow.close();
//   //   loading.value = false;
//   //   console.error("Error creating payment:", error);
//   // }
// }
</script>
