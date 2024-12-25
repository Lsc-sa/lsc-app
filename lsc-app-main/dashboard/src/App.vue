<script setup>
import { useI18n } from "vue-i18n";
const { locale } = useI18n();
import UserApp from "./views/UserApp.vue";
import { ref, onMounted } from "vue";
const language = ref("en");
// Ali was here
const getUserData = async () => {
  try {
    const response = await fetch(
      "/api/method/lsc_api.lsc_api.get_user_data.get_user_data"
    );
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    const data = await response.json();
    language.value = data.message.user_data.language;
    locale.value = language.value;
  } catch (error) {
    console.error("Error fetching user data:", error);
  }
};

onMounted(() => {
  getUserData();
});
</script>

<template>
  <UserApp />
</template>

<style>
html {
  scroll-behavior: smooth;
  background: #f2f2f2 !important;
}
body {
  font-family: "Cairo", sans-serif;
}
</style>
