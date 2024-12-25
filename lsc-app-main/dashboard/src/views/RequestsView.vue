<template>
  <LoggedInTopNav :title="t('Requests')" :backArrow="false" />
  <div
    :dir="$i18n.locale == 'ar' ? 'rtl' : 'ltr'"
    class="bg-white mx-4 rounded mt-24 lg:mt-40 lg:mr-auto lg:ml-auto lg:w-1/2 mb:20"
  >
    <div class="typeOfService flex items-center justify-center py-1">
      <span
        v-for="(req, index) in requests"
        :key="index"
        :class="{ activeService: activeIndex === index }"
        @click="setActive(index)"
      >
        {{ req }}
      </span>
    </div>
  </div>
  <div class="reqFilters flex gap-8 text-black items-center mx-4 mt-8">
    <div class="byMonth flex justify-between flex-grow">
      <select
        class="select select-bordered w-full select-xs select-ghost bg-gray-100 w-full text-black disabled:bg-gray-200 disabled:border-gray-200 disabled:text-black"
        id="month"
        v-model="selectedMonth"
      >
        <option v-for="month in monthsNames" :value="month.value">
          {{ month.name }}
        </option>
      </select>
    </div>
    <div class="byYear flex justify-between flex-grow">
      <select
        class="select select-bordered w-full select-xs select-ghost bg-gray-100 w-full text-black disabled:bg-gray-200 disabled:border-gray-200 disabled:text-black"
        id="year"
        v-model="selectedYear"
      >
        <option v-for="year in years" :value="year">
          {{ year }}
        </option>
      </select>
    </div>
  </div>
  <Loader v-if="loadingCurrent || loadingPrevious" />
  <div v-else-if="isError">there was an error: {{ error }}</div>
  <div v-else>
    <div
      class="openRequeust flex flex-col gap-4 mt-4 mb-20 overflow-y-scroll mx-4 lg:grid lg:grid-cols-3"
    >
      <div
        class="openReqCard flex flex-col gap-4 px-4 py-2 bg-white shadow-sm"
        :dir="$i18n.locale == 'ar' ? 'rtl' : 'ltr'"
        v-for="(request, ind) in availableRequests.filter((e) => {
          if (selectedYear || selectedMonth) {
            const [year, month] = e.creation.split(' ')[0].split('-');
            if (selectedMonth && !selectedYear) {
              return month == selectedMonth;
            } else if (selectedYear && !selectedMonth) {
              return year == selectedYear;
            } else if (selectedYear && selectedMonth) {
              return month == selectedMonth && year == selectedYear;
            }
          } else {
            return true;
          }
        })"
        :key="ind"
        @click="goToRequestDetails(request.name)"
      >
        <h2 class="reqCardType text-center text-black">
          {{ request.item }}
        </h2>
        <div class="flex justify-between w-full">
          <h2 class="reqCardType text-black">{{ request.title }}</h2>
          <h2 class="reqCardType text-black">
            {{ $t("Request No.") }}

            {{ request.name.split("-")[1] }}
          </h2>
        </div>
        <ul class="leading-8 flex justify-between">
          <li>
            <p class="text-sm text-wrap">
              {{ request.status }}
            </p>
          </li>
          <li>
            <p class="text-sm text-wrap">
              {{ request.creation.split(" ")[0] }}
            </p>
          </li>
        </ul>
      </div>
    </div>
  </div>
  <!-- <div v-else>
    {{ $t("No Requests") }}
  </div> -->
  <BottomNav />
</template>

<script setup>
import { useI18n } from "vue-i18n";
const { t, locale } = useI18n();

import BottomNav from "@/components/BottomNav.vue";
import Loader from "@/components/Loader.vue";
import LoggedInTopNav from "../components/LoggedInTopNav.vue";
import { ref, onMounted } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";
import { useQuery } from "@tanstack/vue-query";

const loading = ref(false);
const navigate = useRouter();
const requestOptions = {
  method: "GET",
  headers: { Cookie: document.cookie },
  redirect: "follow",
};
let monthsNames = [];
if (locale.value == "en") {
  monthsNames = [
    {
      name: "January",
      value: "01",
    },
    {
      name: "February",
      value: "02",
    },
    {
      name: "March",
      value: "03",
    },
    {
      name: "April",
      value: "04",
    },
    {
      name: "May",
      value: "05",
    },
    {
      name: "June",
      value: "06",
    },
    {
      name: "July",
      value: "07",
    },
    {
      name: "August",
      value: "08",
    },
    {
      name: "September",
      value: "09",
    },
    {
      name: "October",
      value: "10",
    },
    {
      name: "November",
      value: "11",
    },
    {
      name: "December",
      value: "12",
    },
  ];
} else {
  monthsNames = [
    {
      name: "يناير",
      value: "01",
    },
    {
      name: "فبراير",
      value: "02",
    },
    {
      name: "مارس",
      value: "03",
    },
    {
      name: "أبريل",
      value: "04",
    },
    {
      name: "مايو",
      value: "05",
    },
    {
      name: "يونيو",
      value: "06",
    },
    {
      name: "يوليو",
      value: "07",
    },
    {
      name: "أغسطس",
      value: "08",
    },
    {
      name: "سبتمبر",
      value: "09",
    },
    {
      name: "أكتوبر",
      value: "10",
    },
    {
      name: "نوفمبر",
      value: "11",
    },
    {
      name: "ديسمبر",
      value: "12",
    },
  ];
}
const selectedMonth = ref("");
const years = ["2024", "2025"];
const selectedYear = ref("2024");

fetch("/api/method/frappe.auth.get_logged_user", requestOptions)
  .then((response) => {
    if (!response.ok) {
      throw new Error("You are not logged In");
    }
    return response.json();
  })
  .then()
  .catch(() => navigate.replace("/"));

const requests = ref([t("Currently"), t("Previously")]);
const availableRequests = ref([]);
const activeIndex = ref(0);

const router = useRouter(); // Initialize router

const fetchCurrentRequests = () =>
  axios.get(
    "/api/method/lsc_api.lsc_api.get_current_requests.get_current_requests"
  );
const fetchPreviousRequests = () =>
  axios.get(
    "/api/method/lsc_api.lsc_api.get_previous_requests.get_previous_requests"
  );

const {
  data: currentRequests,
  isLoading: loadingCurrent,
  isError,
  error,
} = useQuery({
  queryKey: ["currentRequests"],
  queryFn: fetchCurrentRequests,
  // enabled: activeIndex.value === 0,
});

const { data: previousRequests, isLoading: loadingPrevious } = useQuery({
  queryKey: ["previousRequests"],
  queryFn: fetchPreviousRequests,
  // enabled: activeIndex.value === 1,
});

const setActive = (index) => {
  activeIndex.value = index;
  localStorage.setItem("activeIndexR", activeIndex.value);

  if (index === 0) {
    availableRequests.value =
      currentRequests?.value?.data?.message?.requests || [];
  } else {
    availableRequests.value =
      previousRequests?.value?.data?.message?.requests || [];
  }
};

const goToRequestDetails = (requestId) => {
  router.push({
    path: "/requests/requestDetails",
    query: { requestId: requestId },
  });
};

onMounted(() => {
  setActive(parseInt(localStorage.getItem("activeIndexR")) || 0);
  loading.value = true;
  setTimeout(() => {
    loading.value = false;
    setActive(parseInt(localStorage.getItem("activeIndexR")) || 0);
  }, 2000);
});
</script>

<style scoped>
span {
  @apply text-primary w-full mx-2 my-2 py-2 flex justify-center text-nowrap rounded duration-300 cursor-pointer;
}

span.activeService {
  @apply bg-primary text-white font-body;
}
</style>
