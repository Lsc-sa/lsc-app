<template>
  <LoggedInTopNav :title="t('Packages')" :backArrow="true" />
  <div
    :dir="$i18n.locale == 'ar' ? 'rtl' : 'ltr'"
    class="packs flex gap-4 overflow-x-scroll scrollbar-hide px-4 pt-24 justify-start mb-4 lg:justify-evenly"
  >
    <div
      class="flex flex-col bg-white min-w-80 items-center gap-2 overflow-x-scroll py-4 my-2 justify-between"
      v-for="(pack, idx) in packages"
      :key="idx"
    >
      <div
        class="packageDetailsCard flex flex-col gap-4 justify-center items-center bg-white w-full rounded py-4 px-4"
      >
        <p class="text-primary">{{ pack.plan_name }}</p>
        <p class="price text-4xl text-black -mb-4 font-black">
          {{ pack.cost }}
        </p>
        <div class="flex items-end text-black gap-1">
          <p class="curr">
            {{ pack.currency }}
          </p>
          <p class="yearly">
            /
            {{ pack.billing_interval }}
          </p>
        </div>
        <p class="text-xs">
          {{ $t("Available Hours:") }}
          {{ pack.custom_total_hrs }}
        </p>
        <div class="collapse collapse-arrow border-b-2 border-black text-black">
          <input type="checkbox" />
          <div class="collapse-title text-xl font-medium">
            {{ $t("Package conditions") }}
          </div>
          <div class="collapse-content" v-html="pack.plan_requiries"></div>
        </div>
      </div>
      <div
        class="title"
        v-for="(serv, index) in pack.allowed_services"
        :key="index"
      >
        <h2 class="text-sm font-bold text-black text-center">
          {{ serv.service_name }}
        </h2>
      </div>
      <button
        :class="[
          'btn',
          pack.plan_name == plan_name || pack.name == plan_name
            ? 'btn-success'
            : '',
        ]"
        @click="
          () => {
            handlePlanSelecting(pack.name);
          }
        "
      >
        {{ $t("Choose This Package") }}
      </button>
    </div>
  </div>
  <div
    class="packageDetails flex flex-col items-center mb-20 w-full gap-4 overflow-x-scroll px-4 lg:max-w-96 lg:mx-auto lg:my-0"
  >
    <RouterLink
      v-if="allowSend"
      class="btn btn-primary text-white border-white bg-primary max-w-64 w-full disabled:bg-gray-200 disabled:border-gray-200 disabled:text-black"
      :to="{
        path: '/packages/paynow',
        query: { plan_name: plan_name },
      }"
    >
      {{ $t("Subscribe Now") }}
    </RouterLink>
  </div>
  <Loader v-if="loading" />
  <!-- <BottomNav /> -->
</template>

<script setup>
import { useI18n } from "vue-i18n";
const { t, locale } = useI18n();

// import BottomNav from "@/components/BottomNav.vue";
import Loader from "@/components/Loader.vue";
import LoggedInTopNav from "../components/LoggedInTopNav.vue";
import { onMounted } from "vue";
import { ref } from "vue";
import { useRouter, RouterLink } from "vue-router";

const loading = ref(false);
const navigate = useRouter();
const plan_name = ref("");
const allowSend = ref(false);
const checkedd = ref(false);
function handlePlanSelecting(pack) {
  plan_name.value = pack;
  allowSend.value = true;
}

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

const packages = ref([]);
const packagesNames = ref([]);
const activeIndex = ref(0);

const setActive = (index) => {
  activeIndex.value = index;
};

const fetchData = async () => {
  loading.value = true;
  try {
    const response = await fetch(
      "/api/method/lsc_api.lsc_api.subscription_plan.subscription_plan.get_subscriptions"
    );
    const data = await response.json();
    loading.value = false;
    packagesNames.value = data.message.data.map((pkge) => pkge.name);
    packages.value = data.message.data.map((pkge) => pkge);
  } catch (error) {
    loading.value = false;
    console.error("Error fetching data:", error);
  }
};

onMounted(() => {
  fetchData();
});
</script>

<style scoped>
span {
  @apply text-primary  text-sm px-4 my-2 p-2 text-nowrap rounded duration-300 cursor-pointer;
}

span.activePackage {
  @apply bg-primary text-white font-body;
}
.scrollbar-hide::-webkit-scrollbar {
  display: none;
}

.scrollbar-hide {
  -ms-overflow-style: none;
  scrollbar-width: none;
}
</style>
