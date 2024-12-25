<script setup>
import { useI18n } from "vue-i18n";
const { t, locale } = useI18n();

import { RouterView } from "vue-router";
</script>

<template>
  <RouterView />
</template>

<style>
html {
  scroll-behavior: smooth;
  direction: rtl;
  background: #f2f2f2 !important;
}
body {
  font-family: "Cairo", sans-serif;
}
</style>
