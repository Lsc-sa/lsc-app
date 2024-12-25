<template>
  <!-- lg:hidden add later after modify all screens -->
  <div class="drawer drawer-end">
    <input id="my-drawer-4" type="checkbox" class="drawer-toggle" />
    <div class="drawer-content">
      <!-- Page content here -->
      <label for="my-drawer-4" aria-label="Open menu" class="drawer-button">
        <img class="block" :src="Drawer" alt="Menu" />
      </label>
    </div>
    <aside class="drawer-side">
      <label
        for="my-drawer-4"
        aria-label="Close sidebar"
        class="drawer-overlay"
        ref="closeModalClick"
      ></label>
      <nav
        class="menu bg-white min-h-full w-80 p-4 text-xl justify-between text-black"
        dir="rtl"
      >
        <!-- Close button -->
        <div class="flex justify-end closeSidebar">
          <label
            for="my-drawer-4"
            class="text-gray-600 hover:text-gray-900 cursor-pointer"
          >
            <img src="../assets/images/icons/drawer.svg" alt="" />
          </label>
        </div>
        <div class="flex justify-center mt-10">
          <img src="../assets/images/icons/logo.png" alt="" />
        </div>
        <!-- First list -->
        <ul class="menu-list">
          <li>
            <RouterLink
              to="/home"
              class="w-full hover:bg-primary rounded-lg flex flex-row-reverse justify-between"
            >
              <img src="../assets/images/icons/home.svg" alt="" />
              {{ $t("Home") }}
            </RouterLink>
          </li>
          <li>
            <RouterLink
              to="/services"
              class="w-full hover:bg-primary rounded-lg flex flex-row-reverse justify-between"
            >
              <img src="../assets/images/icons/services.svg" alt="" />
              {{ $t("Services") }}
            </RouterLink>
          </li>
          <li>
            <RouterLink
              to="/requests"
              class="w-full hover:bg-primary rounded-lg flex flex-row-reverse justify-between"
            >
              <img src="../assets/images/icons/requests.svg" alt="" />
              {{ $t("Requests") }}
            </RouterLink>
          </li>
          <li v-if="!subscriptionStatus">
            <RouterLink
              to="/packages"
              class="w-full hover:bg-primary rounded-lg flex flex-row-reverse justify-between"
            >
              <font-awesome-icon icon="fa-solid fa-receipt" />
              {{ $t("Packages") }}
            </RouterLink>
          </li>
          <!-- <li
            class="w-full hover:bg-primary rounded-lg flex flex-row-reverse justify-between"
          >
            <font-awesome-icon icon="fa-solid fa-headphones-simple" />
            <a href="#"> خدمة العملاء</a>
          </li> -->
        </ul>

        <!-- Second list -->
        <ul class="menu-list mb-22">
          <li>
            <RouterLink
              to="/profile"
              class="w-full hover:bg-primary rounded-lg flex flex-row-reverse justify-between"
            >
              <font-awesome-icon icon="fa-solid fa-gears" />
              {{ $t("Settings") }}
            </RouterLink>
          </li>
          <li
            class="w-full hover:bg-primary rounded-lg flex flex-row-reverse justify-between"
          >
            <button
              @click="handleLogOut"
              class="w-full flex flex-row-reverse justify-between"
            >
              <font-awesome-icon icon="fa-solid fa-arrow-right-from-bracket" />
              {{ $t("Logout") }}
            </button>
          </li>
        </ul>
      </nav>
    </aside>
  </div>
  <!-- Toast Notification -->
  <div v-if="showToast" class="relative">
    <div class="toast bottom-20 left-1/2 -translate-x-1/2">
      <div class="alert alert-info bg-white border-2 border-primary">
        <span>{{ toastMessage }}</span>
      </div>
    </div>
  </div>
  <!-- Loading? -->
  <div
    v-if="loading"
    class="loader absolute z-20 flex mt-[45vh] bg-gray-200 bg-opacity-40 justify-center items-center w-screen h-screen left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2"
  >
    <span class="loading text-primary loading-ring loading-lg"></span>
  </div>
  <!-- END LOADING -->
</template>

<script setup>
import { useI18n } from "vue-i18n";
const { t, locale } = useI18n();
import { useQueryClient } from "@tanstack/vue-query";
const queryClient = useQueryClient();

import Drawer from "../assets/images/icons/drawer.svg";
import { useRouter, RouterLink } from "vue-router";
import axios from "axios";
import showToastMessage from "../router/toastmessage";
import { ref, onMounted } from "vue";

// Toast Message
const toastMessage = ref(null);
const showToast = ref(false);
const navigate = useRouter();
const loading = ref(false);
const closeModalClick = ref(null);

async function handleLogOut() {
  loading.value = true;
  closeModalClick.value.click();
  try {
    await axios.get("/api/method/logout", {
      withCredentials: true,
    });
    loading.value = false;
    showToastMessage(t("Logging Out"), toastMessage, showToast);
    setTimeout(() => {
      queryClient.clear();
      localStorage.clear();
      sessionStorage.clear();
      navigate.replace("/");
    }, 700);
  } catch (error) {
    loading.value = false;
    showToastMessage(
      t("An unexpected error occurred. Please try again later."),
      toastMessage,
      showToast
    );
  }
}

const subscriptionStatus = ref(null);
async function togglePackages() {
  try {
    const response = await axios.get(
      "/api/method/lsc_api.lsc_api.subscription_plan.subscription_plan.get_subscription_status"
    );
    subscriptionStatus.value = response.data.message.data.subscription;
    if (
      subscriptionStatus.value.remaining_cases_hrs == 0 ||
      subscriptionStatus.value.remaining_legal_services_hrs == 0 ||
      subscriptionStatus.value.remaining_consultation_hrs == 0 ||
      subscriptionStatus.value.remaining_hours == 0
    ) {
      subscriptionStatus.value = false;
    } else if (response.data.message.data.subscription == null) return;
  } catch (error) {
    if (response.data.message.data.subscription == null) return;
  }
}
onMounted(() => {
  togglePackages();
});
</script>

<style scoped>
li,
li:hover {
  transition: all 0.3s ease-in-out;
}
.closeSidebar {
  position: absolute;
  left: 25px;
}
.toast {
  direction: rtl;
}
</style>
