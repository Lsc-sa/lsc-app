<template>
  <LoggedInTopNav :title="t('Services')" :backArrow="false" />

  <div
    class="fixed w-full flex flex-col sm:grid sm:grid-cols-5 sm:grid-rows-2 gap-3 mt-20 lg:h-[90vh]"
  >
    <div class="row-span-2 hidden lg:block">
      <SideNav />
    </div>

    <Loader v-if="loadingCurrent" />
    <div
      v-else
      class="py-4 bg-[ghostwhite] h-[80vh] overflow-y-scroll flex flex-col sm:col-span-5 lg:col-span-4 sm:grid sm:grid-cols-4 gap-4"
    >
      <!-- Service Names at the top -->
      <div
        class="bg-white mx-4 rounded place-content-center rounded-3xl shadow-mycard col-span-4 h-fit"
      >
        <div
          class="typeOfService flex overflow-y-scroll py-1 lg:justify-center"
        >
          <span
            v-if="services && services != 'fail'"
            v-for="(service, index) in services"
            :key="index"
            :class="{ activeService: activeIndex === index }"
            @click="setActive($event, index)"
          >
            {{ service?.name }}
          </span>
        </div>
      </div>

      <!-- Service Details -->
      <div
        class="openServices flex flex-col overflow-visible sm:overflow-hidden place-content-center w-full px-6 gap-5 col-span-4"
      >
        <div
          v-if="currentDepartmentDetails"
          v-for="(elemnt, index) in currentDepartmentDetails"
          :key="index"
          class="openServiceCard text-center flex flex-col gap-2 justify-between items-center bg-white rounded py-4 px-4 lg:py-7"
        >
          <div class="flex justify-between items-center w-full">
            <h1 class="text-black font-bold">{{ elemnt?.name }}</h1>
            <h1>
              {{ $t("Cost") }}
              :
              {{ elemnt?.hrs }}
              {{ $t("Hour") }}
            </h1>
          </div>
          <p class="text-sm text-center">
            {{ elemnt?.description }}
          </p>
          <RouterLink
            :to="{
              path: getMatchedPath(elemnt?.name),
              query: { elemnt: elemnt?.item_code, elementName: elemnt?.name },
            }"
            class="btn btn-sm w-full bg-primary border-primary rounded h-8 text-white"
          >
            {{ $t("Book Now") }}
          </RouterLink>
        </div>

        <div
          v-if="services == 'fail'"
          class="openServiceCard text-center flex flex-col gap-2 justify-between items-center bg-white rounded py-4 px-4 lg:py-7"
        >
          <p class="text-black font-bold">
            {{ $t("You are not subscribed to any package.") }}
          </p>
          <RouterLink
            :to="{
              path: '/packages',
            }"
            class="btn btn-sm w-full bg-primary border-primary rounded h-8 text-white"
          >
            {{ $t("Subscribe Now") }}
          </RouterLink>
        </div>
      </div>
    </div>
  </div>
  <div v-if="showToast" class="relative">
    <div class="toast bottom-20 left-1/2 -translate-x-1/2">
      <div class="alert alert-info bg-white border-2 border-primary">
        <span>{{ toastMessage }}</span>
      </div>
    </div>
  </div>
  <Loader v-if="loading" />
  <BottomNav />
</template>

<script setup>
import { useI18n } from "vue-i18n";
const { t, locale } = useI18n();
import Loader from "@/components/Loader.vue";
import BottomNav from "@/components/BottomNav.vue";
import SideNav from "@/components/SideNav.vue";
import { RouterLink } from "vue-router";
import { ref, onMounted } from "vue";
import LoggedInTopNav from "../components/LoggedInTopNav.vue";
import { useRouter } from "vue-router";
import { useQuery } from "@tanstack/vue-query";
import axios from "axios";
import showToastMessage from "../router/toastmessage";

const loading = ref(false);
const navigate = useRouter();
const services = ref([]);
const currentDepartmentDetails = ref(null);
const activeIndex = ref(0);
const showToast = ref(false);
const toastMessage = ref(null);

const fetchServices = () =>
  axios.get("/api/method/lsc_api.lsc_api.get_departments.get_departments");

const {
  data: servicesList,
  isLoading: loadingCurrent,
  isError,
} = useQuery({
  queryKey: ["servicesList"],
  queryFn: fetchServices,
});

// // Fetch departments and services
// const fetchData = async () => {
//   loading.value = true;
//   try {
//     const response = await fetch(
//       "/api/method/lsc_api.lsc_api.get_departments.get_departments"
//     );
//     const data = await response.json();
//     loading.value = false;
//     if (data.message.status !== "fail") {
//       services.value = data.message.departments.sort((a, b) =>
//         b.name.localeCompare(a.name, "ar")
//       );
//       setActive(null, 0); // Set the first department as active initially
//     }
//   } catch (error) {
//     loading.value = false;
//     console.error("Error fetching data:", error);
//   }
// };

// Set the active service based on the clicked index

const setActive = (event, index) => {
  activeIndex.value = index;
  localStorage.setItem("activeIndex", activeIndex.value);
  if (servicesList?.value?.data?.message?.status == "fail") {
    services.value = "fail";
    loading.value = false;
    return;
  }
  if (servicesList?.value?.data?.message?.asp_status == "Complete") {
    localStorage.setItem("asp_status", 2);
  } else if (localStorage.getItem("asp_status") == 1) {
    localStorage.setItem("asp_status", 1);
  } else {
    localStorage.setItem("asp_status", 0);
  }
  services.value = servicesList?.value?.data?.message?.departments?.sort(
    (a, b) => b.name.localeCompare(a.name, "ar")
  );
  currentDepartmentDetails.value =
    (services?.value ?? [])[index]?.details || null;
  if (index == 1)
    event?.target?.parentElement?.scroll({ left: -100, behavior: "instant" });
  if (currentDepartmentDetails.value) {
    localStorage.setItem("depart", true);
  }
};

// Get the appropriate path for the service detail
const getMatchedPath = (title) => {
  if (!title) return;
  if (title.includes("دراسة") || title.toLowerCase().includes("study")) {
    return "/services/study-case";
  } else if (title.includes("دعم") || title.toLowerCase().includes("support")) {
    return "/services/legal";
  } else if (title.includes("قضايا") || title.toLowerCase().includes("case")) {
    return "/services/case";
  } else {
    return "/services/consultation";
  }
};

onMounted(() => {
  setActive(null, parseInt(localStorage.getItem("activeIndex")) || 0);
  if (localStorage.getItem("depart") != "true") {
    loading.value = true;
    setTimeout(() => {
      setActive(null, parseInt(localStorage.getItem("activeIndex")) || 0);
      localStorage.removeItem("depart");
      loading.value = false;
    }, 2000);
  } else {
    localStorage.removeItem("depart");
  }
});
setTimeout(() => {
  setActive(null, parseInt(localStorage.getItem("activeIndex")) || 0);
  loading.value = false;
}, 2200);
setTimeout(() => {
  if (localStorage.getItem("asp_status") == 0) {
    showToastMessage(t("Complete your profile info"), toastMessage, showToast);
    setTimeout(() => {
      navigate.push({ path: `/profile/AccountStatusPage` });
    }, 1000);
  } else if (localStorage.getItem("asp_status") == 1) {
    showToastMessage(t("Complete your profile info"), toastMessage, showToast);
  }
}, 2500);
</script>

<style scoped>
span {
  @apply text-primary px-6 mx-2 my-2 p-2 text-nowrap rounded duration-300 cursor-pointer;
}

span.activeService {
  @apply bg-primary text-white font-body;
}
</style>
