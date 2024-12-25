<template>
  <LoggedInTopNav :title="t('Home')" :backArrow="false" />
  <div
    :dir="$i18n.locale == 'ar' ? 'rtl' : 'ltr'"
    class="fixed w-full flex flex-col sm:grid sm:grid-cols-5 sm:grid-rows-2 gap-3 mt-20 lg:h-[90vh]"
  >
    <div class="row-span-2 hidden lg:block">
      <SideNav />
    </div>
    <Loader v-if="loadingSub || loadingCurrent" />
    <div
      v-else
      class="py-4 bg-[ghostwhite] h-[80vh] overflow-y-scroll flex flex-col sm:col-span-5 lg:col-span-4 sm:grid sm:grid-cols-4 sm:grid-rows-2 gap-4"
    >
      <div
        v-if="subscription"
        class="services px-6 min-w-[300px] gap-5 bg-white mx-8 py-4 place-content-center rounded-3xl shadow-mycard text-end col-span-2 row-span-2"
      >
        <div
          style="width: 100%; height: 300px"
          class="overflow-hidden rounded-3xl"
        >
          <ag-charts :options="chartOptions"></ag-charts>
        </div>
        <div
          class="cont flex w-full justify-between items-center max-w-96 mx-auto mb-4"
        >
          <RouterLink
            :to="{ name: 'CurrentPackageView' }"
            class="flex flex-col items-center justify-center gap-2 text-center"
          >
            <div
              class="radial-progress text-center"
              :style="`--value: 
              ${(
                (subscription.remaining_consultation_hrs /
                  subscription.consultation_hrs) *
                100
              ).toFixed(2)}
            `"
              role="progressbar"
            >
              {{ subscription.consultation_hrs }} /
              {{ subscription.remaining_consultation_hrs }}
            </div>
            <span class="text-md font-bold text-black">
              {{ $t("Consultations") }}
            </span>
          </RouterLink>
          <RouterLink
            :to="{ name: 'CurrentPackageView' }"
            class="flex flex-col items-center justify-center gap-2 text-center"
          >
            <div
              class="radial-progress text-center"
              :style="`--value: 
            ${(
              (subscription.remaining_cases_hrs / subscription.cases_hrs) *
              100
            ).toFixed(2)}
          `"
              role="progressbar"
            >
              {{ subscription.cases_hrs }} /
              {{ subscription.remaining_cases_hrs }}
            </div>
            <span class="text-md font-bold text-black">
              {{ $t("Cases") }}
            </span>
          </RouterLink>
          <RouterLink
            :to="{ name: 'CurrentPackageView' }"
            class="flex flex-col items-center justify-center gap-2 text-center"
          >
            <div
              class="radial-progress text-center"
              :style="`--value: 
              ${(
                (subscription.remaining_legal_services_hrs /
                  subscription.legal_services_hrs) *
                100
              ).toFixed(2)}
            `"
              role="progressbar"
            >
              {{ subscription.legal_services_hrs }} /
              {{ subscription.remaining_legal_services_hrs }}
            </div>
            <span class="text-md font-bold text-black">
              {{ $t("Services") }}
            </span>
          </RouterLink>
        </div>
        <RouterLink :to="{ name: 'CurrentPackageView' }" class="text-success">{{
          $t("Package Managment")
        }}</RouterLink>
      </div>
      <div
        v-else
        class="services w-full px-6 gap-5 flex flex-col items-center justify-center"
      >
        <h2 class="services__heading font-bold text-gray-400 mb-2 lg:text-3xl">
          {{ $t("No Subscription") }}
        </h2>
        <RouterLink :to="{ name: 'PackagesView' }">
          <button
            class="btn btn-primary text-white border-white bg-primary text-white lg:btn-lg"
          >
            {{ $t("Subscribe Now") }}
          </button>
        </RouterLink>
      </div>
      <div
        v-if="subscription"
        class="services overflow-visible sm:overflow-hidden place-content-center w-full px-6 gap-5 col-span-2 col-start-3"
      >
        <h2 class="services__heading font-bold text-black mb-2 lg:text-3xl">
          {{ $t("Current Requests") }}
        </h2>
        <div
          :class="[
            'overflow-visible py-2 my-2 flex gap-4 overflow-x-scroll ',
            !availableRequests || !subscription ? '' : '',
          ]"
        >
          <div
            v-if="availableRequests && availableRequests.length"
            class="card shadow-mycard w-[80%] bg-white text-primary-content flex-shrink-0"
            v-for="(request, index) in availableRequests.slice(0, 3)"
            :key="request.name"
            @click="goToCaseStudyDetail(request.name)"
          >
            <div :class="[index < 3 ? '' : 'hidden', 'card-body']">
              <div
                class="card__title flex flex-row gap-2 items-center min-w-40"
              >
                <h3 class="card-title text-sm text-wrap">{{ request.item }}</h3>
              </div>
              <ul class="leading-8 flex justify-between">
                <li>
                  <p
                    :class="{
                      'text-green-500':
                        request.status === 'New' ||
                        request.status === 'In Progress',
                      'text-red-500':
                        request.status === 'Cancelled' ||
                        request.status === 'Done',
                    }"
                    class="text-sm text-wrap"
                  >
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
          <div v-else class="card shadow-mycard text-primary-content w-full">
            <div class="card-body">
              <div class="card__title flex flex-col gap-2">
                <h1 class="card-title text-wrap text-gray-400 text-3xl">
                  {{ $t("No Current Requests") }}
                </h1>
              </div>
            </div>
          </div>
        </div>
        <div class="flex gap-4 justify-between items-center lg:justify-evenly">
          <RouterLink :to="{ name: 'ServicesView' }">
            <button
              :class="[
                'btn',
                ' btn-primary text-white border-white	 bg-primary',
                'text-white',
                !availableRequests ? 'btn-md mr-12' : 'btn-sm',
              ]"
            >
              {{ $t("Create Service Request") }}
            </button>
          </RouterLink>
          <RouterLink :to="{ name: 'RequestsView' }">
            <button
              :class="[
                'btn',
                'btn-outline',
                'text-black',
                !availableRequests ? 'btn-md mr-12' : 'btn-sm',
              ]"
            >
              {{ $t("All Requests...") }}
            </button>
          </RouterLink>
        </div>
      </div>
      <div
        class="services place-content-center px-5 flex flex-col gap-3 col-span-2 col-start-3 row-start-2"
      >
        <h2 class="services__heading font-bold text-black lg:text-3xl">
          {{ $t("Available Services") }}
        </h2>
        <!-- <h3 v-if="subscription" class="services__sub-heading">
          {{ $t("According to Your Package") }}
        </h3> -->
        <div class="w-full overflow-visible flex gap-4 py-2 overflow-x-scroll">
          <div
            v-if="
              subscription &&
              subscription.allowed_services &&
              subscription.allowed_services.length
            "
            class="card shadow-mycard bg-white text-primary-content w-[80%] max-w-96 flex-shrink-0"
            v-for="(sub, index) in subscription.allowed_services"
            :key="index"
          >
            <!-- <div :class="[index < 3 ? '' : 'hidden', 'card-body']"> -->
            <div class="card-body place-items-center place-content-center">
              <div
                class="card__title flex text-center gap-2 items-center justify-center min-w-40"
              >
                <font-awesome-icon icon="fa-regular fa-handshake" />
                <RouterLink :to="{ name: 'ServicesView' }">
                  <h3 class="card-title text-sm text-wrap">{{ sub }}</h3>
                </RouterLink>
              </div>
            </div>
          </div>
          <div
            v-else
            class="card text-primary-content w-full max-w-96 flex-shrink-0 gap-4"
          >
            <div class="card-body bg-white rounded-md relative">
              <font-awesome-icon
                :icon="['fas', 'lock']"
                class="absolute top-0 left-0"
              />
              <RouterLink :to="{ name: 'ServicesView' }">
                <div
                  class="card__title flex flex-col gap-2 items-start min-w-40"
                >
                  <h3 class="card-title text-md text-wrap">
                    <font-awesome-icon icon="fa-regular fa-handshake" />
                    {{ $t("Consultation Section") }}
                  </h3>
                  <p class="text-sm">{{ $t("Written Consultation") }}</p>
                  <p class="text-sm">{{ $t("In-Person Consultation") }}</p>
                  <p class="text-sm">{{ $t("Remote Consultation") }}</p>
                </div>
              </RouterLink>
            </div>
            <div class="card-body bg-white rounded-md relative">
              <font-awesome-icon
                :icon="['fas', 'lock']"
                class="absolute top-0 left-0"
              />
              <RouterLink :to="{ name: 'ServicesView' }">
                <div
                  class="card__title flex flex-col gap-2 items-start min-w-40"
                >
                  <h3 class="card-title text-md text-wrap">
                    <font-awesome-icon icon="fa-regular fa-handshake" />
                    {{ $t("Services Section") }}
                  </h3>
                  <p class="text-sm">{{ $t("Reconciliation Service") }}</p>
                  <p class="text-sm">{{ $t("Dispute Resolution") }}</p>
                  <p class="text-sm">{{ $t("Other Service") }}</p>
                </div>
              </RouterLink>
            </div>
            <div class="card-body bg-white rounded-md relative">
              <font-awesome-icon
                :icon="['fas', 'lock']"
                class="absolute top-0 left-0"
              />
              <RouterLink :to="{ name: 'ServicesView' }">
                <div
                  class="card__title flex flex-col gap-2 items-start min-w-40"
                >
                  <h3 class="card-title text-md text-wrap">
                    <font-awesome-icon icon="fa-regular fa-handshake" />
                    {{ $t("Litigation Section") }}
                  </h3>
                  <p class="text-sm">{{ $t("Labor Case") }}</p>
                  <p class="text-sm">{{ $t("Commercial Case") }}</p>
                  <p class="text-sm">{{ $t("Criminal Case") }}</p>
                </div>
              </RouterLink>
            </div>
          </div>
          <div v-else class="card text-primary-content w-full items-center">
            <div class="card-body">
              <div class="card__title flex flex-col gap-2">
                <h1 class="card-title text-wrap text-gray-400 text-xl mb-4">
                  {{ $t("You are not subscribed to any package.") }}
                </h1>
              </div>
              <!-- <RouterLink :to="{ name: 'ServicesView' }">
              <button class="btn  btn-primary text-white border-white	 bg-primary btn-sm text-white">إنشاء طلب خدمة</button>
            </RouterLink> -->
              <RouterLink to="/packages">
                <button
                  :class="[
                    'btn  btn-primary text-white border-white	 bg-primary text-white',
                    !subscription ? 'btn-md' : 'btn-sm',
                  ]"
                >
                  {{ $t("Subscribe Now") }}
                </button>
              </RouterLink>
            </div>
          </div>
        </div>
        <!-- <RouterLink v-if="subscription" :to="{ name: 'ServicesView' }">
          <button :class="['btn', 'btn-outline', 'text-black', 'self-center']">
            {{ $t("All Services...") }}
          </button>
        </RouterLink> -->
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
import BottomNav from "@/components/BottomNav.vue";
import SideNav from "@/components/SideNav.vue";
import Loader from "@/components/Loader.vue";
import LoggedInTopNav from "../components/LoggedInTopNav.vue";
import { useRouter } from "vue-router";
import axios from "axios";
import showToastMessage from "../router/toastmessage";

import {
  ref,
  onMounted,
  onUnmounted,
  watch,
  onBeforeUnmount,
  inject,
  reactive,
} from "vue";
import { notificationsState } from "../router/notificationsState";
import { AgCharts } from "ag-charts-vue3";
import { useQuery } from "@tanstack/vue-query";

const remHours = ref("15");
const conHours = ref("20");
const chartOptions = ref({});

const loading = ref(false);
const hasNewNotifications = ref(false);
const navigate = useRouter();
const subscription = ref([]);
const availableRequests = ref([]);
const showToast = ref(false);
const toastMessage = ref(null);

const handleRealtimeNotifications = (data) => {
  hasNewNotifications.value = true;
  console.log("socket update");
  notificationsState.hasNewNotifications = true;
};

// const setupSocketListeners = () => {
//   if (socket) {
//     socket.on("connect", () => {
//       console.log(socket.connected);
//     });

//     socket.on("disconnect", () => {
//       console.log(socket.connected);
//     });

//     socket.on("fetch_notofications", (data) => {
//       console.log(socket);
//       console.log(data);
//     });
//   } else {
//     console.error("Socket instance not found!");
//   }
// };

// const cleanupSocketListeners = () => {
//   if (socket) {
//     socket.off("user_notifications", handleRealtimeNotifications);
//   }
// };

// onBeforeUnmount(() => {
//   cleanupSocketListeners();
// });

// const markNotificationsAsViewed = () => {
//   hasNewNotifications.value = false;
// };

fetch("/api/method/frappe.auth.get_logged_user", {
  method: "GET",
  headers: { Cookie: document.cookie },
  redirect: "follow",
})
  .then((response) => {
    if (!response.ok) {
      localStorage.setItem("asp_status", 3);
      throw new Error("You are not logged In");
    }
    return response.json();
  })
  .then()
  .catch(() => navigate.replace("/"));

const getUserData = async () => {
  try {
    const response = await fetch(
      "/api/method/lsc_api.lsc_api.get_user_data.get_user_data"
    );
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    const data = await response.json();
    locale.value = data.message.user_data.language;
    console.log("lang=" + locale.value);
  } catch (error) {
    console.error("Error fetching user data:", error);
  }
};

const fetchDataQ = () =>
  axios.get(
    "/api/method/lsc_api.lsc_api.subscription_plan.subscription_plan.get_subscription_status"
  );

const { data: subData, isLoading: loadingSub } = useQuery({
  queryKey: ["subData"],
  queryFn: fetchDataQ,
  // enabled: activeIndex.value === 0,
});

const fetchCurrentRequests = () =>
  axios.get(
    "/api/method/lsc_api.lsc_api.get_current_requests.get_current_requests"
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

function loadData() {
  availableRequests.value = currentRequests?.value?.data?.message?.requests;
  const val = subData?.value?.data?.message?.data?.subscription;

  if (val && val != "null") {
    subscription.value = subData?.value?.data?.message?.data?.subscription;

    conHours.value = Math.abs(
      subscription?.value?.total_hours - subscription?.value?.remaining_hours
    );
    remHours.value = subscription?.value?.remaining_hours;
    chartOptions.value = {
      data: [
        {
          segment: t("Consumed"),
          value: parseInt(conHours.value),
        },
        {
          segment: t("Remaining"),
          value: parseInt(remHours.value),
        },
      ],
      title: {
        text: subscription?.value?.subscription_plan,
        fontFamily: "Cairo",
        fontWeight: "bold",
      },
      subtitle: {
        enabled: true,
        text: `${subscription?.value?.total_hours} ${t("Total Hours")}`,
        fontFamily: "Cairo",
      },
      legend: {
        pagination: {
          label: {
            fontFamily: "Cairo",
          },
        },
        item: {
          label: {
            fontFamily: "Cairo",
            fontWeight: "bold",
          },
        },
      },
      series: [
        {
          type: "pie",
          angleKey: "value",
          calloutLabelKey: "segment",
          sectorLabelKey: "value",
          fills: ["#981D20", "#5978B9"],
          sectorLabel: {
            color: "white",
            fontFamily: "Cairo",
            fontWeight: "bold",
          },
          tooltip: {
            enabled: false,
          },
        },
      ],
    };
  }
  loading.value = false;

  if (subData?.value?.data?.message?.asp_status == "Complete") {
    localStorage.setItem("asp_status", 2);
  } else if (localStorage.getItem("asp_status") == 1) {
    localStorage.setItem("asp_status", 1);
  } else if (localStorage.getItem("asp_status") == 3) {
    localStorage.removeItem("asp_status");
  } else {
    localStorage.setItem("asp_status", 0);
  }
}

const router = useRouter();

const goToCaseStudyDetail = (requestId) => {
  router.push({
    path: `/requests/requestDetails`,
    query: { requestId: requestId },
  });
};
// remove any uploads for request details uploading indecators
function getValueByPartialKey(partialKey) {
  for (let i = 0; i < localStorage.length; i++) {
    const key = localStorage.key(i);
    if (key && key.includes(partialKey)) {
      return localStorage.removeItem(key); // Return the value of the matched key
    }
  }
  return null; // Return null if no match is found
}
onMounted(() => {
  // localStorage.setItem("asp_status", 2);
  // localStorage.removeItem("socketOpen");
  getUserData();
  loadData();
  loading.value = true;
  setTimeout(() => {
    loadData();
    loading.value = false;
  }, 2000);

  setTimeout(() => {
    if (localStorage.getItem("asp_status") == 0) {
      showToastMessage(
        t("Complete your profile info"),
        toastMessage,
        showToast
      );
      setTimeout(() => {
        navigate.push({ path: `/profile/AccountStatusPage` });
      }, 1000);
    } else if (localStorage.getItem("asp_status") == 1) {
      showToastMessage(
        t("Complete your profile info"),
        toastMessage,
        showToast
      );
    }
  }, 2500);
});

onUnmounted(() => {
  getValueByPartialKey("uploading");
});
</script>

<style scoped>
.scrollbar-hide::-webkit-scrollbar {
  display: none;
}

.scrollbar-hide {
  -ms-overflow-style: none;
  scrollbar-width: none;
}
</style>
