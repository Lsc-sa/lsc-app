<template>
  <LoggedInTopNav :title="t('Notifications')" />
  <Loader v-if="loadingNotification" />
  <div v-else-if="isError">
    {{ error }}
  </div>
  <div
    v-else
    :dir="$i18n.locale == 'en' ? 'rtl' : 'ltr'"
    class="notification container grid grid-cols-1 grid-rows-1 mt-20 pb-16"
  >
    <div
      v-for="notification in notifications"
      :key="notification.name"
      class="bg-white border-solid border-1 border-gray-200 flex items-center justify-between gap-3 py-5 px-8 lg:px-20"
    >
      <div class="icon">
        <font-awesome-icon
          :icon="['fa-regular', 'fa-bell']"
          :class="{ 'text-red-500': notificationsState.hasNewNotifications }"
        />
      </div>
      <RouterLink
        :to="`/requests/requestDetails?requestId=${notification.document_name}`"
        v-if="notification.document_type == 'Client Transaction'"
        class="content text-right text-sm flex flex-col gap-2"
      >
        <h4 class="text-black" v-html="notification.subject"></h4>
        <p>{{ formatTimestampTo12Hour(notification.creation) }}</p>
      </RouterLink>
      <RouterLink
        to="/profile/CurrentPackage"
        v-else-if="notification.document_type == 'Subscription'"
        class="content text-right text-sm flex flex-col gap-2"
      >
        <h4 class="text-black" v-html="notification.subject"></h4>
        <p>{{ formatTimestampTo12Hour(notification.creation) }}</p>
      </RouterLink>
      <div v-else class="content text-right text-sm flex flex-col gap-2">
        <h4 class="text-black" v-html="notification.subject"></h4>
        <p>{{ formatTimestampTo12Hour(notification.creation) }}</p>
      </div>
    </div>
  </div>
  <BottomNav />
</template>

<style scoped>
.text-red-500 {
  color: #ef4444; /* Tailwind CSS red color */
}
</style>

<script setup>
import { useI18n } from "vue-i18n";
const { t, locale } = useI18n();
import Loader from "../components/Loader.vue";
import BottomNav from "../components/BottomNav.vue";
import LoggedInTopNav from "../components/LoggedInTopNav.vue";
import axios from "axios";
import { ref, onMounted, watch, onBeforeUnmount, inject } from "vue";
import { notificationsState } from "../router/notificationsState";
import { useQuery } from "@tanstack/vue-query";

const notifications = ref([]);
// const hasNewNotifications = ref(false);
// // Inject the socket instance provided in main.js
// const socket = inject("$socket");
const currentLoading = ref(false);
// Function to fetch notifications from the API
const getNotificationsData = () =>
  axios.get(
    "/api/method/lsc_api.lsc_api.get_user_notifications.get_user_notifications"
  );

const {
  data: allNotification,
  isLoading: loadingNotification,
  isError,
  error,
} = useQuery({
  queryKey: ["allNotification"],
  queryFn: getNotificationsData,
  enabled: true,
});

function formatTimestampTo12Hour(timestamp) {
  // Create a new Date object from the timestamp string
  const date = new Date(timestamp);

  // Get the name of the day (e.g., Monday, Tuesday, etc.)
  let dayName;
  if (locale.value == "en") {
    dayName = date.toLocaleDateString("en", { weekday: "short" });
  } else {
    dayName = date.toLocaleDateString("ar-EG", { weekday: "short" });
  }

  // Extract parts of the date
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, "0"); // Months are zero-indexed
  const day = String(date.getDate()).padStart(2, "0");

  // Format hours and minutes
  let hours = date.getHours();
  const minutes = String(date.getMinutes()).padStart(2, "0");
  let ampm;
  if (locale.value == "en") {
    ampm = hours >= 12 ? "PM" : "AM";
  } else {
    ampm = hours >= 12 ? "مساءاً" : "صباحاً";
  }
  hours = hours % 12 || 12; // Convert 24h to 12h format

  // Return the formatted date string with the day name
  return `${hours}:${minutes} ${ampm} -- ${dayName}، ${day}-${month}-${year}`;
}

watch([loadingNotification], ([currentLoading]) => {
  if (!currentLoading) {
    notifications.value = allNotification?.value?.data?.message;
  }
});
onMounted(() => {
  notifications.value = allNotification?.value?.data?.message;
  notificationsState.hasNewNotifications = false;
  // getNotificationsData();
  // setupSocketListeners();
});
</script>
