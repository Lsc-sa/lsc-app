<template>
  <div class="drawer drawer-end lg:hidden">
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
              to="/"
              class="w-full hover:bg-primary rounded-lg flex flex-row-reverse justify-between"
            >
              <img :src="servicesIcon" :alt="t('Services')" />
              {{ $t("Login") }}
            </RouterLink>
          </li>
          <li>
            <button
              @click="goHome"
              class="w-full hover:bg-primary rounded-lg flex flex-row-reverse justify-between"
            >
              <img :src="homeIcon" :alt="t('Home')" />
              {{ $t("Home") }}
            </button>
          </li>
          <li class="accomInfo flex justify-between items-center">
            <label class="label cursor-pointer w-full text-black">
              <span class="label-text">
                {{ $t("Language") }}
              </span>
              <div class="flex gap-2">
                <span class="label-text">عربي</span>
                <input
                  type="checkbox"
                  class="toggle bg-white"
                  :checked="$i18n.locale != 'ar'"
                  @change="toggleLanguage"
                />
                <span class="label-text">English</span>
              </div>
            </label>
          </li>
        </ul>
      </nav>
    </aside>
  </div>
</template>

<script setup>
import { useI18n } from "vue-i18n";
const { t, locale } = useI18n();
import homeIcon from "../assets/images/icons/home.svg";
import servicesIcon from "../assets/images/icons/services.svg";

import Drawer from "../assets/images/icons/drawer.svg";
import { useRouter, RouterLink } from "vue-router";
import { ref, onMounted } from "vue";

const closeModalClick = ref(null);
const router = useRouter();
const goHome = () => {
  const loc = window.location.origin;
  router.go(loc);
};
const toggleLanguage = () => {
  if (locale.value == "ar" || locale.value == null) {
    locale.value = "en";
  } else {
    locale.value = "ar";
  }
  // Set language in localStorage
  localStorage.setItem("language", locale.value);
  // Set language in cookies (cookie will expire in 1 year)
  document.cookie = `language=${locale.value}; path=/; max-age=${
    60 * 60 * 24 * 30 * 12
  }`;
  console.log("lang=" + locale.value);
  router.go("/");
};
onMounted(() => {
  // Check if language is set in localStorage
  const storedLanguage = localStorage.getItem("language");
  if (storedLanguage) {
    // Set language in locale
    locale.value = storedLanguage;
  }
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
