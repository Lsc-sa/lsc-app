<template>
  <div class="btm-nav bg-white lg:hidden">
    <router-link to="/home">
      <img :src="homeIcon" :alt="t('Home')" />
      <span>{{ $t("Home") }}</span>
    </router-link>
    <router-link to="/services">
      <img :src="servicesIcon" :alt="t('Services')" />
      <span>{{ $t("Services") }}</span>
    </router-link>
    <router-link to="/requests">
      <img :src="requestsIcon" :alt="t('Requests')" />
      <span>{{ $t("Requests") }}</span>
    </router-link>
    <router-link to="/profile">
      <img :src="profileIcon" :alt="t('Profile')" />
      <span>{{ $t("Profile") }}</span>
    </router-link>
  </div>
</template>

<script setup>
import { useI18n } from "vue-i18n";
const { t, locale } = useI18n();

import profileIcon from "../assets/images/icons/profile.svg";
import homeIcon from "../assets/images/icons/home.svg";
import requestsIcon from "../assets/images/icons/requests.svg";
import servicesIcon from "../assets/images/icons/services.svg";
import { ref } from "vue";
import { RouterLink } from "vue-router";
</script>

<style scoped>
span {
  @apply text-black text-sm px-2  p-1 text-nowrap rounded-lg duration-300 cursor-pointer;
}

.router-link-active span {
  @apply bg-primaryLight bg-opacity-50 text-primary font-bold;
}
.btm-nav {
  box-shadow: 0 -4px 20px 1px rgb(0 0 0 / 10%);
}
</style>
