<template>
  <iframe
    :style="{ height: heightQuery }"
    :src="invoice"
    class="w-[21cm]"
    frameborder="0"
  ></iframe>
</template>

<script setup>
import { useI18n } from "vue-i18n";
const { t, locale } = useI18n();

import { onMounted } from "vue";
import { useRoute } from "vue-router";

const route = useRoute();
const invoice = route.query.invoice || "";
const heightQuery = route.query.height || "27cm";

onMounted(() => {
  if(!invoice){
    window.close();
    return;
  }
  if (
    invoice.includes("new.najiz") ||
    invoice.includes("youtube") ||
    invoice.includes("printview")
  ) {
    window.location.href = invoice;
  } else {
    const iframe = document.querySelector("iframe");
    iframe.onload = () => {
      setTimeout(() => {
        // window.close();
      }, 2000);
    };
  }
});
</script>
